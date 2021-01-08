from aip import AipSpeech
import os

APP_ID = '11711274'
API_KEY = 'iL6rNZgPjplCGYQfw86zO2ro'
SECRET_KEY = '0YNfOLiAPUgqCL4XxYVoO2oLV37pmByY'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('你好啊', 'zh', 1, {
    "spd": 4,
    'vol': 8,
    "pit": 6,
    "per": 0,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.m4a', 'wb') as f:
        f.write(result)
else:
    print(result)
