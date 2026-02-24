import flet as ft
import traceback

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "Login App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    try:
        # واجهة تسجيل الدخول مباشرة (لا يوجد سبلاش ولا انتظار)
        login_view = ft.Column(
            [
                # استخدمنا أيقونة جاهزة وخفيفة جداً في التحميل
                ft.Icon(ft.Icons.LOCK_PERSON_ROUNDED, size=80, color=ft.Colors.BLUE),
                ft.Text("تسجيل الدخول", size=30, weight="bold"),
                ft.Container(height=10),
                ft.TextField(label="اسم المستخدم", width=300, border_radius=10),
                ft.TextField(label="كلمة المرور", password=True, can_reveal_password=True, width=300, border_radius=10),
                ft.Container(height=10),
                ft.ElevatedButton(
                    "دخول", 
                    width=300, 
                    height=50,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        # إضافة الواجهة داخل SafeArea لضمان استقرار الشاشة
        page.add(ft.SafeArea(login_view))

    except Exception as e:
        # فخ الأخطاء الطوارئ (باش ما نرجعوش للشاشة البيضاء أبداً)
        page.add(ft.SafeArea(ft.Text(f"ERROR:\n{traceback.format_exc()}", color=ft.Colors.RED)))

if __name__ == "__main__":
    # تشغيل التطبيق (بدون assets_dir مؤقتاً لتجنب أي كراش في مسارات الأندرويد)
    ft.app(target=main)
