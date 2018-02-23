from aip import AipSpeech

APP_ID = '10818524'
API_KEY = 'itP1il3o3QFXLQCMSgPcZl2R'
SECRET_KEY = '60d3ed5232a252e9f5ff06d893ee2780'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

result=client.asr(get_file_content('sh.wav'), 'wav', 16000, {
    'lan': 'zh',
})		

print(result['result'][0])
