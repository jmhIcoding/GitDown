# 简介
如果Github的项目太大，直接git clone可能下载到半路就中断了，导致反反复复下载不了。
这个时候应该咋办呢？
本人写了一个支持Github特定文件夹内容下载的项目：GitDown.
github地址为：https://github.com/jmhIcoding/GitDown

目前已经公开的类似项目，经常会出现下载文件丢失的问题，我这个项目会自动检测丢失，对于未成功下载的文件会反复尝试下载。

# 使用方法
## 安装

```bash
pip3 install pygithub requests

git clone https://github.com/jmhIcoding/GitDown.git
```

## 使用

```bash
cd src

python main.py -h
usage: main.py [-h] --repo REPO --directory DIRECTORY
               [--thread_num THREAD_NUM]

Download github resposity directory.

optional arguments:
  -h, --help            show this help message and exit
  --repo REPO           Something like
                        https://github.com/jmhIcoding/social_webpage
  --directory DIRECTORY
                        Something like pcaps/. Note that do not start with "/"
                        and end with "/", use "" (empty) for root directory.
  --thread_num THREAD_NUM
                        The thread number for download!

```

输入 仓库的名称，以及要下载的目录名就可以了。
注意仓库名的格式类似于：https://github.com/jmhIcoding/social_webpage，里面有用户名和仓库名。
目录名不能以“/” 开始和结束。


首次运行需要提供自己的github access token， 因为项目运行需要能够访问你自己的github项目，因此需要此token，获取方式见：https://blog.csdn.net/u014175572/article/details/55510825

```python
Please input your github access token now, first time:1234
```
如果输入的token，无效会报错：

```python
Please input your github access token now, first time:1234
Traceback (most recent call last):
  File "E:\GitDown\src\config.py", line 12, in <module>
    git.get_repo('helloworld9992939329392939294333435452dhfhdfjdfdgfgdfgfd___dfdf')
  File "C:\Program Files\Python36\lib\site-packages\github\MainClass.py", line 334, in get_repo
    "GET", "%s%s" % (url_base, full_name_or_id)
  File "C:\Program Files\Python36\lib\site-packages\github\Requester.py", line 319, in requestJsonAndCheck
    verb, url, parameters, headers, input, self.__customConnection(url)
  File "C:\Program Files\Python36\lib\site-packages\github\Requester.py", line 342, in __check
    raise self.__createException(status, responseHeaders, output)
github.GithubException.BadCredentialsException: 401 {"message": "Bad credentials", "documentation_url": "https://docs.github.com/rest"}

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "main.py", line 3, in <module>
    from src.parser_git_dir import *
  File "E:\GitDown\src\__init__.py", line 2, in <module>
    import config
  File "E:\GitDown\src\config.py", line 15, in <module>
    raise  ValueError('The token you input is invalid!!!')
ValueError: The token you input is invalid!!!

```

运行示例：

```bash
Download pcaps/weibo/shuqi/2021101/1633039566.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3133/3685 [26:02<09:38,  1.05s/it]Download pcaps/weibo/shuqi/2021101/1633039591.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3134/3685 [26:03<09:28,  1.03s/it]Download pcaps/weibo/shuqi/2021101/1633039615.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3135/3685 [26:03<07:17,  1.26it/s]Download pcaps/weibo/shuqi/2021101/1633039639.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3136/3685 [26:05<11:16,  1.23s/it]Download pcaps/weibo/shuqi/2021101/1633039663.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3137/3685 [26:06<09:52,  1.08s/it]Download pcaps/weibo/shuqi/2021101/1633039687.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3138/3685 [26:07<08:20,  1.09it/s]Download pcaps/weibo/shuqi/2021101/1633039711.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3139/3685 [26:08<08:58,  1.01it/s]Download pcaps/weibo/shuqi/2021101/1633039735.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3140/3685 [26:09<08:13,  1.11it/s]Download pcaps/weibo/shuqi/2021101/1633039759.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3141/3685 [26:09<07:23,  1.23it/s]Download pcaps/weibo/shuqi/2021101/1633039783.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3142/3685 [26:10<07:26,  1.22it/s]Download pcaps/weibo/shuqi/2021101/1633039807.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3143/3685 [26:10<06:24,  1.41it/s]Download pcaps/weibo/shuqi/2021101/1633039831.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3144/3685 [26:12<07:22,  1.22it/s]Download pcaps/weibo/shuqi/2021101/1633039856.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3145/3685 [26:12<06:55,  1.30it/s]Download pcaps/weibo/shuqi/2021101/1633039881.pcap now!
 85%|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ | 3146/3685 [26:13<05:36,  1.60it/s]Download pcaps/weibo/shuqi/2021101/1633039906.pcap now!

```
下载的结果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2e139e859d694001b7cc4eb67b970b69.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBASWNvZGluZ19GMjAxNA==,size_19,color_FFFFFF,t_70,g_se,x_16)
