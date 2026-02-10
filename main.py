import flet as ft
import threading
import os

VALID_USER = "Ali"
VALID_PASS = "12345"

def main(page: ft.Page):
    page.title = "Login App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE

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

    username = ft.TextField(label="Username", autofocus=True)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    msg = ft.Text(value="", color=ft.Colors.RED)

    def exit_app(e=None):
        # ✅ Mobile: اقفل الصفحة بدون kill
        if page.platform in (ft.PagePlatform.ANDROID, ft.PagePlatform.IOS):
            page.window_close()
            return

        # ✅ Desktop: اغلاق لطيف + failsafe
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

    # ✅ AppBar ثابت لكل الصفحات
    page.appbar = ft.AppBar(
        title=ft.Text("Login App"),
        center_title=True,
        actions=[
            ft.IconButton(icon=ft.Icons.EXIT_TO_APP, tooltip="Exit", on_click=exit_app)
        ],
    )

    # ✅ حاوية محتوى Responsive: تاخذ عرض الشاشة لكن تحده في الشاشات الكبيرة
    content = ft.Container(
        padding=20,
        alignment=ft.alignment.center,
        expand=True,
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[],
        ),
    )

    def build_card(controls):
        # كارد وسط الشاشة، يتمدد على الموبايل ويكون شكله مرتب على الكبير
        return ft.Container(
            content=ft.Column(
                controls=controls,
                spacing=12,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            ),
            padding=20,
            border_radius=16,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(
                blur_radius=18,
                spread_radius=1,
                color=ft.Colors.BLACK12,
                offset=ft.Offset(0, 6),
            ),
            width=420,              # حد أقصى شكلي على الكبير
            # على الموبايل بيتمدد تلقائياً بسبب الـ layout والـ padding
        )

    def show_login():
        msg.value = ""
        username.value = ""
        password.value = ""

        card = build_card([
            ft.Text("Login", size=28, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            username,
            password,
            msg,
            ft.ElevatedButton(text="Login", on_click=handle_login),
            ft.OutlinedButton(text="Exit App", on_click=exit_app),
        ])

        content.content.controls.clear()
        content.content.controls.append(
            ft.Row(
                controls=[card],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
        page.update()

    def show_home():
        card = build_card([
            ft.Text(f"Hi {VALID_USER}", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.ElevatedButton(text="Logout", on_click=handle_logout),
            ft.OutlinedButton(text="Exit App", on_click=exit_app),
        ])

        content.content.controls.clear()
        content.content.controls.append(
            ft.Row(
                controls=[card],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
        page.update()

    def handle_login(e):
        u = (username.value or "").strip()
        p = (password.value or "").strip()

        if u == VALID_USER and p == VALID_PASS:
            show_home()
        else:
            msg.value = "Wrong username or password"
            page.update()

    def handle_logout(e):
        show_login()

    # ✅ ضع المحتوى مرة واحدة
    page.add(content)
    show_login()

ft.app(target=main)
