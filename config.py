import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "28276831"))
API_HASH = getenv("API_HASH", "e1d302d72df431cd419bb2267e2200b8")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6869756562:AAFVzgPQEhop6aUg32XpWYWiOoYMZ07JYeI")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hilecomnet:xX5cT007jTsDFaqJ@cluster0.n8ivy3k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 500))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002241454536))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6737592159"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/t3rickg/mangomangomango", # dont Change this otherwise u get error 🧧
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/learningbots79")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/learning_bots")

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
STRING1 = getenv("STRING_SESSION", "BAGveF8AEEMFwvFdVSPxF7fe9XBl0XGH07yQrua0L4jy-l8Yl44dRIV-FRk_v9Yvfye9nR_P2kFCug9B_3d5ybv8iggDRU68YZxipbdrU4OmaKza10WncRZL7GmOje-362xceTXQaZE9k8nWlQ4UhevUG9WV96pb2ohnB88khVgAvuc_qqVYb9j2Pkd_S8cn5XvKy2n8cC1WyTM1aBThocumnIIV6O2vYbLNs3j7DRLAPC2I6FsgCDcnEKovMZ8OaoLm3d_RKfr88sknLCy0GA3XG-SC-TzzOInRNNFyL9U9d_9MamyDOtw2y0zmbU85qRtYqlnpRYyICRfiJrLdWotqDSc-VwAAAAGzTENpAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
STATS_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
STREAM_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
