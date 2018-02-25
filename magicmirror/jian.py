import urllib, urllib.request, sys
import ssl

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=itP1il3o3QFXLQCMSgPcZl2R&client_secret=60d3ed5232a252e9f5ff06d893ee2780&'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content)
#https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=itP1il3o3QFXLQCMSgPcZl2R&client_secret= 60d3ed5232a252e9f5ff06d893ee278&
