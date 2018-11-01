#!/usr/bin/python
#-*-coding:utf-8 -*-

import itchat, time
import requests

tuling_key = '1107d5601866433dba9599fac1bc0083'

def get_response(send_msg):
    apiurl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : tuling_key,
        'info'   : send_msg,
        'userid' : 'my_robot'
    }
    try:
        r = requests.post(apiurl, data=data).json()
        return r.get('text')
    except:
        return

#自动回复相同内容
@itchat.msg_register(itchat.content.TEXT)
def ruling_reply(msg):
    chat_content = msg['Text']
    defaultReply = 'I got:' + chat_content
    reply = get_response(chat_content)
    return reply or defaultReply  #reply为空时返回默认值

#登录
itchat.auto_login(hotReload=True)
#一直运行
itchat.run()
#发送信息
#itchat.send(u'测试消息发送', 'filehelper')



