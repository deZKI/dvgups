import requests
import bs4
import lxml

import requests

cookies = {
    '284d116cec806918b414484c9507d383': 'e2dijndm69fe2mpdrdm9liks13',
    'SL_G_WPT_TO': 'ru',
    'SL_GWPT_Show_Hide_tmp': '1',
    'SL_wptGlobTipTmp': '1',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '284d116cec806918b414484c9507d383=e2dijndm69fe2mpdrdm9liks13; SL_G_WPT_TO=ru; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1',
    'Origin': 'https://www.dvgups.ru',
    'Referer': 'https://www.dvgups.ru/index.php?Itemid=1247&option=com_timetable&view=newtimetable',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

params = {
    'Itemid': '1247',
    'option': 'com_timetable',
    'view': 'newtimetable',
}

data = {
    'GroupID': '52129',
}

response = requests.post('https://www.dvgups.ru/index.php', params=params, cookies=cookies, headers=headers, data=data)

file = open('1.html', 'w')
file.write(response.text)