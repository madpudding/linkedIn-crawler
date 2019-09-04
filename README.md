# -
领英的爬虫-linked-scrapy
这是一个抓取领英的小爬虫，不是特别复杂，但我写了一定的时间，其中的思路和设计模式，现在的我看来，有些可以改进的地方，但我已经懒得改了。

下面说一下我的架构吧：
（1）：linkedin_crawler
（2）：linkedin-cookie负责cookie信息
（3）：linkedin—redis负责存储检验
具体介绍可以查看：https://blog.csdn.net/qq_40244755/article/details/84896938

领英上个人信息还是挺多，说起来这也算小小的侵犯隐私了，罪过，罪过。

Star在"2019.10.1"之前到40,目前13颗star，重写领英爬虫，目前想好有scrapy和普通的requests的两个版本，requests版本的封装和项目结构、健壮性都会比现在的好~
