import flet as ft
import threading
import os

VALID_USER = "Ali"
VALID_PASS = "12345"

def main(page: ft.Page):
    page.title = "Login App"

    # ✅ توافق مع الإصدارات: بعض الإصدارات فيها page.window وبعضها فيها page.window_width...
    if hasattr(page, "window"):
        try:
            page.window.width = 420
            page.window.height = 520
            page.window.resizable = False
        except Exception:
            pass
    else:
        # API قديم
        page.window_width = 420
        page.window_height = 520
        page.window_resizable = False

    username = ft.TextField(label="Username", width=320)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=320)
    msg = ft.Text(value="", color=ft.Colors.RED)

    def exit_app(e):
        # (اختياري) مؤشر للمستخدم
        try:
            page.snack_bar = ft.SnackBar(ft.Text("Closing..."))
            page.snack_bar.open = True
            page.update()
        except Exception:
            pass

        def really_close():
            # ✅ الطريقة الموصى بها لسطح المكتب: page.window.close() / destroy()
            # لكن في بعض الإصدارات destroy يسبب Freeze لثواني، فنجرب close أولًا
            try:
                if hasattr(page, "window"):
                    try:
                        page.window.close()   # غالبًا أسرع/أنعم
                    except Exception:
                        page.window.destroy() # خيار بديل (قد يتأخر/يعلق لحظات)
                else:
                    # API قديم
                    page.close()
            except Exception:
                pass

            # ✅ Failsafe: لو ما قفل خلال 1 ثانية، اقفل العملية نهائيًا بدون تجميد طويل
            def force_kill():
                os._exit(0)

            threading.Timer(1.0, force_kill).start()

        # نفذ الإغلاق خارج حدث الزر لتقليل "Not Responding"
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

# ✅ تشغيل كنافذة Desktop
ft.app(target=main, view=ft.AppView.FLET_APP)
