# NEX-SPLIT-PS3-ISO-Split-Tool

**NEX SPLIT** is a lightweight utility designed for **modded/jailbroken PS3 consoles**. It splits large PS3 ISO files into smaller parts, making them easier to transfer to a **FAT32 USB drive**, which has a file-size limitation of around 4 GB.

## Features

* 🎮 Designed for **modded/jailbroken PS3 consoles**
* 💿 Splits large **PS3 ISO** files into multiple parts
* 💾 Useful for transferring ISO files to **FAT32 USB drives**
* 📁 Easy ISO and output-folder selection
* ⚙️ Customizable split size
* 📊 Real-time progress bar and status
* 🖥️ Modern dark interface built with **CustomTkinter**
* 🚀 Uses threading to keep the interface responsive during the split process

## How It Works

NEX SPLIT reads the selected ISO file and divides it into smaller chunks based on the size you choose.

The generated files are named like:

`GAME_NAME.ISO.0`
`GAME_NAME.ISO.1`
`GAME_NAME.ISO.2`
`...`

The resulting parts can then be copied to a FAT32 USB drive and used with a compatible PS3 setup and manager such as **webMAN MOD**, depending on your console configuration.

## How to Use

1. Select your **PS3 `.iso`** file.
2. Choose the **output folder**.
3. Set the desired **split size**.
4. Click **SPLIT ISO**.
5. Wait until the process reaches **100%**.
6. Copy the generated parts to your USB drive.
7. Use them with your compatible modded PS3 setup.

## Built With

* Python
* CustomTkinter
* Tkinter
* Threading
* OS file handling

## Disclaimer

This tool only splits ISO files into smaller pieces. It does **not** modify, decrypt, or alter the contents of the ISO.

Use this software with game backups that you legally own.

**Made by Nexxus** 🎮
