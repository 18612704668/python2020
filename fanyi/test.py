# python爬虫实现百度翻译
# urllib和request POST参数提交
from urllib import request,parse
import json

keyword = input('请输入翻译的单词：')
base_url = 'https://fanyi.baidu.com/#en/zh'
# 构建请求对象
data = {'kw': keyword}
data = parse.urlencode(data).encode('utf-8')
# 模拟浏览器
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
req = request.Request(url=base_url,data=data,headers=header)

res = request.urlopen(req)
print(req)
print(res)
'''
# 获取响应的json字符串
str_json = res.read().decode('utf-8')
# 把json转换成字典
myjson = json.loads(str_json)  # 将字符串转化为字典
info = myjson['data'][0]['v']
print(info)
'''
