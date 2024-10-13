# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25672330"))
API_HASH = getenv("API_HASH", "fbfcabdb2f7f55fe64c4e662a40618e9")
BOT_TOKEN = getenv("BOT_TOKEN", "7474212080:AAF9Qe5DHekRl2aA5plSq3zaFqj2MUX2vpM")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6745609407").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Krishopkyt:Krishopkyt@opkrish.jw1hi.mongodb.net/?retryWrites=true&w=majority&appName=Opkrish")
LOG_GROUP = getenv("LOG_GROUP", "-1002312252849")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001960284878"))
