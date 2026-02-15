import flet as ft
import traceback

def main(page: ft.Page):
    # إعدادات أساسية عشان نضمنوا الرؤية
    page.title = "Test App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.padding = 20
    page.scroll = "adaptive"  # مهم جداً للموبايل

    # الـ AppBar
    page.appbar = ft.AppBar(
        title=ft.Text("Login Test"),
        center_title=True,
        bgcolor=ft.Colors.BLUE_100,
    )

    # هنا اللقطة: نبي نطبع أي خطأ يصير على الشاشة طول
    try:
        # عناصر بسيطة ومباشرة بدون دوال معقدة
        t_title = ft.Text("Login Page", size=30, color="black", weight="bold")
        tf_user = ft.TextField(label="Username", width=300)
        tf_pass = ft.TextField(label="Password", password=True, width=300)
        btn_login = ft.ElevatedButton("Login", width=300, height=50)

        # دالة بسيطة للزر
        def on_click(e):
            if tf_user.value == "Ali" and tf_pass.value == "123":
                page.snack_bar = ft.SnackBar(ft.Text("Success!"))
                page.snack_bar.open = True
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Wrong!"))
                page.snack_bar.open = True
            page.update()

        btn_login.on_click = on_click

        # الإضافة المباشرة للصفحة (أضمن طريقة)
        page.add(
            ft.Column(
                [
                    t_title,
                    tf_user,
                    tf_pass,
                    btn_login
                ],
                alignment=ft.MainAxisAlignment.START, # يبدأ من فوق
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )
    
    except Exception as e:
        # لو صار أي خطأ فني، حيطلعلك مكتوب بالأحمر ع الشاشة
        page.add(ft.Text(f"Error: {e}\n{traceback.format_exc()}", color="red"))

    page.update()

if __name__ == "__main__":
    ft.app(target=main)
