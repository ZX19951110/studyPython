# -*- coding:utf-8 -*-
import re
class re_test(object):
    def test(self):
        demo = 'hello world 123 456'
        res = re.match('.+',demo)
        print(res)
        print(res.group())
        print(res.span())
    def tanlan_test(self):
        demo = 'test123456'
        res = re.match('^test.*?(\d+)',demo)#  .*如果后面不加？则变为贪婪匹配
        print(res)
        print(res.group(1))
        print(res.span())
    def html_test(self):
        html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
        title = re.findall('<h2 class="title">(.*?)</h2>',html)
        data_view = re.findall('<li data-view="(\d*)"',html)
        print(title)
        print(data_view)
if __name__ == '__main__':
    re_test = re_test()
    #re_test.test()
    #re_test.tanlan_test()
    re_test.html_test()