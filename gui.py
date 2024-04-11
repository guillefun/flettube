import flet as ft


# set by main
run_backend = None

def main(page: ft.Page):
    page.title = "Youtube Downloader"
    #page.vertical_alignment = "center"
    page.window_height = 600
    page.window_width = 1200



    def pick_file_result(e: ft.FilePickerResultEvent):
        selected_path.value = pick_file_dialog.result.path + ".mp4"
        page.update()


    def handle_submit(e):
        if not url_input.value:
            url_input.error_text = "Please enter URL"
            page.update()
        else:
            url_input.error_text = None
            run_backend(url_input.value,selected_path.value, in_progress, on_complete, handle_error)
            page.update()

    def in_progress(*args):
        download_complete.value = "Download In Progress"
        page.update()
    
    def on_complete(*args):
        download_complete.value = "Download Complete"
        page.update()

    def handle_error(*args):
        download_complete.value = "Something went wrong, try again"
        page.update()
    

    url_input = ft.TextField(label="Video URL")
    pick_file_dialog = ft.FilePicker(on_result=pick_file_result)
    pick_file_button = ft.ElevatedButton(
        "Pick File Name",
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: pick_file_dialog.save_file(
            file_type="video", 
            allowed_extensions=["mp4"])
        )
    page.overlay.append(pick_file_dialog)
    selected_path = ft.Text()
    #selected_path.value = "File Save Location"

    download_button = ft.TextButton("Download", on_click=handle_submit)
    
    download_complete = ft.Text()

    page.add(
      ft.Row(
        [
          ft.Text("Download youtube videos")
        ],
        alignment=ft.MainAxisAlignment.CENTER
      )
    )
    page.add(
        ft.Column(
            [   
                ft.Row([
                    url_input
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([
                    pick_file_button,
                    selected_path
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([
                    download_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER
                    ),
                ft.Row([
                    download_complete
                ],
                alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=50
        )
    )

def run_gui():
    ft.app(target=main)


if __name__ == "__main__":
    run_gui()