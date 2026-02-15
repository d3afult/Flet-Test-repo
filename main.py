import flet as ft

VALID_USER = "Ali"
VALID_PASS = "12345"

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "Login App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    
    # أهم سطر للموبايل: يخلي الصفحة تقبل السكرول لو المحتوى طويل
    page.scroll = ft.ScrollMode.AUTO
    
    # محاذاة العناصر
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # AppBar
    page.appbar = ft.AppBar(
        title=ft.Text("Login App"),
        center_title=True,
        bgcolor=ft.Colors.BLUE_50,
    )

    # عناصر الإدخال
    username = ft.TextField(label="Username", autofocus=True)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    msg = ft.Text("", color=ft.Colors.RED)

    # دالة العرض الرئيسية
    def show(view: ft.Control):
        page.clean() # بديل لـ controls.clear() أحياناً يكون أضمن
        
        # استخدام SafeArea ضروري في الموبايل عشان ما يجيش المحتوى تحت شريط الساعة
        page.add(
            ft.SafeArea(
                ft.Container(
                    # نحول الـ expand=True عشان ما يسببش مشاكل مع الـ Scroll
                    padding=20,
                    alignment=ft.alignment.center,
                    content=ft.Container(
                        # نخلو العرض مرن، أقصى شي 400 لكن يصغر لو الشاشة صغيرة
                        width=None, 
                        constraints=ft.BoxConstraints(max_width=400),
                        padding=20,
                        border_radius=16,
                        # حطيتلك لون خلفية خفيف (رمادي) عشان تميز الكونتينر عن الخلفية البيضاء
                        bgcolor=ft.Colors.GREY_100, 
                        content=view,
                    ),
                ),
                expand=True, # SafeArea هو اللي ياخذ الـ expand
            )
        )
        page.update()

    def handle_login(e):
        u = (username.value or "").strip()
        p = (password.value or "").strip()

        if u == VALID_USER and p == VALID_PASS:
            msg.value = ""
            show_home()
        else:
            msg.value = "Wrong username or password"
            page.update()

    def handle_logout(e):
        username.value = ""
        password.value = ""
        msg.value = ""
        show_login()

    def show_login():
        msg.value = ""
        show(
            ft.Column(
                controls=[
                    ft.Text("Login", size=28, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    username,
                    password,
                    msg,
                    ft.ElevatedButton(
                        "Login", 
                        on_click=handle_login,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                        height=50, # تكبير الزر شوية للمس
                    ),
                ],
                spacing=15,
                # هذا يخلي العناصر تتمدد لعرض الكونتينر
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            )
        )

    def show_home():
        show(
            ft.Column(
                controls=[
                    ft.Icon(ft.Icons.CHECK_CIRCLE, size=60, color=ft.Colors.GREEN),
                    ft.Text(f"Ahlan {VALID_USER}", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.ElevatedButton("Logout", on_click=handle_logout, height=50),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            )
        )

    show_login()

if __name__ == "__main__":
    ft.app(target=main)
