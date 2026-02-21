import flet as ft
import time

VALID_USER = "Ali"
VALID_PASS = "12345"

def main(page: ft.Page):
    # --- 1. إعدادات الصفحة (قاهر الشاشة البيضاء) ---
    page.title = "Login App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    
    # التعديلات الأساسية للموبايل
    page.scroll = "adaptive"  # مهم جداً لمنع تعليق الواجهة
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- 2. تعريف الحقول ---
    username = ft.TextField(label="Username", width=300, border_radius=10)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300, border_radius=10)
    msg = ft.Text("", color=ft.Colors.RED)

    # --- 3. تصميم الحاويات (الشاشات) ---

    # واجهة السبلاش (تظهر أولاً)
    splash_container = ft.Column(
        controls=[
            # عرض الأيقونة من مجلد assets
            ft.Image(
                src="icon.png", 
                width=150, 
                height=150, 
                fit=ft.ImageFit.CONTAIN,
                error_content=ft.Icon(ft.Icons.IMAGE_NOT_SUPPORTED, size=50) # احتياطي
            ),
            ft.Container(height=20),
            ft.ProgressRing(width=40, height=40, stroke_width=3, color=ft.Colors.BLUE),
            ft.Text("جاري التحميل...", size=16, color=ft.Colors.BLUE_GREY),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        visible=True 
    )

    # واجهة تسجيل الدخول
    login_container = ft.Column(
        controls=[
            ft.Icon(ft.Icons.LOCK_OUTLINE_ROUNDED, size=80, color=ft.Colors.BLUE_GREY),
            ft.Text("تسجيل الدخول", size=30, weight="bold"),
            ft.Container(height=10),
            username,
            password,
            msg,
            ft.ElevatedButton(
                "Login", 
                width=300, 
                height=50, 
                on_click=lambda e: handle_login(),
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
            ),
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        visible=False 
    )

    # الواجهة الرئيسية
    home_container = ft.Column(
        controls=[
            ft.Icon(ft.Icons.CHECK_CIRCLE_OUTLINE_ROUNDED, size=80, color="green"),
            ft.Text(f"مرحباً {VALID_USER}!", size=25, weight="bold"),
            ft.Text("تم تسجيل الدخول بنجاح", color="grey"),
            ft.Container(height=20),
            ft.ElevatedButton("Logout", width=300, height=50, on_click=lambda e: handle_logout()),
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        visible=False
    )

    # --- 4. المنطق البرمجي (Logic) ---

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

    # دالة الانتقال (تنفذ بعد ظهور الصفحة)
    async def remove_splash(e):
        time.sleep(3.5) # الانتظار لعرض السبلاش
        splash_container.visible = False
        login_container.visible = True
        await page.update_async()

    # --- 5. تجميع الصفحة داخل SafeArea ---
    # استخدام SafeArea يضمن عدم اختفاء المحتوى تحت "النوتش"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                [splash_container, login_container, home_container],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
    )

    # تشغيل مهمة الانتقال بشكل آمن
    page.run_task(remove_splash)

if __name__ == "__main__":
    # تشغيل التطبيق مع تحديد مجلد الصور
    ft.app(target=main, assets_dir="assets")
