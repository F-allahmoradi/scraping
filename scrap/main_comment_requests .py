import requests
import pandas as pd
import json


cookies = {
    'mid': 'ZrPACwALAAHOP9kcItU53i9pCkKP',
    'ig_did': '2629BC5E-48CF-4F5C-80D5-55A7DD90DFE0',
    'datr': 'EMCzZrWrVRVYtmGKPTt6b_dp',
    'igd_ls': '%7B%2217845863629661758%22%3A%7B%22c%22%3A%7B%221%22%3A%22HCwAABbaAhaGl9-TBBMFFvyY2aX9rbM_AA%22%2C%222%22%3A%22GRwVQBxMAAAWARa4gJ7rDBYAFriAnusMABYoAA%22%7D%2C%22d%22%3A%22a2d95052-859d-4ba9-9ea1-5e95952668af%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22hpzk95%22%7D%7D',
    'ps_l': '1',
    'ps_n': '1',
    'csrftoken': 'Ls2xqSOc80COGAFn0kFGE815pFwXeSLU',
    'ds_user_id': '49778853757',
    'sessionid': '49778853757%3AcNprjP19FBpSsX%3A14%3AAYce1f9KmnPjZIiglYtvorZY2eet8c8PNTmRB0HmCw',
    'shbid': '"1838\\05449778853757\\0541758793970:01f7ce0b23afd9f12ac28d29444a9298d2fef7b2ae36bf80b2b05227abcdcd802436c0b7"',
    'shbts': '"1727257970\\05449778853757\\0541758793970:01f73c6f270951ea88fcbf9b7ab7387dbde63a3367ee125ddd8c52ff31a5f871c5856ff3"',
    'wd': '819x564',
    'rur': '"RVA\\05449778853757\\0541758902585:01f7988a64150d2fbc8ef8ec2600d9bc38553401706d91e5d46bc035fa2cecc959db335f"',
}

headers = {
    'accept': '*/*',
    'accept-language': 'fa-IR,fa;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'mid=ZrPACwALAAHOP9kcItU53i9pCkKP; ig_did=2629BC5E-48CF-4F5C-80D5-55A7DD90DFE0; datr=EMCzZrWrVRVYtmGKPTt6b_dp; igd_ls=%7B%2217845863629661758%22%3A%7B%22c%22%3A%7B%221%22%3A%22HCwAABbaAhaGl9-TBBMFFvyY2aX9rbM_AA%22%2C%222%22%3A%22GRwVQBxMAAAWARa4gJ7rDBYAFriAnusMABYoAA%22%7D%2C%22d%22%3A%22a2d95052-859d-4ba9-9ea1-5e95952668af%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22hpzk95%22%7D%7D; ps_l=1; ps_n=1; csrftoken=Ls2xqSOc80COGAFn0kFGE815pFwXeSLU; ds_user_id=49778853757; sessionid=49778853757%3AcNprjP19FBpSsX%3A14%3AAYce1f9KmnPjZIiglYtvorZY2eet8c8PNTmRB0HmCw; shbid="1838\\05449778853757\\0541758793970:01f7ce0b23afd9f12ac28d29444a9298d2fef7b2ae36bf80b2b05227abcdcd802436c0b7"; shbts="1727257970\\05449778853757\\0541758793970:01f73c6f270951ea88fcbf9b7ab7387dbde63a3367ee125ddd8c52ff31a5f871c5856ff3"; wd=819x564; rur="RVA\\05449778853757\\0541758902585:01f7988a64150d2fbc8ef8ec2600d9bc38553401706d91e5d46bc035fa2cecc959db335f"',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/p/C_xBDhGNVZh/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="129.0.6668.70", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.70"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-bloks-version-id': '433151bb88b20e8ea00ec6776a5710adf95e47fc8933b346b315c48c7298703f',
    'x-csrftoken': 'Ls2xqSOc80COGAFn0kFGE815pFwXeSLU',
    'x-fb-friendly-name': 'PolarisPostCommentsPaginationQuery',
    'x-fb-lsd': 'qB8ESBSOa59m3ii31bDU04',
    'x-ig-app-id': '936619743392459',
}

