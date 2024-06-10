import flet as ft


def main(page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.CupertinoContextMenu(
            enable_haptic_feedback=True,
            content=ft.Image("https://picsum.photos/200/200"),
            actions=[
                ft.CupertinoContextMenuAction(
                    text="Action 1",
                    is_default_action=True,
                    trailing_icon=ft.icons.CHECK,
                    on_click=lambda e: print("Action 1"),
                ),
                ft.CupertinoContextMenuAction(
                    text="Action 2",
                    trailing_icon=ft.icons.MORE,
                    on_click=lambda e: print("Action 2"),
                ),
                ft.CupertinoContextMenuAction(
                    text="Action 3",
                    is_destructive_action=True,
                    trailing_icon=ft.icons.CANCEL,
                    on_click=lambda e: print("Action 3"),
                ),
            ],
        )
    )


ft.app(target=main)