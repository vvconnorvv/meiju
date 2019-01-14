## 概述
基于scrapy开发的美剧天堂前100美剧信息爬取
## 需求
目标网站：meijutt.com
需求：美剧排名前100信息获取 https://www.meijutt.com/new100.html
## 大概开发步骤
1. scrapy startproject movie
2. scrapy genspider meiju miejutt.com
3. 开发spiders/meiju.py 