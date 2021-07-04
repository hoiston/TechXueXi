## headless version for docker
###  修改内容
* 使用headless driver（运行在无图形化的docker或服务器上）
* 使用单线程学习
* 调整部分input等不适应后台运行的方法
* 少量指定版本driver兼容性处理
* 必须使用钉钉机器人（以便于后台运行登录）
* 增加完成学习后钉钉机器人消息通知

### 20210616更新内容
* 解决钉钉二维码图片不显示的问题，补充输出二维码图片识别url。
    * based on https://github.com/TechXueXi/TechXueXi/issues/108 (thanks to mudapi)
    * **链接复制后打开学习APP，发送给自己，点击链接即可登录**
* 加入登录自动超时重试（重试2次）
* 加入超时退出（针对部分答题问题导致程序挂起）
* 去除docker容器配置文件，简化使用（现在只需要一条命令即可）

### 20210703更新内容
* 合并最新的0630主分支答题部分修改
* 支持arm架构docker（自动根据运行环境的arch判断拉取）
    * 目前通过QEMU构建基于arm64v8与arm32v7的镜像
    * 因无arm环境未进行测试验证，有问题可以提issue反馈（最好有报错的日志），请@wx5223
    * arm32v5的镜像目前还有较多的依赖包等问题（如上述镜像可以正常使用后期看需求再考虑）
* 增加部分答题异常处理，避免部分无限循环的问题


