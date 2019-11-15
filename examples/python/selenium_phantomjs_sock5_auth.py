# -*- coding: utf-8 -*-
'''
使用selenium下的无窗口浏览器phantomjs的sock5认证代理示例
因为是无窗口浏览器，所以截了一张图片放在本程序当前目录下
可以打印了访问网址的title和源代码
'''
from selenium import webdriver

#要访问的目标网页
page_url = "http://dev.kuaidaili.com/testproxy"

#代理服务器ip和端口
ip = '59.38.241.25:23916'

#用户名和密码(私密代理/独享代理)
username = 'myusername'
password = 'mypassword'

#代理参数设置
service_args = [
    '--proxy=%s' % ip,
    '--proxy-type=socks5',
    '--proxy-auth=%s:%s' %(username,password)
]

#启动PhantomJS
driver = webdriver.PhantomJS(service_args = service_args)

#访问网址
driver.get(page_url)

#打出网页title和网页源代码
print driver.title
print driver.page_source

#退出PhantomJS
driver.quit()
