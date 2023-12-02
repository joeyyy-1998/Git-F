request模块：

请求接口网址： https://apis.tianapi.com/kuaidi/index 

1.POST /GET 

POST请求相对安全，GET请求相对不安全

GET请求可以缓存，POST请求不能缓存

GET请求有长度限制，POST请求没有长度限制

GET只能传输字符串，POST可以传输多种类型数据

GET请求入参在URL上，POST请求入参在Request body上

POST*有可能*产生两个数据包，GET只会发送一个数据包

刷新和回退的时候GET请求无害，POST数据会被重新提交

详细参考：‘https://juejin.cn/post/7219889814114975804?searchId=20231127163332127AF532BAB8E3CA6926’

2.在vscode创建自己的Python项目

详细参考：

‘https://huaweicloud.csdn.net/6549f5a05543f15fea1a22fd.html?dp_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mjc5OTA4LCJleHAiOjE3MDIwMjQ3NjUsImlhdCI6MTcwMTQxOTk2NSwidXNlcm5hbWUiOiJzaGVuZHVfXzEyMyJ9.oAo1-zJBKE76RQJc3Am3KkLvngoeJUueGcE0Wa2tvj8’

 3.小技巧： choice1,新建后手动选择语言,或在左侧新建时指定文件后缀 

 choice2: 先新建个空py文件，以后都从这个文件copy出来再打开 

4.html中的POST /GET 请求的区别

 注意 **GET 请求不应该有 body**，但POST存在body

