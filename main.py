import flet as ft
import asyncio # استخدمنا asyncio بدل time عشان ما نجمدوش التطبيق

async def main(page: ft.Page):
    # --- 1. إعدادات الصفحة الاحترافية ---
    page.title = "Login App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.padding = 0 # حنخلوه 0 عشان الـ Splash تاخذ راحتها
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- 2. تعريف واجهة السبلاش سكرين ---
    # Container كبير يغطي الشاشة
    splash_view = ft.Container(
        content=ft.Column(
            [
                ft.Image(src="icon.png", width=150, height=150),
                ft.Container(height=20),
                ft.ProgressRing(width=40, color="blue"),
                ft.Text("جاري التحميل...", size=16, weight="w500"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=True,
        bgcolor=ft.Colors.WHITE,
        visible=True
    )

    # --- 3. تعريف واجهة تسجيل الدخول ---
    login_view = ft.SafeArea(
        content=ft.Container(
            padding=20,
            content=ft.Column(
                [
                    ft.Text("Login", size=32, weight="bold"),
                    ft.TextField(label="Username", width=300, border_radius=10),
                    ft.TextField(label="Password", password=True, width=300, border_radius=10),
                    ft.Container(height=10),
                    ft.ElevatedButton("Login", width=300, height=50),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
        visible=False # مخفية في البداية
    )

    # إضافة الواجهات للصفحة
    page.add(splash_view, login_view)
    
    # تحديث الصفحة لأول مرة عشان تطلع السبلاش طول
    await page.update_async()

    # --- 4. منطق الانتقال (هنا التغيير الجوهري) ---
    # ننتظروا 3 ثواني بدون ما نجمدوا التطبيق
    await asyncio.sleep(3)
    
    # تبديل الرؤية
    splash_view.visible = False
    login_view.visible = True
    
    # تحديث الصفحة بعد التغيير
    await page.update_async()

# تشغيل التطبيق بنمط الـ Async
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
