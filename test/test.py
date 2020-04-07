# urlopen的使用
#  from urllib import request
# resp = request.urlopen('https://www.baidu.com')
# print(resp.read())



#URL编码
# urlencode函数的使用方法
# from urllib import parse
# data = {'name':'爬虫基础','greet':'hello world','age':100}
# qs = parse.urlencode(data)
# print(qs)

# URL拼接
# from urllib import request
# from urllib import parse
# url = 'https://www.baidu.com/s'
# params = {"wd":"刘德华"}
# qs = parse.urlencode(params)
# url = url+'?'+qs
# print(url)
# resp = request.urlopen(url)
# print(resp.readlines())


#parse_qs（url解码）的使用
# from urllib import parse
# data = {'name':'爬虫基础','greet':'hello world','age':100}
# qs = parse.urlencode(data)
# print(qs)
# print(parse.parse_qs(qs))


#urlparse和urlsplit的使用
# from urllib import request,parse
#
# url = 'http://www.baidu.com/s?username=zhiliao'
#
# result = parse.urlsplit(url)
# # result = parse.urlparse(url)   #urlparse里面多了一个params属性，而urlsplit没有这个params属性
#
# print('scheme:',result.scheme)
# print('netloc:',result.netloc)
# print('path:',result.path)
# print('query:',result.query)


#reuest.Requset类
#如果想要在请求的时候增加一些请求头，那么就必须使用request.Request类来实现。比如要增加一个User-Agent，示例代码如下：

# from urllib import request
#
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
# }
# req = request.Request("http://www.baidu.com/",headers=headers)
# resp = request.urlopen(req)
# print(resp.read())

# from urllib import request
# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# headers = {
#  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
# }
# req = request.Request(url,headers=headers)
# resp = request.urlopen(req)
# print(resp.read())

#post请求，data参数的使用


from urllib import request,parse
url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
headers = {

    'Host':'www.lagou.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Connection':'keep-alive',
    'Cookie':'JSESSIONID=ABAAAECABGFABFF0BFA664E0488CA6D5B14AAAC55DD5B75; WEBTJ-ID=20200406211435-1714fa0dec48d4-0c3e33311f2eed-34564a7c-2073600-1714fa0dec544; user_trace_token=20200406211435-13524488-8c17-46d9-9126-7685f962ef59; LGSID=20200406211435-291267ed-37e6-46eb-9adf-4c3da68d0a16; LGUID=20200406211435-5c6f1089-566b-42e8-94f3-52441dcc0689; _ga=GA1.2.111789087.1586178875; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1586178875; _gid=GA1.2.1552387108.1586178876; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221714fa0f3dcea-0ed824e617ca66-34564a7c-2073600-1714fa0f3ddb34%22%2C%22%24device_id%22%3A%221714fa0f3dcea-0ed824e617ca66-34564a7c-2073600-1714fa0f3ddb34%22%7D; sajssdk_2015_cross_new_user=1; gate_login_token=e72542b3086a56ddd8f13cf59fd8f21b56386a94fb293fb351399e29cd3b782f; _putrc=71802467CA137A8E123F89F2B170EADC; login=true; unick=%E7%94%A8%E6%88%B74668; privacyPolicyPopup=false; hasDeliver=0; _gat=1; TG-TRACK-CODE=index_search; SEARCH_ID=b16dbb8d77134ebfb787131d7169ebbe; X_HTTP_TOKEN=6d98ce2d2d3a5f1c7122816851a6d563f91bc39fa9; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1586182218; LGRID=20200406221018-ab71c160-9bbe-486b-b558-5080a046cca7'
}
##如果爬虫访问失败，就添加cookie信息
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))


# from urllib import request
#
# # 这个是没有使用代理的
# # resp = request.urlopen('http://httpbin.org/get')
# # print(resp.read().decode("utf-8"))
#
# # 这个是使用了代理的
# handler = request.ProxyHandler({"http":"218.66.161.88:31769"})
#
# opener = request.build_opener(handler)
# req = request.Request("http://httpbin.org/ip")
# resp = opener.open(req)
# print(resp.read())