data = {
    'av': '17841449852722356',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': '25',
    '__hs': '19992.HYP:instagram_web_pkg.2.1..0.1',
    'dpr': '1',
    '__ccg': 'UNKNOWN',
    '__rev': '1016826985',
    '__s': 'e0qts0:swfsoj:n0k5vu',
    '__hsi': '7418975302926625554',
    '__dyn': '7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO0FE2awgo9oO0n24oaEnxO1ywOwv89k2C1Fwc60D87u3ifK0EUjwGzEaE2iwNwmE2eUlwhEe87q7U881eFEbUGdG1QwTU9UaQ0Lo6-3u2WE5B08-269wr86C1mwPwUQp1yUb9UK6V8aUuwm9EO6UaU4W7U5SE',
    '__csr': 'gV1QwX2dWMF2l9iNRE-F7ORXl5BHqLHaBjG8X9Z9tBi_KV7AiVcClojHy94lrKqmogEDGaCqCpGKHUzgLJJcxozUF34cmm4aypUPzFozDDByamfJ269AxeCV9QqjGfKibG5Rzk4AUGdZ004W6hpQ3608vwaG1uwVBgtwWCU38BgC0Ooyp0vWhqwrz00E-x93U8Q2qve2mEgwIwxEgm1cGhQ1OgfUgyEyKm1uyRgcE2mg6ioEauqowgkaweHg5y1CgWE2Xg5G221zw9ksB22yk642qeg561ew34PGaBgjw0u-o0-O02gy',
    '__comet_req': '7',
    'fb_dtsg': 'NAcPqmDQAXNSRU2-L14iHYqsa_B_UmcuqB0NyBdsQXezVOBOALiK5zA:17858225011064242:1726167471',
    'jazoest': '26185',
    'lsd': 'qB8ESBSOa59m3ii31bDU04',
    '__spin_r': '1016826985',
    '__spin_b': 'trunk',
    '__spin_t': '1727364795',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisPostCommentsPaginationQuery',
    'variables': '{"after":"{\\"server_cursor\\": \\"QVFBM1FxdlVpYnZ3N244TzB0aENWSXo2Qnhsc1p3S2ludzMxYzBNa3h0UFYyLTZ3bnB0NTVtR3JDRDRUOFJjZUVhRGJ5SHlXRTBMc0JpX1ZxWk40MUR5NUpqV3lRSkxUMDN5dy1qbTlOLUZ1VlE=\\", \\"is_server_cursor_inverse\\": true}","before":null,"first":10,"last":null,"media_id":"3460746345717626248","sort_order":"popular","__relay_internal__pv__PolarisIsLoggedInrelayprovider":true}',
    'server_timestamps': 'true',
    'doc_id': '7823865067713647',
}




response = requests.post('https://www.instagram.com/graphql/query/', headers=headers, cookies=cookies, data=data)
comments_data = response.json()
has_next_page = comments_data['data']['xdt_api__v1__media__media_id__comments__connection']['page_info']['has_next_page']

comment_list = []
user_name=[]

while has_next_page:
    server_cursor = \
    json.loads(comments_data['data']['xdt_api__v1__media__media_id__comments__connection']['page_info']['end_cursor'])[
        'server_cursor']

    comments = comments_data['data']['xdt_api__v1__media__media_id__comments__connection']['edges']

    for comment in comments:
        comment_text = comment['node']['text']
        user_name_text = comment ['node']['user']['username']
        comment_list.append(comment_text)
        user_name.append(user_name_text)


    data['variables'] = (f'{{"after":"{{\\"server_cursor\\": \\"{server_cursor}\\", \\"is_server_cursor_inverse\\": true}}",'
                         f'"before":null,"first":10,"last":null,"media_id":"3460746345717626248","sort_order":"popular",'
                         f'"__relay_internal__pv__PolarisIsLoggedInrelayprovider":true}}')
    response = requests.post('https://www.instagram.com/graphql/query/', headers=headers, cookies=cookies, data=data)

    if response.status_code == 200:
        comments_data = response.json()
        has_next_page = comments_data['data']['xdt_api__v1__media__media_id__comments__connection']['page_info'][
            'has_next_page']

    else:
        print(f"error : {response.status_code}")





pruduct5 = {'names': user_name, 'commeents': comment_list}
data = pd.DataFrame.from_dict(pruduct5, orient='index')
data = data.transpose()
writer = pd.ExcelWriter('comment2.xlsx')
data.to_excel(writer)
writer.close()