![](https://raw.githubusercontent.com/wx5223/TechXueXi/headless-single-docker/img_folder/dingding2.jpg)

提前准备
* 打开钉钉-建群或讨论组，踢掉好友（仅保留自己）
* 创建自定义机器人
* 获取token(Webhook地址中token)与secret(加签)


使用方法：
```
# 步骤1 创建并运行容器（首次运行，仅运行一次，除非删除容器）
docker run -d --name xuexi wx5223/xuexi:v20210703 python pandalearning.py 替换为自己的token 替换为自己的secret

# 启动容器（每天运行）
docker start xuexi
```
问题排查：
```
# 日志查看（仅用于排查问题）
docker logs xuexi
# 删除容器（可以重新执行步骤1 创建容器）
docker rm xuexi
```

#### 额外：
* 20210704：TechXueXi主库好像已被迁移，原issue等信息已经丢失，目前好像不能pull request。暂未同步至主库。
```
# 版本更新步骤：v20210616_headless -> v20210703
docker rm xuexi
# 重新执行步骤1，注意命令中的版本号v20210703
```
---
---
**[在线聊天室地址及说明](https://github.com/TechXueXi/TechXueXi/issues/14)**

**支持每日答题，支持每周答题，支持专项答题**

**下载地址：https://github.com/TechXueXi/TechXueXi/releases**

（如使用源码，请使用主分支。请勿使用 dev 分支，该分支用于存放正在开发的代码，不保证稳定、可用，可能造成问题）

> 本项目基于某已终止的项目，请自行搜索后前往star。我们由衷地敬佩这个领域的先锋们
![](https://raw.githubusercontent.com/TechXueXi/TechXueXi/master/img_folder/banner.jpg)

![](https://raw.githubusercontent.com/TechXueXi/TechXueXi/master/img_folder/kjqg.png)

本仓库现由“科技强国”组织进行维护，这是全网较好的成熟产品，但已停止，我们于心不忍。

许多IT人员本终日埋头写代码，确实有需求，与其各人重复修改编写浪费生产力不如团队合作维护，因此我们还是希望继续维护此生态。

若您有意愿加入本组织，持续对本项目进行维护，请发送主题“申请科技强国组织成员”的邮件至tobctobc@protonmail.com，请将您的github用户名添加到邮件正文中，便于发送邀请。谢谢。

本项目维护计划、路线图参见 https://github.com/TechXueXi/TechXueXi/projects/1

如您参与贡献，请注意：维护计划、路线图中每一条未列至"Done"下时，仅可在 dev 分支改动。

### [👨‍👨‍👦‍👦   直接参与贡献](https://github.com/TechXueXi/TechXueXi/blob/master/CONTRIBUTING.md)(内附提交方法)

如您开发了其他“科技强国”项目，也可以加入本组织，相互交流，共同维护生态。



# TechXueXi

TechXueXi 是一款使用python语言编写的学习工具。可达 47 分/天



![学习情景](https://github.com/TechXueXi/TechXueXi/blob/master/img_folder/peoplelearning.jpg?raw=true)
[![Badge](https://img.shields.io/badge/link-996.icu-%23FF4D5B.svg?style=flat-square)](https://996.icu/#/zh_CN)
 [![GitHub stars](https://img.shields.io/github/stars/TechXueXi/TechXueXi.svg?style=social)](https://github.com/TechXueXi/TechXueXi/stargazers)     [![GitHub forks](https://img.shields.io/github/forks/TechXueXi/TechXueXi.svg?style=social)](https://github.com/TechXueXi/TechXueXi/network/members)  `请点击页面顶部靠右star与fork`







[![GitHub release](https://img.shields.io/github/release/TechXueXi/TechXueXi.svg?label=%E7%89%88%E6%9C%AC)](https://github.com/TechXueXi/TechXueXi/releases/tag/)   ![GitHub top language](https://img.shields.io/github/languages/top/TechXueXi/TechXueXi.svg)  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/TechXueXi/TechXueXi.svg)  ![GitHub repo size](https://img.shields.io/github/repo-size/TechXueXi/TechXueXi.svg) ![GitHub](https://img.shields.io/github/license/TechXueXi/TechXueXi.svg) ![platforms](https://img.shields.io/badge/platform-win32%20%7C%20win64%20%7C%20linux%20%7C%20osx-brightgreen.svg)     [![GitHub issues](https://img.shields.io/github/issues/TechXueXi/TechXueXi.svg)](https://github.com/TechXueXi/TechXueXi/issues)  [![GitHub closed issues](https://img.shields.io/github/issues-closed/TechXueXi/TechXueXi.svg)](https://github.com/TechXueXi/TechXueXi/issues?q=is%3Aissue+is%3Aclosed) ![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/TechXueXi/TechXueXi.svg)   ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/TechXueXi/TechXueXi.svg)  ![GitHub contributors](https://img.shields.io/github/contributors/TechXueXi/TechXueXi.svg)


[TOC]

## 📃免责声明
TechXueXi为python学习交流的开源非营利项目，仅作为程序员之间相互学习交流之用，使用需严格遵守开源许可协议。严禁用于商业用途，禁止使用TechXueXi进行任何盈利活动。对一切非法使用所产生的后果，我们概不负责。

![](https://raw.githubusercontent.com/TechXueXi/TechXueXi/master/img_folder/qsjwczlhql.jpg)



## 👍程序特性

<img align="right" width="300" src="https://raw.githubusercontent.com/TechXueXi/TechXueXi/master/img_folder/phone.jpg" alt="copy URL to clipboard" />



###### 全平台支持： win，macos，linux，vps，Raspbian-pi等各种平台

请使用带图形界面的环境,推荐windows。尽量使用自用电脑，最好不要使用vps,云主机等（因为有可能被xuexi根据服务商ip查到）。

`不支持xp`

###### 全程后台静默学习： 也可开启前台学习展示

###### 自动核对学习分数： 根据每日分数学满为止

###### ~~支持保存账户信息： 可以保存帐户信息每日免去重复登陆~~

###### 默认多线程学习：  可关闭，建议开启，每日学满只需20分钟

###### ~~可设置自动关机：  每天下班用办公室电脑学习后自动关机~~

###### 增强防检测：随机浏览器请求头及自然学习行为模拟





`右侧为手机操作vps示例`

另有安卓本地运行方式，请查看issue #323 （可能无法使用）



## 📗使用方法

### 🔑快速使用

​	`解压后运行 TechXueXi 来启动程序；`

​	~~根据提示输入用户标记，标记可以是任意***英文/中文/数字***~~

​	~~根据提示选择是否保存钉钉账号密码，保存后下次使用将不需要输入。~~

​	`登陆之后自动学习`

​	注意`mac需要在终端中打开`

​	`二维码登陆弹出右侧提示勿点击停用，直接x掉即可`

<img align="right" width="410" src="https://raw.githubusercontent.com/TechXueXi/TechXueXi/master/img_folder/detection.png" alt="copy URL to clipboard" />

### 🔐进阶使用
<!--
​    快捷方式中或者终端运行时加入参数分别是：

​	`第一个参数为用户标记；`

​	`第二个参数为 hidden 或 show，对应后台运行和前台运行；`

​	`第三个参数为 single 或 multithread, 对应单线程和多线程学习；`

​	`第四个参数为 num 为输入一个数字，表示学习完成后多少秒自动关机。`  

### 📅示例 win平台

​    user1 为已经保存了钉钉账户的用户标记

​	`TechXueXi.exe user1 表示自动开启user1 学习`

​	`TechXueXi.exe user1 show single 表示前台显示且单线程开启user1 学习`

​	`TechXueXi.exe user1 hidden multithread 300 表示后台多线程开启user1 学习，学习完毕300秒关机`
-->
### 🔧更新方法

​    下载更新包覆盖原文件，打开程序验证版本信息







## 💾下载地址
**非windows系统请暂时使用源码或虚拟机运行，各位若编译了二进制文件，可以邮件我们（推荐）或提交PR，谢谢————20200428**


<!--
[windows高速下载](https://github.com/TechXueXi/TechXueXi/releases)


[全部文件列表](https://techxuexi.github.io/TechXueXi-download/)

[![](https://img.shields.io/badge/download-win%20完整版-blue.svg?style=for-the-badge&logo=windows)](https://techxuexi.github.io/TechXueXi-download/Panda_learning-win.7z)  首次使用推荐下载

[![](https://img.shields.io/badge/download-win%20更新包-blue.svg?style=for-the-badge&logo=windows)](https://techxuexi.github.io/TechXueXi-download/pandalearning.exe) ![](https://img.shields.io/badge/size-6.91%20mb-9cf.svg?style=social)  下载覆盖即可使用，老用户下载

------

[![](https://img.shields.io/badge/download-osx%20程序包-green.svg?style=for-the-badge&logo=apple)](https://techxuexi.github.io/TechXueXi-download/原作者旧版/pandalearning_macos.zip) ![](https://img.shields.io/badge/size-12.9%20mb-9cf.svg?style=social)   需预先安装Chrome浏览器

[![](https://img.shields.io/badge/download-osx%20浏览器-green.svg?style=for-the-badge&logo=google-chrome)](https://techxuexi.github.io/TechXueXi-download/原作者旧版/googlechrome.dmg) ![](https://img.shields.io/badge/size-74.3%20mb-9cf.svg?style=social)   Google Chrome镜像

------

[![](https://img.shields.io/badge/download-linux%20程序-orange.svg?style=for-the-badge&logo=linux)](https://techxuexi.github.io/TechXueXi-download/原作者旧版/pandalearning_linux.tar.gz) ![](https://img.shields.io/badge/size-11.2%20mb-9cf.svg?style=social)   需预先安装Chrome浏览器

[![](https://img.shields.io/badge/download-rpm%20浏览器-orange.svg?style=for-the-badge&logo=google-chrome)](https://techxuexi.github.io/TechXueXi-download/原作者旧版/google-chrome-stable_current_x86_64.rpm) ![](https://img.shields.io/badge/size-55.1%20mb-9cf.svg?style=social)   适用于 Fedora/openSUSE

[![](https://img.shields.io/badge/download-deb%20浏览器-orange.svg?style=for-the-badge&logo=google-chrome)](https://techxuexi.github.io/TechXueXi-download/原作者旧版/google-chrome-stable_current_amd64.deb)  ![](https://img.shields.io/badge/size-55.0%20mb-9cf.svg?style=social)   适用于 Debian/Ubuntu

[Fedora/openSUSE dnf安装Chrome和Chromedriver方法](<https://github.com/TechXueXi/TechXueXi/blob/master/FedoraopenSUSE%E5%BF%AB%E9%80%9F%E4%BD%BF%E7%94%A8Panda-Learning%E6%96%B9%E6%B3%95.md>)



------

[![](https://img.shields.io/badge/download-树莓派%20版本-ff69b4.svg?style=for-the-badge&logo=raspberry-pi)](https://techxuexi.github.io/TechXueXi-download/原作者旧版/google-chrome-stable_current_amd64.deb)  ![](https://img.shields.io/badge/size-6.25%20mb-9cf.svg?style=social)   适用于 raspberrypi

[Raspberry Pi 说明](https://github.com/TechXueXi/TechXueXi/blob/master/%E6%A0%91%E8%8E%93%E6%B4%BE%E7%89%88%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md)

-->

## 📑常见问题

win平台可能提示`无法定位程序输入点ucrtbase.terminate于动态链接库api-ms-win-crt-runtime-|1-1-0.dll`等缺失dll文件的问题而无法使用，尝试安装`Visual C++ Redistributable for Visual Studio 2015`

**下载安装:**

[![](https://img.shields.io/badge/download-vc_redist.x64-blue.svg?style=for-the-badge&logo=visualstudiocode)](https://raw.fastgit.org/TechXueXi/Panda-Learning/master/windows不能运行时安装/vc_redist.x64.exe) 

[![](https://img.shields.io/badge/download-vc_redist.x86-blue.svg?style=for-the-badge&logo=visualstudiocode)](https://raw.fastgit.org/TechXueXi/Panda-Learning/master/windows不能运行时安装/vc_redist.x86.exe) 





## 📕问题提交

在仔细阅读文档的前提下

- 检查当前的issue是否有与你相关的。发布重复的issue会让双方都降低效率，搜索开放和已经关闭的issue来检查你现在提出的issue是否已经被提及。
- 请明确你的问题：期望的输出是什么，实际发生了什么？以及其他人如何复现你的问题。
- 对结果的链接：复现问题的方式
- 汇报系统环境的详细信息，注明程序版本号与运行环境。
- 如果你粘贴错误输出到一个issue中，请使用三个反引号包裹` ```使得显示更漂亮易读``` `。

[![GitHub issues](https://img.shields.io/github/issues/TechXueXi/TechXueXi.svg)](https://github.com/TechXueXi/TechXueXi/issues)  [![GitHub closed issues](https://img.shields.io/github/issues-closed/TechXueXi/TechXueXi.svg)](https://github.com/TechXueXi/TechXueXi/issues?q=is%3Aissue+is%3Aclosed) 

提交issue标题示例  `V2.4 win10x64 软件显示问题…`




## 📌关于学习强国

个人认为，学习强国本身受众就是国家的栋梁，本人不欢迎不热爱国家的人加入本项目。

学习强国聚合了大量可免费阅读的期刊、古籍、公开课、歌曲、戏曲、电影、图书等资料，内容严谨，专业性强。没有博眼球，无下限的自媒体内容和虚假新闻。推荐大家自发积极学习使用。TechXueXi 仅额外提供给上班上学期间工作学业繁重，抽不出时间完成学习强国任务的非程序员。

“学习强国”意义深远。





## 📝源码

[![](https://img.shields.io/badge/source-pandalearning-orange.svg?style=for-the-badge&logo=visualstudiocode)](https://github.com/TechXueXi/TechXueXi/tree/master/SourcePackages) 

简易说明，具体请谷歌必应百度

安装 python 3

### win源码使用说明

1. 下载 ChromeDriver，chrome 并配置好

2. 安装所需 python 模块

```
pip install -r requirements.txt
```

3. 执行文件

```
python ./pandalearning.py
```


### mac源码使用说明

1. 安装ChromeDriver

```
brew install chromedriver
```

2. 安装所需 python 模块

```
pip install -r requirements.txt
```

3. 执行文件

```
python3 ./pandalearning.py
```





## 📜许可证

![GitHub](https://img.shields.io/github/license/TechXueXi/TechXueXi.svg) 

[![](https://github.com/TechXueXi/TechXueXi/blob/master/img_folder/1920px-LGPLv3_Logo.svg.png?raw=true)](https://github.com/TechXueXi/TechXueXi/blob/master/LICENSE)

 
# **我们不接受任何捐赠。**
