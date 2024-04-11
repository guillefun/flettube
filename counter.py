import flet as ft

from pytube import YouTube, request

import os
from pathlib import Path

request.default_range_size = 500000

youtube_data = 0

def main(page: ft.Page):
  page.title = "Counter"

  #page.vertical_alignment= ft.MainAxisAlignment.CENTER
  
  txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100, border_radius=20, read_only=True)
  def in_progress(*args):
      youtube_data.value = "Download In Progress"
      page.update()
  
  def on_complete(*args):
      youtube_data.value = "Download Complete"
      page.update()

  def handle_error(*args):
      youtube_data.value = "Something went wrong, try again"
      page.update()

  def get_video(url, save_location):
    try:
        filename = str(Path(save_location).name)
        output_path = str(os.path.split(Path(save_location))[0])
        print(filename)
        print(output_path)
        download = YouTube(url, on_progress_callback=in_progress, on_complete_callback=on_complete)
        stream = download.streams.filter(progressive=True).get_highest_resolution()
        stream.download(filename=filename, output_path=output_path)
        return  
    except:
        error = True
        handle_error()
        return
      
  def search_video(e): 
    print(txt_url.value)
    print(not bool(txt_url.value.strip())) #TODO: change bool(strip) to youtube url parser
    global youtube_data
    if youtube_data != 0 or not bool(txt_url.value.strip()):
      page.remove(youtube_data)
      page.update()
    if bool(txt_url.value.strip()):
      youtube_data = ft.Row(
          [
            ft.Text("Done")
          ],
          alignment=ft.MainAxisAlignment.CENTER
        )
      page.add(
        youtube_data
      )
      page.update()
    
    get_video('https://youtu.be/2lAe1cqCOXo',"./")
    #YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
    #yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
    #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first¢#().download()

  txt_url = ft.TextField( label="Paste your URL", on_change=search_video, border_radius=20)

  page.add(
    ft.Row(
      [
        ft.Text("Download youtube videos")
      ],
      alignment=ft.MainAxisAlignment.CENTER
    )
  )

  page.add(
    ft.Row(
      [
        txt_url
      ],
      alignment=ft.MainAxisAlignment.CENTER
    )
  )

ft.app(main)



