import flet as ft
import time
import threading
import traceback # مكتبة صيد الأخطاء

def main(page: ft.Page):
    # إعدادات أساسية ومضمونة 100% في الأندرويد
    page.title = "Login App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    try:
        # --- 1. الشاشات ---
        # استخدمنا أيقونة عادية (ROCKET) بدل صورتك مؤقتاً لعزل المشكلة
        splash = ft.Column(
            [
                ft.Icon(ft.Icons.ROCKET_LAUNCH, size=100, color=ft.Colors.BLUE),
                ft.Text("جاري التحميل...", size=20, weight="bold"),
                ft.ProgressBar(width=200)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            visible=True
        )

        login = ft.Column(
            [
                ft.Text("تسجيل الدخول", size=30, weight="bold"),
                ft.TextField(label="Username", width=300),
                ft.TextField(label="Password", password=True, width=300),
                ft.ElevatedButton("Login", width=300, height=50)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            visible=False
        )

        # إضافة الشاشات داخل SafeArea آمنة
        page.add(ft.SafeArea(ft.Column([splash, login], horizontal_alignment=ft.CrossAxisAlignment.CENTER)))

        # --- 2. دالة الانتقال (مع فخ أخطاء خاص بيها) ---
        def start_app():
            try:
                time.sleep(3)
                splash.visible = False
                login.visible = True
                page.update()
            except Exception as e:
                # لو صار خطأ في وقت الانتقال، اطبعه على الشاشة
                page.add(ft.Text(f"Transition Error: {traceback.format_exc()}", color=ft.Colors.RED))
                page.update()

        # التشغيل في الخلفية
        threading.Thread(target=start_app, daemon=True).start()

    except Exception as e:
        # السحر هنا: لو التطبيق ضرب أول ما فتح، حيطبعلك الخطأ هنا بدل الشاشة البيضاء!
        error_msg = traceback.format_exc()
        page.add(ft.SafeArea(ft.Text(f"CRASH ERROR:\n{error_msg}", color=ft.Colors.RED, selectable=True)))
        page.update()

if __name__ == "__main__":
    # مسحنا `assets_dir` مؤقتاً لأنها المتهم الأول في تعليق الأندرويد
    ft.app(target=main)
