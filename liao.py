# -*- coding: utf-8 -*-
import urllib
import json
import os
import sys


from aip import AipSpeech

APP_ID = '10818524'
API_KEY = 'itP1il3o3QFXLQCMSgPcZl2R'
SECRET_KEY = '60d3ed5232a252e9f5ff06d893ee2780'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



def text2voice(text):
    url = 'http://tts.baidu.com/text2audio?idx=1&tex={0}&cuid=baidu_speech_' \
          'demo&cod=2&lan=zh&ctp=1&pdt=1&spd=3&per=0&vol=5&pit=5'.format(text)
    os.system('mplayer "%s"' % url)

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

if __name__ == '__main__':
    key = 'e239f9181f05460184f540b4f035328f'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    reload(sys)
    sys.setdefaultencoding('utf-8')
    while True:
        #info = raw_input('me:')
        os.system('arecord -t wav -f S16_LE -d 5 -r 16000 -D "plughw:1,0" sh.wav');
        result=client.asr(get_file_content('sh.wav'), 'wav', 16000, { 'lan': 'zh', })		
        if result['err_no'] != 0:
            continue
        print(result)
#        info = result['result'][0]
#        info=info.encode('utf-8')
#        print(info)
#        if len(info) == 0:
#            continue
#        request = api + info
#        response = getHtml(request)
#        dic_json = json.loads(response)
#        print 'robot:'.decode('utf-8') + dic_json['text']
#        text2voice(dic_json['text'])
