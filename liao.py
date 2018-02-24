# -*- coding: utf-8 -*-
import urllib
import json
import os


from aip import AipSpeech

APP_ID = '10818524'
API_KEY = 'itP1il3o3QFXLQCMSgPcZl2R'
SECRET_KEY = '60d3ed5232a252e9f5ff06d893ee2780'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
if __name__ == '__main__':
    key = 'e239f9181f05460184f540b4f035328f'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    while True:
        #info = raw_input('me:')
        os.system('arecord -t wav -f S16_LE -d 5 -r 16000 -D "hw:0,2" sh.wav')
        result=client.asr(get_file_content('sh.wav'), 'wav', 16000, { 'lan': 'zh', })		
        info=(result['result'][0])
        print(info)
        info=info.encode('utf-8')
        if len(info) == 0:
            continue
        request = api + info
        response = getHtml(request)
        dic_json = json.loads(response)
        print 'robot:'.decode('utf-8') + dic_json['text']
