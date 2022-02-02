import requests
import json
import urllib3
import time
import writeFile
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http_headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
}

briefList = []
def getActivityInfo(username):
    first_url = 'https://api.zhihu.com/moments/%s/activities?action_feed=true&limit=10&reverse_order=0' % str(username)
    re = requests.get(url=first_url, verify=False, headers=http_headers)
    first_result = json.loads(re.text)['data']
    for i in first_result:
        try:
            briefList.append(i['brief'])
            if i['source']['action_type'] == 'MEMBER_VOTE_ANSWER':
                question = i['target']['question']['title']
                answer = i['target']['excerpt']
                answer_link = i['target']['url']
                action_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['source']['action_time']))
                msg = "正在收集，时间为：%s" % str(action_time)
                sys.stdout.write(str(msg) + '\r')
                writeFile.write(username, '点赞回答', question, answer, answer_link, action_time)
            elif i['source']['action_type'] == 'MEMBER_CREATE_ANSWER':
                question = i['target']['question']['title']
                answer = i['target']['excerpt']
                answer_link = i['target']['url']
                action_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['source']['action_time']))
                msg = "正在收集，时间为：%s" % str(action_time)
                sys.stdout.write(str(msg) + '\r')
                writeFile.write(username, '发表回答', question, answer, answer_link, action_time)
            elif i['source']['action_type'] == 'MEMBER_CREATE_PIN':
                question = i['target']['content'][0]['content']
                answer_link = i['target']['url']
                action_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['source']['action_time']))
                msg = "正在收集，时间为：%s" % str(action_time)
                sys.stdout.write(str(msg) + '\r')
                writeFile.write(filename=username, type='发表想法', question=question, answer='', link=answer_link, time=action_time)
            elif i['source']['action_type'] == 'MEMBER_CREATE_ARTICLE':
                question = i['target']['title']
                answer_link = i['target']['url']
                action_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['source']['action_time']))
                msg = "正在收集，时间为：%s" % str(action_time)
                sys.stdout.write(str(msg) + '\r')
                writeFile.write(filename=username, type='发表文章', question=question, answer='', link=answer_link, time=action_time)
            elif i['source']['action_type'] == 'MEMBER_VOTE_ARTICLE':
                question = i['target']['title']
                answer_link = i['target']['url']
                action_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['source']['action_time']))
                msg = "正在收集，时间为：%s" % str(action_time)
                sys.stdout.write(str(msg) + '\r')
                writeFile.write(filename=username, type='点赞文章', question=question, answer='', link=answer_link,
                                time=action_time)
            else:
                pass
        except Exception:
            pass
    return [first_result[-1]['id'], username]


def getWholeInfo(id, username):
    mainUrl = 'https://api.zhihu.com/moments/%s/activities?offset=%d' % (str(username), int(id))
    re = requests.get(url=mainUrl, verify=False, headers=http_headers)
    result = json.loads(re.text)['data']
    for i in result:
        try:
            briefList.append(i['brief'])
        except Exception:
            pass
        try:
            if i['source']['action_type'] == 'MEMBER_VOTE_ANSWER':
                question = i['target']['question']['title']
                answer = i['target']['excerpt']
                answer_link = i['target']['url']
                action_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['source']['action_time']))
                msg = "正在收集，时间为：%s" % str(action_time)
                sys.stdout.write(str(msg) + '\r')
                writeFile.write(username, '点赞回答', question, answer, answer_link, action_time)
            elif i['source']['action_type'] == 'MEMBER_CREATE_ANSWER':
                question = i['target']['question']['title']
                answer = i['target']['excerpt']
                answer_link = i['target']['url']
                action_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['source']['action_time']))
                msg = "正在收集，时间为：%s" % str(action_time)
                sys.stdout.write(str(msg) + '\r')
                writeFile.write(username, '发表回答', question, answer, answer_link, action_time)
            elif i['source']['action_type'] == 'MEMBER_CREATE_PIN':
                question = i['target']['content'][0]['content']
                answer_link = i['target']['url']
                action_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['source']['action_time']))
                msg = "正在收集，时间为：%s" % str(action_time)
                sys.stdout.write(str(msg) + '\r')
                writeFile.write(filename=username, type='发表想法', question=question, answer='', link=answer_link, time=action_time)
            elif i['source']['action_type'] == 'MEMBER_CREATE_ARTICLE':
                question = i['target']['title']
                answer_link = i['target']['url']
                action_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['source']['action_time']))
                msg = "正在收集，时间为：%s" % str(action_time)
                sys.stdout.write(str(msg) + '\r')
                writeFile.write(filename=username, type='发表文章', question=question, answer='', link=answer_link, time=action_time)
            elif i['source']['action_type'] == 'MEMBER_VOTE_ARTICLE':
                question = i['target']['title']
                answer_link = i['target']['url']
                action_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['source']['action_time']))
                msg = "正在收集，时间为：%s" % str(action_time)
                sys.stdout.write(str(msg) + '\r')
                writeFile.write(filename=username, type='点赞文章', question=question, answer='', link=answer_link,
                                time=action_time)
            else:
                pass
        except Exception:
            pass
    time.sleep(0.1)

    try:
        getWholeInfo(result[-1]['id'], username)
    except Exception:
        print('收集完毕')


def collect(username):
    getWholeInfo(getActivityInfo(username)[0], username)
    return briefList
