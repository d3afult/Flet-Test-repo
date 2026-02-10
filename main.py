import flet as ft
import threading
import os

VALID_USER = "Ali"
VALID_PASS = "12345"

def main(page: ft.Page):
    page.title = "Login App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE

    # ✅ AppBar ثابت
    def exit_app(e=None):
        if page.platform in (ft.PagePlatform.ANDROID, ft.PagePlatform.IOS):
            page.window_close()
            return

        # Desktop close (failsafe)
        def really_close():
            try:
                if hasattr(page, "window"):
                    try:
                        page.window.close()
                    except Exception:
                        page.window.destroy()
                else:
                    page.close()
            except Exception:
                pass
            threading.Timer(1.0, lambda: os._exit(0)).start()

        threading.Timer(0.05, really_close).start()

    page.appbar = ft.AppBar(
        title=ft.Text("Login App"),
        center_title=True,
        actions=[ft.IconButton(icon=ft.Icons.EXIT_TO_APP, on_click=exit_app)],
    )

    # ✅ جذر بسيط وواضح
    root = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[],
    )
    page.add(root)

    username = ft.TextField(label="Username", autofocus=True)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    msg = ft.Text("", color=ft.Colors.RED)

    def card(controls):
        # ✅ بدون shadow (عشان ما يكسر على بعض الإصدارات)
        return ft.Container(
            content=ft.Column(
                controls=controls,
                spacing=12,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            ),
            padding=20,
            border_radius=16,
            bgcolor=ft.Colors.WHITE,
            width=360,  # شكل مرتب على الموبايل
        )

    def render(widget):
        root.controls.clear()
        # ✅ سنتر + بادينج مناسب لأي شاشة
        root.controls.append(
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                padding=20,
                content=widget,
            )
        )
        page.update()

    def show_error(err: Exception):
        render(
            card([
                ft.Text("UI Error", size=22, weight=ft.FontWeight.BOLD),
                ft.Text(str(err)),
                ft.ElevatedButton("Back", on_click=lambda e: show_login()),
            ])
        )

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
        password.value = ""
        msg.value = ""
        show_login()

    def show_login():
        try:
            msg.value = ""
            render(
                card([
                    ft.Text("Login", size=28, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    username,
                    password,
                    msg,
                    ft.ElevatedButton("Login", on_click=handle_login),
                    ft.OutlinedButton("Exit App", on_click=exit_app),
                ])
            )
        except Exception as ex:
            show_error(ex)

    def show_home():
        try:
            render(
                card([
                    ft.Text(f"Hi {VALID_USER}", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.ElevatedButton("Logout", on_click=handle_logout),
                    ft.OutlinedButton("Exit App", on_click=exit_app),
                ])
            )
        except Exception as ex:
            show_error(ex)

    show_login()

ft.app(target=main)
