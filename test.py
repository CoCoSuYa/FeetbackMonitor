import requests


def make_request():
    url = "https://txc.qq.com/api/v2/165920/dashboard/posts/list"

    params = {
        "page": 1,
        "count": 2,
        "from": "2023-08-22 15:46:54",
        "to": "2023-08-23 15:46:54",
        "status": 0,
        "order": 1,
        "label": "all"
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "_horizon_uid=4b8af6d6-a18e-444e-9ec1-f80d7e8790be; tvfe_boss_uuid=97d889f8b14236f5; pgv_pvid=3245525164; pac_uid=0_cdec3ae1df1ac; iip=0; RK=hfN0dHTQnY; ptcz=5822d84a0f75a967b3adbff3bbbea5c065e1e611f1ac6eb308181cc1603e8d71; eas_sid=u10647S5C4J1o4V7v0F6F974R9; LW_sid=R1U6n725p4g155O0j9X226d1P2; LW_uid=x1W617R5b4g1K5Y0N9N2E6g1Y3; __wj_userid=4b8af6d6-a18e-444e-9ec1-f80d7e8790be; _tucao_session=VE9zaHVkSmdLYXFRZzJwRjg3dTE5VEFkQXR2UWJUV0s1K0JVK1BGM3hBUkZSYXByOXFkTFlEZ3J2bFJFTWUyOGVQMW9scGRYNTBVSDIrR09uV1ZOQ2Vrc2ZST2IyM3dzMlp4aWZjZFo4eFhibTJSSHlpVmN6QVNvM00rS3BlaTBYYTNsNXNqU0JHRFFiYTlZS2xUeFF3PT0%3D--TY27GkbJj0M%2BnFU6gmOstA%3D%3D; _tucao_custom_info=Qi81UlVUbEpROVh4enAxNWR4b2xDTVMwZkxGVGlkK2ZiSnRjd0M4YVdOL0RKVVYyNjB0RmVxYWRaMUtQbDJyYQ%3D%3D--hAPWF9K4bQJ5oj7xNtgR%2BQ%3D%3D; _horizon_sid=fea9a94c-2562-4b70-ac42-72dc4f96746f",  # 长cookie信息
        "Host": "txc.qq.com",
        "Referer": "https://txc.qq.com/dashboard/all-posts",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",  # 省略部分信息
        "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS"
    }

    response = requests.get(url, params=params, headers=headers)

    # 输出返回信息
    if response.status_code == 200:
        print(response.json())  # 如果返回的是JSON格式
    else:
        print("Error:", response.status_code, response.text)


# 调用函数
make_request()
