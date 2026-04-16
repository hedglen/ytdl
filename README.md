# ytdl

yt-dlp wrapper with presets. Downloads go straight to `D:/media/Downloads`.

## Usage

```powershell
ytdl <url>                        # best quality video (mp4)
ytdl <url> --quality 1080         # cap at 1080p
ytdl <url> --audio                # audio only (mp3)
dl <url>                          # alias for ytdl
dll                               # list all supported extractors
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

## Supported Sites

### Video / Streaming

| Site | Extractor | Notes |
|------|-----------|-------|
| YouTube | `youtube`, `youtube:playlist`, `youtube:tab`, `youtube:clip` | Videos, playlists, Shorts, clips |
| Twitch | `twitch:vod`, `twitch:clips`, `twitch:collection` | VODs, highlight clips, collections |
| Vimeo | `vimeo`, `vimeo:album`, `vimeo:channel` | Indie/pro video hosting |
| Reddit | `reddit` | Video posts download cleanly |
| Twitter/X | `twitter`, `twitter:spaces` | Tweets with video, Spaces recordings |
| Bluesky | `Bluesky` | Video posts |
| Instagram | `instagram`, `instagram:story` | Reels, posts, stories |
| TikTok | `TikTok`, `tiktok:user` | Videos, user feeds |
| Kick | `kick:vod`, `kick:clips` | Streaming platform VODs and clips |
| Rumble | `Rumble`, `RumbleChannel` | Videos and channel feeds |

### Music

| Site | Extractor | Notes |
|------|-----------|-------|
| SoundCloud | `soundcloud`, `soundcloud:playlist`, `soundcloud:user` | Tracks, playlists, full profiles |
| Bandcamp | `Bandcamp`, `Bandcamp:album`, `Bandcamp:user` | Albums, tracks, artist pages |
| Audiomack | `audiomack`, `audiomack:album` | Hip-hop/R&B focused, free streaming |
| Last.fm | `LastFM`, `LastFMPlaylist` | Links out to actual audio tracks |
| Audius | `Audius`, `audius:playlist`, `audius:track` | Decentralized music platform |
| Mixcloud | `mixcloud`, `mixcloud:playlist` | DJ sets, mixes, radio shows |

### Tech / Learning

| Site | Extractor | Notes |
|------|-----------|-------|
| Udemy | `udemy`, `udemy:course` | Paid course videos (requires login) |
| Pluralsight | `pluralsight`, `pluralsight:course` | Dev/IT training |
| Frontend Masters | `FrontendMasters`, `FrontendMastersCourse` | Frontend-focused courses |
| Khan Academy | `khanacademy`, `khanacademy:unit` | Free educational content |
| Nebula | `nebula:video`, `nebula:channel`, `nebula:season` | Creator-owned streaming platform |
| LinkedIn Learning | `linkedin:learning`, `linkedin:learning:course` | Professional dev courses |

### Gaming / Clips

| Site | Extractor | Notes |
|------|-----------|-------|
| Xbox Clips | `XboxClips` | Clips from Xbox network |
| Steam | `SteamCommunity` | Community video posts |
| Medal.tv | `MedalTV` | Gaming clip highlights |

### Podcasts / Long-form Audio

| Site | Extractor | Notes |
|------|-----------|-------|
| Apple Podcasts | `ApplePodcasts` | Public episodes |
| Libsyn | `Libsyn` | Common podcast host |
| Simplecast | `simplecast`, `simplecast:episode` | Another common podcast host |
| Spreaker | `Spreaker`, `SpreakerShow` | Podcast platform |

### Utility / File Sharing

| Site | Extractor | Notes |
|------|-----------|-------|
| Dropbox | `Dropbox` | Shared video file links |
| Google Drive | `GoogleDrive`, `GoogleDrive:Folder` | Shared video links |
| Loom | `loom` | Screen recordings |
| Streamable | `Streamable` | Short video clip hosting |

## Other Sites As Well - Try it out

