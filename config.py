import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("27412728"))
API_HASH = getenv("0ef7db3bf8f66b685cbdbfd82829ae0b")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7156914807:AAFkY__BrdWsUfHTxxKOeH3AqNo5QpqnCmA")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://Adarsh98:Adarsh@cluster0.rjnamra.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("180", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002103631960", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7047834233"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("musicpro1")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("ee0820ee-5cdf-4d23-aeb5-f26ba44a9ed4")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/indian_best_english_chatting")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/indian_best_english_chatting")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQGiSPgAmlC1XHilDsbVvipe2Yq5cz7KHqeXi6Idl487QGVdBQdp9uCIV9cleiiajuAtQ3Lv6SzuGkCstr5fnvnJXTxhOr9G0jBP8vHEBRYD79Pe8RSKjez8J4gu4Xla2tH7BnhxHKtJhREWl8o99AcuzI-TmL9VuqaWjtZj8gXK7gzLyLUxpfY_0hMzRiA3g8FfDrSUrr5PRbQHpBYHyfnWIYFcrBQ7JgZPlfAJHt4W_AkyeiDJ4d2mgMj0EGY3Vb1Io9N24omQkk1AyYjJtDGzWxQRnRIz4ROAh3PZr0t0GwDXF3GiJEpbxIDX0BeP47M1XZgx-1Hv1XTBjndJu_uTmCPd6gAAAAGkFWp5AA", None)
STRING2 = getenv("BQGiSPgAmlC1XHilDsbVvipe2Yq5cz7KHqeXi6Idl487QGVdBQdp9uCIV9cleiiajuAtQ3Lv6SzuGkCstr5fnvnJXTxhOr9G0jBP8vHEBRYD79Pe8RSKjez8J4gu4Xla2tH7BnhxHKtJhREWl8o99AcuzI-TmL9VuqaWjtZj8gXK7gzLyLUxpfY_0hMzRiA3g8FfDrSUrr5PRbQHpBYHyfnWIYFcrBQ7JgZPlfAJHt4W_AkyeiDJ4d2mgMj0EGY3Vb1Io9N24omQkk1AyYjJtDGzWxQRnRIz4ROAh3PZr0t0GwDXF3GiJEpbxIDX0BeP47M1XZgx-1Hv1XTBjndJu_uTmCPd6gAAAAGkFWp5AA", None)
STRING3 = getenv("BQGiSPgAmlC1XHilDsbVvipe2Yq5cz7KHqeXi6Idl487QGVdBQdp9uCIV9cleiiajuAtQ3Lv6SzuGkCstr5fnvnJXTxhOr9G0jBP8vHEBRYD79Pe8RSKjez8J4gu4Xla2tH7BnhxHKtJhREWl8o99AcuzI-TmL9VuqaWjtZj8gXK7gzLyLUxpfY_0hMzRiA3g8FfDrSUrr5PRbQHpBYHyfnWIYFcrBQ7JgZPlfAJHt4W_AkyeiDJ4d2mgMj0EGY3Vb1Io9N24omQkk1AyYjJtDGzWxQRnRIz4ROAh3PZr0t0GwDXF3GiJEpbxIDX0BeP47M1XZgx-1Hv1XTBjndJu_uTmCPd6gAAAAGkFWp5AA", None)
STRING4 = getenv("BQGiSPgAmlC1XHilDsbVvipe2Yq5cz7KHqeXi6Idl487QGVdBQdp9uCIV9cleiiajuAtQ3Lv6SzuGkCstr5fnvnJXTxhOr9G0jBP8vHEBRYD79Pe8RSKjez8J4gu4Xla2tH7BnhxHKtJhREWl8o99AcuzI-TmL9VuqaWjtZj8gXK7gzLyLUxpfY_0hMzRiA3g8FfDrSUrr5PRbQHpBYHyfnWIYFcrBQ7JgZPlfAJHt4W_AkyeiDJ4d2mgMj0EGY3Vb1Io9N24omQkk1AyYjJtDGzWxQRnRIz4ROAh3PZr0t0GwDXF3GiJEpbxIDX0BeP47M1XZgx-1Hv1XTBjndJu_uTmCPd6gAAAAGkFWp5AA", None)
STRING5 = getenv("BQGiSPgAmlC1XHilDsbVvipe2Yq5cz7KHqeXi6Idl487QGVdBQdp9uCIV9cleiiajuAtQ3Lv6SzuGkCstr5fnvnJXTxhOr9G0jBP8vHEBRYD79Pe8RSKjez8J4gu4Xla2tH7BnhxHKtJhREWl8o99AcuzI-TmL9VuqaWjtZj8gXK7gzLyLUxpfY_0hMzRiA3g8FfDrSUrr5PRbQHpBYHyfnWIYFcrBQ7JgZPlfAJHt4W_AkyeiDJ4d2mgMj0EGY3Vb1Io9N24omQkk1AyYjJtDGzWxQRnRIz4ROAh3PZr0t0GwDXF3GiJEpbxIDX0BeP47M1XZgx-1Hv1XTBjndJu_uTmCPd6gAAAAGkFWp5AA", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/4b6c180e566d4ae40207c.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/4b6c180e566d4ae40207c.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/4b6c180e566d4ae40207c.jpg"
STATS_IMG_URL = "https://graph.org/file/4b6c180e566d4ae40207c.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/6db32c63c677905cc5cc3.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/6db32c63c677905cc5cc3.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:https://t.me/indian_best_english_chatting
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):https://t.me/indian_best_english_chatting
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:https://t.me/indian_best_english_chatting
    if not re.match("(?:http|https)://", SUPPORT_CHAT):https://t.me/indian_best_english_chatting
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
