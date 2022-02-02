import requests
import time
import sys
import urllib.parse
import tqdm

def delete(cookie, briefList):
    http_headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Cookie': '%s' % cookie
    }
    count = 1
    msg = input('将要删除动态，确定吗？(y/n)')
    if msg == 'y':
        for i in tqdm.tqdm(briefList):
            data = {'item_brief': i}
            data = urllib.parse.urlencode(data)
            mainUrl = 'https://api.zhihu.com/moments/activity?%s' % data
            re = requests.delete(url=mainUrl, headers=http_headers, verify=False)
            time.sleep(0.2)
            count = count + 1
         #   msg = "正在删除第%s条" % str(count)
         #   sys.stdout.write(str(msg) + '\r')
        print("删除完毕")
    else:
        print("取消删除动态")
        sys.exit()
