import requests

TOKEN = 8863661925:AAHtb7vszU-XT1BFeQGchaeaGazSyG-HLkc
CHAT_ID = 459241285

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

res = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "TEST MESSAGE"
})

print(res.text)