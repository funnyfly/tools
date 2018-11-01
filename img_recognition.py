#!/user/bin/python
#-*-coding: utf-8-*-
import base64
import datetime
import random
import urllib
import urllib2
import json

def ac_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=qGiZaGrHwA0EzYjVuRSYLLZv&client_secret=TIztLWGnvzBy5FpUGS7cfTHH6ThbG1IC'
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    content = json.loads(content)
    return content['access_token']
    '''
    response = {
      "refresh_token": "25.b55fe1d287227ca97aab219bb249b8ab.315360000.1798284651.282335-8574074",
      "expires_in": 2592000,
      "scope": "public wise_adapt",
      "session_key": "9mzdDZXu3dENdFZQurfg0Vz8slgSgvvOAUebNFzyzcpQ5EnbxbF+hfG9DQkpUVQdh4p6HbQcAiz5RmuBAja1JJGgIdJI",
      "access_token": "24.6c5e1ff107f0e8bcef8c46d3424a0e78.2592000.1485516651.282335-8574074",
      "session_secret": "dfac94a3489fe9fca7c3221cbf7525ff"
    }
    '''

def bd_pic():
    '''
    
    '''
    #通用图像分析  该请求用于通用物体及场景识别，即对于输入的一张图片（可正常解码，且长宽比适宜），输出图片中的多个物体及场景标签。
    # request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
    #通用图像分析——图像主体检测  用户向服务请求检测图像中的主体位置。
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect"
    # 二进制方式打开图片文件
    f = open('zj.jpg', 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img, "with_face": 1}
    params = urllib.urlencode(params)

    access_token = ac_token()
    request_url = request_url + "?access_token=" + access_token
    request = urllib2.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(request)
    content = response.read()
    # content = json.loads(content)
    if content:
        print content.decode('utf-8')
bd_pic()
