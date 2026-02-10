import flet as ft

VALID_USER = "Ali"
VALID_PASS = "12345"

def main(page: ft.Page):
    page.title = "Login App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE

    # AppBar
    page.appbar = ft.AppBar(
        title=ft.Text("Login App"),
        center_title=True,
    )

    # عناصر الإدخال
    username = ft.TextField(label="Username", autofocus=True)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    msg = ft.Text("", color=ft.Colors.RED)

    def show(view: ft.Control):
        page.controls.clear()
        page.add(
            ft.Container(
                expand=True,
                padding=20,
                alignment=ft.alignment.center,
                content=ft.Container(
                    width=420,  # حد أقصى على الشاشات الكبيرة
                    padding=20,
                    border_radius=16,
                    bgcolor=ft.Colors.WHITE,
                    content=view,
                ),
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
                    ft.ElevatedButton("Login", on_click=handle_login),
                ],
                spacing=12,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            )
        )

    def show_home():
        show(
            ft.Column(
                controls=[
                    ft.Text(f"Hi {VALID_USER}", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.ElevatedButton("Logout", on_click=handle_logout),
                ],
                spacing=12,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            )
        )

    show_login()

ft.app(target=main)

