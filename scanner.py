import requests
import time
from pybit.unified_trading import HTTP

BOT_TOKEN = "8735020732:AAH7Ue7Y6tbsOWJ3RrcNem0eCw4N7rRO0k8"
CHAT_ID = "835304619"

session = HTTP()
sent = set()

def send_message(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

print("🚀 Scanner Started")

while True:
    try:
        data = session.get_tickers(category="linear")

        for coin in data["result"]["list"]:

            symbol = coin["symbol"]
            change = float(coin["price24hPcnt"]) * 100

            if change >= 45:

                if symbol not in sent:

                    send_message(
                        f"🚀 {symbol}\n24H Change: {change:.2f}%"
                    )

                    sent.add(symbol)

        time.sleep(60)

    except Exception as e:
        print(e)
        time.sleep(30)
