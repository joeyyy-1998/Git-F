import requests
import json

def GET(number):
    result = requests.get(
        'https://apis.tianapi.com/tianqi/index?key=0e2c14f1c9ab22c92478155dfdeccb21&number=' + number )
    # 解析python request之后的返回结果的json格式
    resultJson = result.json()
    #返回需要的json字典
    return resultJson

 

def POST(number):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    result = requests.post('https://apis.tianapi.com/tianqi/index',
                           data={
                               'key': '0e2c14f1c9ab22c92478155dfdeccb21',
                               'number': number,
                           }, headers=headers)
    
    resultJson = result.json()
     
    return resultJson 
 


def QueryPackageDetail(choice, number):
    if choice == '1':
        print('----已选择GET协议！----')
        x = GET(number)
        
    elif choice == '2':
        print('----已选择POST协议！----')
        x = POST(number)
    else:
        print('----Error:选择错误----')


    print('--------------查询结果：---------------')
    print('状态：',x.get('result').get('status'))
    print('更新时间：',x.get('result').get('updatetime'))
    print('快递名：',x.get('result').get('kuaidiname'))
    print('团购名：',x.get('result').get('enkuaidiname'))
    print('电话：',x.get('result').get('telephone'))
    print('--------------查询结果：---------------')


    print('请选择你想要使用的协议：1.GET 2.POST')
    choice = input('你的协议选择：')
    number = input('请输入需要查询的快递单号：')
    QueryPackageDetail(choice,number)