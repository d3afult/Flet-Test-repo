import flet as ft

VALID_USER = "Ali"
VALID_PASS = "12345"

def main(page: ft.Page):
    # 1. إعدادات الصفحة (ضرورية للموبايل)
    page.title = "Login App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.scroll = "adaptive"  # عشان لو قلبت الموبايل او طلع الكيبورد
    page.padding = 20

    # 2. التنسيق (عشان يجي في النص)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.appbar = ft.AppBar(
        title=ft.Text("Login App"),
        center_title=True,
        bgcolor=ft.Colors.BLUE_50,
    )

    # تعريف العناصر بره عشان نقدر نوصلولهم
    username = ft.TextField(label="Username", width=300)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)
    msg = ft.Text("", color=ft.Colors.RED)

    # دالة الدخول
    def handle_login(e):
        if username.value == VALID_USER and password.value == VALID_PASS:
            page.clean() # نمسح المحتوى القديم
            page.add(home_view()) # نضيف صفحة الهوم
        else:
            msg.value = "Wrong username or password"
            page.update()

    # دالة الخروج
    def handle_logout(e):
        username.value = ""
        password.value = ""
        msg.value = ""
        page.clean()
        page.add(login_view())

    # 3. تصميم صفحة الدخول (بدون expand)
    def login_view():
        return ft.Column(
            controls=[
                ft.Text("Login", size=30, weight="bold"),
                username,
                password,
                msg,
                ft.ElevatedButton("Login", on_click=handle_login, width=300, height=45),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    # 4. تصميم صفحة الهوم
    def home_view():
        return ft.Column(
            controls=[
                ft.Icon(ft.Icons.CHECK_CIRCLE, size=60, color="green"),
                ft.Text(f"Welcome {VALID_USER}!", size=25, weight="bold"),
                ft.ElevatedButton("Logout", on_click=handle_logout, width=300, height=45),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    # أول ما يفتح التطبيق نعرضوا الـ Login
    # استخدمنا SafeArea عشان النوتش
    page.add(ft.SafeArea(login_view()))

if __name__ == "__main__":
    ft.app(target=main)
