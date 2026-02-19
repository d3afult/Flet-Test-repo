import flet as ft
import time
import threading

VALID_USER = "Ali"
VALID_PASS = "12345"

def main(page: ft.Page):
    # 1. إعدادات الصفحة
    page.title = "Login App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.scroll = "adaptive"
    page.padding = 0  # نخلوه 0 في البداية عشان السبلاش تغطي الشاشة
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- تعريف عناصر الإدخال ---
    username = ft.TextField(label="Username", width=300, border_radius=10)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300, border_radius=10)
    msg = ft.Text("", color=ft.Colors.RED)

    # --- الدوال الأساسية (Login/Logout) ---
    def handle_login(e):
        if username.value == VALID_USER and password.value == VALID_PASS:
            page.clean()
            page.add(home_view())
        else:
            msg.value = "Wrong username or password"
            page.update()

    def handle_logout(e):
        username.value = ""
        password.value = ""
        msg.value = ""
        page.clean()
        page.add(login_view())

    # --- تصميم الشاشات ---

    # شاشة السبلاش (Splash Screen)
    def splash_view():
        return ft.Container(
            content=ft.Column(
                [
                    # هنا تطلع الأيقونة بتاعك (icon.png) اللي في مجلد assets
                    ft.Image(
                        src="icon.png", 
                        width=150, 
                        height=150,
                        fit=ft.ImageFit.CONTAIN,
                        animate_opacity=1000, # انيميشن خفيف (ثانية واحدة)
                    ),
                    ft.Container(height=20),
                    # دويرة التحميل
                    ft.ProgressRing(width=40, height=40, stroke_width=3, color=ft.Colors.BLUE_ACCENT),
                    ft.Text("جاري التحميل...", size=16, color=ft.Colors.BLUE_GREY_400),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.center,
        )

    # شاشة الدخول
    def login_view():
        page.padding = 20
        page.appbar = ft.AppBar(
            title=ft.Text("Login App"),
            center_title=True,
            bgcolor=ft.Colors.BLUE_50,
        )
        return ft.Column(
            controls=[
                ft.Text("Login", size=30, weight="bold"),
                username,
                password,
                msg,
                ft.ElevatedButton("Login", on_click=handle_login, width=300, height=50),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    # شاشة الهوم
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

    # --- منطق تشغيل السبلاش ثم الانتقال ---
    
    # 1. نعرضوا السبلاش أول ما يفتح الأب
    page.add(splash_view())
    page.update()

    # 2. دالة للانتقال بعد وقت معين (3 ثواني مثلاً)
    def transition_logic():
        time.sleep(3) # يراجي 3 ثواني
        page.clean() # يمسح السبلاش
        page.add(ft.SafeArea(login_view())) # يضيف الدخول داخل SafeArea
        page.update()

    # نشغلوها في خيط منفصل (Thread) عشان ما تجمدش الشاشة
    threading.Thread(target=transition_logic).start()

if __name__ == "__main__":
    # مهم جداً: نحددوا وين مجلد الصور (assets)
    ft.app(target=main, assets_dir="assets")
