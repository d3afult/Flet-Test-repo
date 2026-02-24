import flet as ft
import traceback

def main(page: ft.Page):
    # --- إعدادات الصفحة ---
    page.title = "App with Notifications"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- دالة إرسال إشعار تجريبي ---
    def send_notification(e):
        # هذا الإشعار يظهر من أسفل الشاشة بشكل أنيق
        page.open(
            ft.SnackBar(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.NOTIFICATIONS_ACTIVE, color=ft.Colors.WHITE),
                        ft.Text("هذا إشعار تجريبي: لقد قمت بضغط الزر بنجاح!"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                bgcolor=ft.Colors.BLUE_800, # لون الإشعار
                action="فهمت", # زر داخل الإشعار لإغلاقه
                duration=4000, # يختفي بعد 4 ثواني
            )
        )

    try:
        # --- الحقول ---
        user_input = ft.TextField(label="اسم المستخدم", width=300, border_radius=10)
        pass_input = ft.TextField(label="كلمة المرور", password=True, width=300, border_radius=10)
        error_txt = ft.Text("", color="red")

        # --- واجهة تسجيل الدخول ---
        login_ui = ft.Column(
            [
                ft.Icon(ft.Icons.LOCK_PERSON, size=80, color="blue"),
                ft.Text("تسجيل الدخول", size=30, weight="bold"),
                user_input,
                pass_input,
                error_txt,
                ft.ElevatedButton(
                    "دخول", 
                    width=300, 
                    height=50,
                    on_click=lambda _: handle_login()
                ),
                ft.Container(height=20),
                # زر تجربة الإشعار
                ft.TextButton(
                    "إرسال إشعار تجريبي (Test)", 
                    icon=ft.Icons.NOTIFICATION_ADD,
                    on_click=send_notification
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        # --- دالة الدخول ---
        def handle_login():
            if user_input.value == "Ali" and pass_input.value == "12345":
                error_txt.value = ""
                # إشعار نجاح الدخول
                page.open(
                    ft.SnackBar(
                        content=ft.Text(f"مرحباً بك {user_input.value}!"),
                        bgcolor=ft.Colors.GREEN_700
                    )
                )
                page.update()
            else:
                error_txt.value = "البيانات غير صحيحة"
                page.update()

        page.add(ft.SafeArea(login_ui))

    except Exception:
        page.add(ft.Text(f"خطأ: {traceback.format_exc()}", color="red"))

if __name__ == "__main__":
    ft.app(target=main)
