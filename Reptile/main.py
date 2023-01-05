# 引入requests模块和BeautifulSoup模块
import requests
from bs4 import BeautifulSoup

# 引入内置os模块 用来创建文件夹
import os

# 保存数据
def get_data():
    #保存图片
    def get_pic(args):
        print(args)

        # 图片路径
        path = os.getcwd()+'/pic_data/'
        # 如果不存在，就新建
        if not os.path.exists(path):
            os.mkdir(path)

        # content用于获取图片
        res_pic = requests.get(args).content
        name = args.split('/')[-1]
        # 图片是二进制 使用wb
        w = open(path+name,'wb')
        # 写入图片
        w.write(res_pic)

        # 打印图片名称 保存成功
        print(name,'保存成功')

    #保存文字
    def get_text(args):
        path = os.getcwd() + '/text_data/'
        if not os.path.exists(path):
            os.mkdir(path)
        w = open(path+'data.txt','a',encoding='utf-8')
        w.write(args)
        print('保存成功',args)

    # 网址
    url = 'https://itawenya.cn'

    # 修改请求头
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        # ''
    }

    # 发送请求和获取
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')

    imgs = soup.find_all('img')
    # 循环获取图片网址
    for i in imgs:
        img_url = url + i['src'][1:]
        # 获取后调用方法，保存图片
        get_pic(img_url)

    # 获取文本内容
    elm_a = soup.find_all('a',attrs={'id':'QA-a'})
    elm_p = soup.find_all('p')

    # 获取后调用方法，保存文本
    for i in elm_p+elm_a:
        get_text(i.text)

# 运行程序
get_data()


