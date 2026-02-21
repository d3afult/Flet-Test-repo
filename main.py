import flet as ft
import time
import threading

VALID_USER = "Ali"
VALID_PASS = "12345"

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "Login App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.scroll = "adaptive"
    page.padding = 20
    
    # محاذاة في المنتصف
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- تعريف الحقول ---
    username = ft.TextField(label="Username", width=300)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)
    msg = ft.Text("", color=ft.Colors.RED)

    # --- الشاشات الثلاثة (كـ حاويات) ---

    # 1. السبلاش سكرين
    splash_container = ft.Column(
        controls=[
            ft.Image(src="icon.png", width=120, height=120, fit=ft.ImageFit.CONTAIN),
            ft.Container(height=20),
            ft.ProgressRing(width=40, height=40, stroke_width=3, color=ft.Colors.BLUE),
            ft.Text("جاري التحميل...", size=16),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        visible=True # ظاهرة في البداية
    )

    # 2. شاشة الدخول
    login_container = ft.Column(
        controls=[
            ft.Text("تسجيل الدخول", size=30, weight="bold"),
            username,
            password,
            msg,
            ft.ElevatedButton("Login", width=300, height=50, on_click=lambda e: handle_login()),
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        visible=False # مخفية في البداية
    )

    # 3. الشاشة الرئيسية
    home_container = ft.Column(
        controls=[
            ft.Icon(ft.Icons.CHECK_CIRCLE, size=60, color="green"),
            ft.Text(f"مرحباً {VALID_USER}!", size=25, weight="bold"),
            ft.ElevatedButton("Logout", width=300, height=45, on_click=lambda e: handle_logout()),
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        visible=False # مخفية في البداية
    )

    # --- الدوال (Logic) ---
    def handle_login():
        if username.value == VALID_USER and password.value == VALID_PASS:
            login_container.visible = False
            home_container.visible = True
            msg.value = ""
            page.update()
        else:
            msg.value = "Wrong username or password"
            page.update()

    def handle_logout():
        username.value = ""
        password.value = ""
        home_container.visible = False
        login_container.visible = True
        page.update()

    # نضيف الشاشات الثلاثة مرة وحدة للصفحة
    page.add(splash_container, login_container, home_container)

    # --- الانتقال من السبلاش للدخول ---
    def remove_splash():
        time.sleep(3) # راجي 3 ثواني
        splash_container.visible = False # أخفي السبلاش
        login_container.visible = True   # أظهر الدخول
        page.update()

    # تشغيل المؤقت في الخلفية
    threading.Thread(target=remove_splash).start()

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
