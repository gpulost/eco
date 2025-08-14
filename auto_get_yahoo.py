import time
import requests

def get_sdi():
    now = int(time.time())
    sdi_url = f"https://query1.finance.yahoo.com/v8/finance/chart/SDI=F?events=capitalGain%7Cdiv%7Csplit&formatted=true&includeAdjustedClose=true&interval=1d&period1=1597371362&period2={now}&symbol=SDI%3DF&userYfid=true&lang=zh-Hant-HK&region=HK"

    headers = {
        "origin": "https://hk.finance.yahoo.com",
        "priority": "u=1, i",
        "referer": f"https://hk.finance.yahoo.com/quote/SDI%3DF/history/?period1=1597371362&period2={now}",
        "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }

    response = requests.get(sdi_url, headers=headers)
    print(response)
    if response.status_code == 200:
        data = response.json()
        open("sdi-latest.json", "w").write(json.dumps(data))
    else:
        print(f"Failed to get data: {response.text}")

if __name__ == "__main__":
    get_sdi()