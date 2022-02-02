# -*- coding: utf-8 -*
import getopt
import sys
import getActivityInfo
import deleteContent
import os


def help():
    print("""
    -h --help                   帮助文档
    -u --username               用户名
    -c --cookie                 你的Cookie
    -d --delete                 是否选择删除动态（删除动态必须保证Cookie有效）
eg：
    python3 zhihuCollector.py -u 刘看山
    python3 zhihuCollector.py -u 刘看山 -c 'KLBRSID=d726|1643774487|1643773005; _xsrf=dr14GTt7c...' -d True
    """)
    sys.exit()


def main():
    isDelete = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:d:c:", ["username=", "delete=", "cookie="])
        for opt, arg in opts:
            if opt == '-h':
                help()
            elif opt in ("-u", "--username"):
                username = arg
            elif opt in ("-d", "--delete"):
                isDelete = arg
            elif opt in ("-c", "--cookie"):
                cookie = arg
        if os.path.exists('%s.csv' % str(username)):
            os.remove('%s.csv' % str(username))
        if not isDelete:
            getActivityInfo.collect(username)
        else:
            deleteContent.delete(cookie, getActivityInfo.collect(username))
    except Exception as e:
        print(e)
        help()


if __name__ == '__main__':
    main()
