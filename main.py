import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        
        # Getting the YouTube link and creating a YouTube object
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        # Updating the title to show that the download is in progress
        title.configure(text="Downloading: " + ytObject.title, text_color="blue")

        # Downloading the video
        video.download()
        finishedLabel.configure(text="Download completed", text_color="green")
    except Exception as e:
        finishedLabel.configure(text="Error: " + str(e), text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Downloaded: {percentage:.2f}%")

    # Update percentage label
    per = f"{percentage:.2f}%"
    pPercentage.configure(text=per)
    pPercentage.update()

    # Update progress bar
    progressBar.set(percentage / 100)
    progressBar.update()

def clearFields():
    link.set("")  # Clear the StringVar
    title.configure(text="Insert a YouTube link", text_color="black")
    finishedLabel.configure(text="")
    pPercentage.configure(text="0%")
    progressBar.set(0)

# System Setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI Elements

# Title label
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input
link = tkinter.StringVar()
link_entry = customtkinter.CTkEntry(app, width=350, height=40, textvariable=link)
link_entry.pack(padx=10, pady=10)

# Finished Download
finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack(padx=10, pady=10)

# Progress bar
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download_button = customtkinter.CTkButton(app,
                                          width=150,
                                          height=40,
                                          text="Download",
                                          command=startDownload)
download_button.pack(padx=10, pady=10)

# Clear button
clear_button = customtkinter.CTkButton(app,
                                       width=150,
                                       height=40,
                                       text="Clear",
                                       command=clearFields)
clear_button.pack(padx=10, pady=10)

# Run app
app.mainloop()
