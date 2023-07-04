import requests, sys
from win10toast import ToastNotifier

act_id = str(sys.argv[1])
_MHYUUID = str(sys.argv[2])
ltoken  = str(sys.argv[3])
ltuid  = str(sys.argv[4])

def fetch_data():
    url = "https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=en-us"
    headers = {
        'Host': 'sg-hk4e-api.hoyolab.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://act.hoyolab.com/',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://act.hoyolab.com',
        'Cookie': '_MHYUUID=' + _MHYUUID + '; ltoken=' + ltoken + '; ltuid='  + ltuid +';',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'TE': 'trailers',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    payload = {'act_id': act_id}

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        print(data)
        toast = ToastNotifier()

        if data["retcode"] == -5003: # Already checked in
            toast.show_toast(
                "Genshin Check-In",
                data["message"],
                duration=5,
                icon_path="checkin.ico",
                threaded=False,
            )
        if data["retcode"] == 0:
            if data["data"]["gt_result"]["risk_code"] == 5001:
                toast.show_toast(
                    "Genshin Check-In",
                    "Failed (Probably because of missing Captcha)",
                    duration=5,
                    icon_path="checkin.ico",
                    threaded=False,
                )
            elif data["data"]["gt_result"]["risk_code"] == 0:
                toast.show_toast(
                    "Genshin Check-In",
                    "Success <3",
                    duration=5,
                    icon_path="checkin.ico",
                    threaded=False,
                )
            else:
                toast.show_toast(
                    "Genshin Check-In",
                    "Something went wrong... risk_code=" + str(data["data"]["gt_result"]["risk_code"]),
                    duration=5,
                    icon_path="checkin.ico",
                    threaded=False,
                )
        else: # Something went wrong
            toast.show_toast(
                "Genshin Check-In",
                "Received invalid response from HoYoLAB API",
                duration=5,
                icon_path="checkin.ico",
                threaded=False,
            )
    except requests.exceptions.RequestException as error:
        print("Error occurred:", error)

fetch_data()