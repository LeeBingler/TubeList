# MP3 Playlist Downloader

A modern Python GUI application that allows you to easily download YouTube videos or playlists as MP3 files.
Built with **Tkinter**, **CustomTkinter**, and **pytubefix**, this project includes a simple UI, dynamic resizing, and robust error handling.

---

## Features

* Download individual YouTube videos or entire playlists
* Choose your download directory with a system file picker
* Modern, customizable interface using **CustomTkinter**
* Responsive fonts that scale with the window size
* Graceful handling of invalid URLs or network errors
* Clear and readable logs of all actions

---

## Requirements

* **Python 3.10+**
* **Pipenv** installed globally:

  ```bash
  pip install pipenv
  ```

---

## Setup and Run

1. Clone the repository:

   ```bash
   git clone https://github.com/LeeBingler/MP3-playlist-downloader.git
   cd MP3-playlist-downloader
   ```

2. Install dependencies using Pipenv:

   ```bash
   pipenv install
   ```

3. Launch the application:

   ```bash
   pipenv run python main.py
   ```

---

## Technical Details

* **Framework:** Tkinter and CustomTkinter
* **Downloader:** pytubefix
* **Environment management:** Pipenv
* **Error handling:** Built-in handling for common pytube exceptions
* **Dynamic UI:** Adjusts fonts and layout on window resize

---

## License

This project is released under the **MIT License**.
You are free to use, modify, and distribute it as you wish.

---

## Author

GitHub: [LeeBingler](https://github.com/LeeBingler)
