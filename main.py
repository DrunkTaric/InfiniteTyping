import requests
from time import sleep
from dotenv import dotenv_values

config = dotenv_values(".env")
channel = config["CHANNEL_ID"]
token = config["TOKEN"]

while True:
	response = requests.request("POST", f"https://discord.com/api/v9/channels/{channel}/typing", headers = {
        'authorization': token
    })
	sleep(3)