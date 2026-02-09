import flet as ft
import threading
import os

VALID_USER = "Ali"
VALID_PASS = "12345"

def main(page: ft.Page):
    page.title = "Login App"

    # (اختياري) لمنع شاشة فاضية بسبب الثيم/الخلفية
    page.bgcolor = ft.Colors.WHITE
    page.theme_mode = ft.ThemeMode.LIGHT

    # ✅ إعدادات النافذة فقط لسطح المكتب (مش Android)
    if hasattr(page, "window") and page.platform in (
        ft.PagePlatform.WINDOWS,
        ft.PagePlatform.MACOS,
        ft.PagePlatform.LINUX,
    ):
        try:
            page.window.width = 420
            page.window.height = 520
            page.window.resizable = False
        except Exception:
            pass

    username = ft.TextField(label="Username", width=320)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=320)
    msg = ft.Text(value="", color=ft.Colors.RED)

    def exit_app(e):
        # ✅ على Android: اقفل الصفحة بدون kill للتطبيق
        if page.platform in (ft.PagePlatform.ANDROID, ft.PagePlatform.IOS):
            page.window_close()
            return

        # ✅ Desktop: منطقك السابق (مع failsafe)
        try:
            page.snack_bar = ft.SnackBar(ft.Text("Closing..."))
            page.snack_bar.open = True
            page.update()
        except Exception:
            pass

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

    def show_login():
        page.controls.clear()
        page.add(
            ft.Column(
                controls=[
                    ft.Text("Login", size=28, weight=ft.FontWeight.BOLD),
                    username,
                    password,
                    msg,
                    ft.ElevatedButton(text="Login", width=320, on_click=handle_login),
                    ft.OutlinedButton(text="Exit App", width=320, on_click=exit_app),
                ],
                spacing=12,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            )
        )
        page.update()

    def show_home():
        page.controls.clear()
        page.add(
            ft.Column(
                controls=[
                    ft.Text(f"Hi {VALID_USER}", size=30, weight=ft.FontWeight.BOLD),
                    ft.ElevatedButton(text="Logout", width=320, on_click=handle_logout),
                    ft.OutlinedButton(text="Exit App", width=320, on_click=exit_app),
                ],
                spacing=14,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
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
        password.value = ""
        msg.value = ""
        show_login()

    show_login()

# ✅ خليه كده: يشتغل Desktop + Android
ft.app(target=main)

