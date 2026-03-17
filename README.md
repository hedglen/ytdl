# ytdl

yt-dlp wrapper with presets. Downloads go straight to `D:/media/Downloads`.

## Usage

```powershell
ytdl <url>                        # best quality video (mp4)
ytdl <url> --quality 1080         # cap at 1080p
ytdl <url> --audio                # audio only (mp3)
```

## Config

Edit `config.toml` to change download directory, default quality, or format.

## Setup

```powershell
cd projects/ytdl
python -m venv .venv
.venv/Scripts/pip install rich
```

The `ytdl` alias is registered in the PowerShell profile via dotfiles.
