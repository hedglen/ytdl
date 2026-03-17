#!/usr/bin/env python3
"""ytdl — yt-dlp wrapper. Downloads to D:/media/Downloads."""

import subprocess
import sys
import tomllib
from pathlib import Path

from rich.console import Console
from rich.panel import Panel

console = Console()

CONFIG_PATH = Path(__file__).parent / "config.toml"


def load_config() -> dict:
    with open(CONFIG_PATH, "rb") as f:
        return tomllib.load(f)


def build_args(url: str, cfg: dict, quality: str | None, audio_only: bool) -> list[str]:
    out_dir = cfg["paths"]["download_dir"]
    fmt = cfg["defaults"]["format"]
    q = quality or cfg["defaults"]["quality"]

    args = ["yt-dlp", "--no-mtime", "-o", f"{out_dir}/%(title)s.%(ext)s"]

    if audio_only:
        args += ["-x", "--audio-format", "mp3"]
        if cfg["defaults"]["embed_thumbnail"]:
            args += ["--embed-thumbnail"]
    else:
        if q == "best":
            args += ["-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"]
        elif q in ("1080", "720", "480"):
            args += ["-f", f"bestvideo[height<={q}][ext=mp4]+bestaudio[ext=m4a]/best[height<={q}]"]
        else:
            args += ["-f", "best"]

        args += ["--merge-output-format", fmt]

        if cfg["defaults"]["subtitles"]:
            args += ["--write-subs", "--embed-subs"]

    args.append(url)
    return args


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        console.print(Panel(
            "[bold]ytdl[/bold] [cyan]<url>[/cyan] [dim][[--audio] [--quality 1080|720|480|best]][/dim]\n\n"
            "  [cyan]--audio[/cyan]       Download audio only (mp3)\n"
            "  [cyan]--quality[/cyan]     Video quality: best (default), 1080, 720, 480\n\n"
            "Downloads go to [yellow]D:/media/Downloads[/yellow]",
            title="yt-dlp wrapper",
            border_style="blue"
        ))
        sys.exit(0)

    args = sys.argv[1:]
    audio_only = "--audio" in args
    quality = None

    if "--quality" in args:
        idx = args.index("--quality")
        quality = args[idx + 1]
        args = [a for i, a in enumerate(args) if i not in (idx, idx + 1)]

    url = next((a for a in args if a.startswith("http")), None)
    if not url:
        console.print("[red]Error:[/red] No URL provided.")
        sys.exit(1)

    cfg = load_config()
    cmd = build_args(url, cfg, quality, audio_only)

    mode = "audio (mp3)" if audio_only else f"video ({quality or cfg['defaults']['quality']})"
    console.print(f"[bold blue]↓[/bold blue] Downloading [cyan]{mode}[/cyan]")
    console.print(f"[dim]{url}[/dim]\n")

    result = subprocess.run(cmd)
    if result.returncode == 0:
        console.print(f"\n[bold green]✓[/bold green] Saved to [yellow]{cfg['paths']['download_dir']}[/yellow]")
    else:
        console.print("\n[bold red]✗[/bold red] Download failed.")
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
