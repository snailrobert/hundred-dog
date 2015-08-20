#!env python
#coding=UTF-8

import os
import re
import urllib
import urllib2
import PIL.Image as Image  

def get_url(pagenum):
    open_url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?format=json&ie=utf-8&oe=utf-8&query=%E7%8B%97&resource_id=6829&rn=72&from_mid=1&pn="+str(pagenum*71)+"&type_size=&type_func=&type_feat=&t=1440056394086&cb=jQuery110209821268892654501_1440053900697&_=1440053900711"
    htmlpaper = urllib2.urlopen(open_url).read()
    htmlurl=re.findall('/u=[0-9]*,[0-9]*&fm=5(?=\")',htmlpaper)
    return htmlurl

def outimg():
    ix=121*4
    iy=121*45
    outImage = Image.new('RGBA', (ix, iy))
    for y in  range(1,46):
        for x in range(1,5):
            if(x*y<178):
                inImage = Image.open('tmp/'+str(x*y)+'.jpg')  
                outImage.paste(inImage,( (x-1)*121, (y-1)*121)) 
    outImage.save('tmp/outimg.jpg')
for num in range(0,3):
    tmp=get_url(num)
    count=num*71;
    for i in tmp:
        urllib.urlretrieve('https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/'+i,'tmp/'+str(count+1)+'.jpg')
        count=count+1
outimg()