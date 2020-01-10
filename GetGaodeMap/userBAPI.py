# -*- coding: utf-8 -*-
"""
Created on Thu May 17 14:22:23 2018
百度地图api
a1  坐标格式为：lat<纬度>,lng<经度>|lat<纬度>,lng<经度>
a4  坐标类型，可选参数，默认为bd09ll。允许的值为：bd09ll（百度经纬度坐标）、
bd09mc（百度摩卡托坐标）、gcj02（国测局加密坐标）、wgs84（gps设备获取的坐标
a5  只对驾车算路(driving)生效。  该服务为满足性能需求，不含道路阻断信息干预。
可选值：
    10： 不走高速；
    11：常规路线，即多数人常走的一条路线，不受路况影响；
    12： 距离较短（考虑路况）：即距离相对较短的一条路线，
        但并不一定是一条优质路线。计算耗时时，考虑路况对耗时的影响；
    13： 距离较短（不考虑路况）：路线同以上，但计算耗时时，
        不考虑路况对耗时的影响，可理解为在路况完全通畅时预计耗时。 
        注：除13外，其他tactics 的耗时计算都考虑实时路况
"""
import json
from urllib.request import urlopen
import urllib
import sys
s1="42.909089"
s2="116.382668"
t1="31.194255"
t2="121.334198"
a1=r"http://api.map.baidu.com/routematrix/v2/driving?output=json"
a2=r"&origins="+s1+","+s2
a3=r"&destinations="+t1+","+t2
a4=r"&coord_type=wgs84"
a5=r"&tactics=11"
a6=r"&ak=RyoNrajzbXPcVQKAeCTcL7E2k3RnrEAX"
#a6为从百度地图网站申请的api
url=a1+a2+a3+a4+a5+a6
 
#下面四行为url有汉字时的解决办法
#name=u"北京西站"
#s=urllib.parse.quote(name)
#a=u"http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=2AGHayMtz8F9zlDimvRo1TCPbAKmzDfm"%(s)
 
b = urlopen(url)
c=b.read() 
result = json.loads(c)
 
sys.stdout = open('recodexml.log', mode = 'w',encoding='utf-8')
print (result)

#结果示例，距离以米为单位，时间以秒为单位，除以3600为小时。message为是否成功。
#{'status': 0, 'result': 
#[{'distance': {'text': '1723.8公里', 'value': 1723771},
# 'duration': {'text': '19.5小时', 'value': 70279}}],
# 'message': '成功'}
 
# print(c["status"])
# print(c["result"][0]["distance"]["value"]/1000)
# print(c["result"][0]["duration"]["value"]/60)