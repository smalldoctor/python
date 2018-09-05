# -*- coding: utf-8

import time
import urllib.request as request
import urllib.parse as parse
import hashlib
import json

ak = 'jdjzlyY5xQKatd96GamdvvDjFC7t1Ou6'
sk = 'UrDlXuVmsZNY0MLbuNxtg53PovaCCZzt'
# 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
queryStr = '/geocoder/v2/?output=json&ak=' + ak + '&address='
# 计算SN时不包含如下信息
targetHttp = 'http://api.map.baidu.com'

PLACES = (
    '南京市栖霞区林景瑞园', '南京市雨花台区大数据产业基地', '广州市天河区中国移动南方基地',
    '广州市天河区万科云城米酷',
    '南京市栖霞区金鹰湖滨天地', '南京市浦口区南京工业大学', '南京市栖霞区晓庄广场',
    '南京市栖霞区常发广场',
    '南京市建邺区中央商场',
    '南京市鼓楼区鼓楼医院',
)


def fetch_place(place):
    newQueryStr = queryStr + place
    # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = parse.quote(newQueryStr, safe="/:=&?#+!$,;'@()*[]")
    rawStr = encodedStr + sk
    md5Info = hashlib.md5(parse.quote_plus(rawStr).encode("utf8")).hexdigest()
    newQueryStr = encodedStr + "&sn=" + md5Info
    # 如果url中含有中文需要进行编码,encode
    response = request.urlopen(targetHttp + newQueryStr)
    result = response.read().decode("utf-8")
    # 字符串转JSON
    result = json.loads(result)
    print("{},{}, {:6.2f}, {:6.2f}".format(place, result['result']['level'],
                                           result['result']['location']['lat'],
                                           result['result']['location']['lng'],
                                           ))


def main():
    for place in PLACES:
        fetch_place(place)


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started

    print()
    print("time elapsed: {:.2f}s".format(elapsed))
