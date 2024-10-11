# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25254897"))
API_HASH = getenv("API_HASH", "85be8d682c5605fbde55c94c34f610be")
BOT_TOKEN = getenv("BOT_TOKEN", "7533648739:AAFFckab5s7Q-V6hZHzSmgVlARm5sRTG0GE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6745609407").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://debojitbbb0:NgiJdMgZ1VilczTq@cluster0.xpvhh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002312252849")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001960284878"))
