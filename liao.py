# -*- coding: utf-8 -*-
import urllib
import json
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
if __name__ == '__main__':
    key = 'e239f9181f05460184f540b4f035328f'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    while True:
        info = raw_input('me:')
        request = api + info +'&loc=上海市'
        response = getHtml(request)
        dic_json = json.loads(response)
        print 'robot:'.decode('utf-8') + dic_json['text']
