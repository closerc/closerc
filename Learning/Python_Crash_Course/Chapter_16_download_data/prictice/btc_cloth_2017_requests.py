import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)

# 将数据写入文件
with open(r'Chapter_16_test_file\btc_close_2017_requests.json', 'w') as f:
    f.write(req.text)
file_requests = req.json()
