import requests
import json

def GET(text):
    result = requests.get(
        'https://apis.tianapi.com/fanyi/index?key=2ca1c8dfd378ba935996ce837f62bf4c&text=' + text)
    # 解析python request之后的返回结果的json格式
    resultJson = result.json()
    #返回需要的json字典
    return resultJson


def POST(text):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'  #post方式请求时，enctype应为application/x-www-form-urlencoded
    }
    result = requests.post('https://apis.tianapi.com/fanyi/index',
                           data={
                               'key': '2ca1c8dfd378ba935996ce837f62bf4c',
                               'text': text,
                           }, headers=headers)
    
    resultJson = result.json()    #这里若是txt，则返回resultJson1 = result.txt()
    #返回需要的json字典
    return resultJson 

def TranslateTxt(choice,text):
    if choice == '1':
        print('----已选择GET协议！----')
        x = GET(text )
        
    elif choice == '2':
        print('----已选择POST协议！----')
        x = POST(text)
    else:
        print('----Error:选择错误----')

    print('--------------该文本翻译结果如下：---------------')
    #print(x)
    print('待翻译文本',x.get('result').get('src'))
    print('已翻译文本',x.get('result').get('dst'))
    print('--------------该文本翻译结果完成：---------------')

print('请选择你想要使用的协议：1.GET 2.POST')
choice = input('你的协议选择：')
text = input('请输入需要翻译的文本：')          
     
TranslateTxt(choice,text)