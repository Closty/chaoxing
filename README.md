## 介绍
[![](https://img.shields.io/badge/%E8%B6%85%E6%98%9F-%E8%87%AA%E5%8A%A8%E7%AD%BE%E5%88%B0-orange?link=https://www.choaoxing.com&link=https://github.com/Closty/chaoxing)](https://github.com/Closty/chaoxing)
[![](https://img.shields.io/badge/by-%E7%93%B6%E5%AD%90-green?link=https://www.clost.net)](https://www.clost.net/default/871.html)
![chaoxing](https://github.com/Closty/chaoxing/workflows/chaoxing/badge.svg)
[![HitCount](http://hits.dwyl.com/closty/chaoxing.svg)](http://hits.dwyl.com/closty/chaoxing)

<img src="https://s1.ax1x.com/2020/04/26/JRuNrR.png" width = "500" height = "300" alt="github实现云签到" align=center />

### 前言
为了让同学们更加认真、更加专注听课，而不去用手机签到花费大量时间、耗费大量精力，特此在[原脚本](https://github.com/mkdir700/chaoxing_auto_sign)中开发升级，请自行合理使用！挂科请不要找我，谢谢合作！请点击下方View all of README.md了解更多。

本项目支持学习通任何形式的签到（包括二维码签到、手势签到等），如果是位置签到也可以自定义位置，如果是拍照签到，请自认倒霉，因为默认是黑色照片，自定义照片还在等待开发中。

本脚本最大的不同应该就是基于github action运行，所以并不需要服务器、不需要服务器、不需要服务器同样也不需要掌握任何python的相关设置，你所需要准备的就是一个github账号以及一个耐而不烦的心。傻瓜式的操作却可以解决你最大的痛苦。

### 特点
1、基于原先作者强大的脚本，本项目支持任何形式的学习通签到。<br>
2、基于server酱使得签到成功时会将签到信息发送至你的微信。<br>
2、无需挂在任何服务器上，只需要点几下，让github自动为你签到。<br>
3、使用强大的GitHub actions功能，实现无服务器实时监控您的学习通签到。<br>
4、无需掌握任何编程知识，强大的后端后端已做好，您仅需点击几下。



## 快速使用


[无法查看图片？](https://www.clost.net/default/871.html "无法查看图片？")

- Fork本项目后进入自己的仓库，点击你的仓库右上角的 Settings，找到 Secrets
    <details>
   <summary> 如何Fork本项目？</summary>
   注册或登陆您的github账号，访问<https://github.com/Closty/chaoxing>进入github的本项目页面中，点击右上角的Fork按钮，如图所示。
   
   ![Fork本项目][7]
   
   </details>
-  fork后进入你自己的仓库并在setting配置您的超星账号信息
    <details>
   <summary> 如何配置？</summary>
   1.首先进入自己的仓库（前提您已经登陆账号）
	
   ![E19D60FD6823769D2822C93960835D01.jpg][3]
   <br><br><br>
   2.点击chaoxing字样的项目也就是刚刚fork后的项目
   
   ![41CA3BC4C95CAE8D7F8FB3A05B816CB0.jpg][4]
   <br><br><br>
   3.点击setting进入设置界面
   
   ![711234FE886728474A5326E42A06A40E.jpg][5]
   <br><br><br>
   4.点击secrets后点击add a new secret
   
   ![3AB6B127331F5CCE552730FACDA680A3.jpg][6]
   <br><br><br>
   依次添加以下所有name以及value。<br>
    ┉┉ ∞ ∞ ┉┉┉┉ ∞ ∞ ┉┉┉ <br>Name:<code>CHAOXING_USERNAME</code><br>
	Value：<code>填写你的超星账户，最好为11位的手机号</code><br>
   ┉┉ ∞ ∞ ┉┉┉┉ ∞ ∞ ┉┉┉<br>
     Name：<code>CHAOXING_PASSWORD</code><br>
     Value：<code>填写你的超星密码</code><br>
    ┉┉ ∞ ∞ ┉┉┉┉ ∞ ∞ ┉┉┉<br>
     Name：<code>CHAOXING_SCHOOL</code><br>
     Value：<code>填写你的schoolid</code>#如果CHAOXING_USERNAME中的Value填写的是手机号，则本处填写'None'<br>
     ┉┉ ∞ ∞ ┉┉┉┉ ∞ ∞ ┉┉┉<br>
     Name：<code>CHAOXING_SERVEROR</code><br>
     Value：<code>填写True或者False</code>#True代表使用微信提醒，False代表不使用<br>
     ┉┉ ∞ ∞ ┉┉┉┉ ∞ ∞ ┉┉┉<br>
     Name：<code>CHAOXING_SERVER</code><br>
     Value：<code>填写你的server酱SCKEY码，以SCU开头</code>#申请地址http://sc.ftqq.com/3.version  <br>
      ┉┉ ∞ ∞ ┉┉┉┉ ∞ ∞ ┉┉┉<br>配置完后如下图所示

   ![3ABA6F49DE5D7DB3144B14FC9A7F1809.jpg][2]
   
    </details>
- 设置好环境变量后点击你的仓库上方的 Actions 选项，会打开一个如下的页面，点击 `I understand...` 按钮确认在 Fork 的仓库上启用 GitHub Actions 。
- 最后在你这个 Fork 的仓库内随便改点什么（比如给 README 文件删掉或者增加几个字符）提交一下手动触发一次 GitHub Actions 就可以了 **（重要！！！测试发现在 Fork 的仓库上 GitHub Actions 的定时任务不会自动执行，必须要手动触发一次后才能正常工作）** 。
   <details>
   <summary> 如何随意修改README文件？</summary>
   
   1.进入你的仓库并进入code界面,点击笔字的按钮进入编写
   ![2D6731A3F5A39D89D91B4F201F8C0B70.jpg](https://cdn.jsdelivr.net/gh/closty/tuchuang/usr/uploads/2020/04/3647386614.jpg)<br><br><br>
   2.在代码框随意编写或删减以达到改变代码的效果，随后点击提交commit，当然如果可以让说明书更精美欢迎来pull
   ![E0F2D41544BE07971A596488E7A72EAA.jpg](https://cdn.jsdelivr.net/gh/closty/tuchuang/usr/uploads/2020/04/3472948209.jpg)

   </details>
   
- <details>
   <summary> 如何查看脚本执行情况？</summary>
   注意： 为了实现某个链接/帐户访问出错时不中断程序继续尝试下一个，GitHub Actions 的状态将永远是“通过”（显示绿色的✔），请自行检查 GitHub      Actions 日志：依次点击<code>Actions</code>=><code>chaoxing</code>=><code>get_points</code>=><code>Qiandao</code>项的输出确定程序执行情况。
	
   ![6D6681A2A552E03AE2AEC28B4542F217.jpg][1]

   </details>





## 配置说明
- 配置自动执行时间
时间配置在`chaoxing/.github/workflows/cxworker.yml`文件中 第九行    `- cron: '* * * * *'`
默认：每5-6分钟自动执行签到脚本（github有时间延迟与相应限制），你也可以通过 `Push` 操作手动触发执行。
如需自定义时间，请配合[cron表达在线生成器](https://cron.clost.net "cron表达在线生成器")使用
- 配置python脚本
python脚本在`chaoxing/cx.py`文件中，其中第12—34行为配置区域，如需自己的服务器运行更改含有`os.environ`的相关参数即可。 
- 配置位置签到
进入`chaoxing/cx.py`修改225行`'address': '中国',`的`中国`为你想显示的位置；修改227行`'clientip': '0.0.0.0',`的`0.0.0.0`为你想显示的[ip地址](https://www.ip138.com/ "ip地址")。
- 配置拍照签到
目前无法配置，默认纯黑色照片，请等待更新。

## 关于
本项目基于https://github.com/mkdir700/chaoxing_auto_sign
制作，使得脚本可以无服务器执行，并简化操作以让更多人使用。
本项目遵循GNU GPLv3开源协议；并有以下条款特此说明：
1. 请勿使用本项目进行商业用途
1. 请勿使用本项目违反当地法规
1. 请勿使用本项目损害他人或集团利益

以上条款，若使用者违反，后果自行承担与作者本人无关！

## 鸣谢

[mkdir700](https://github.com/mkdir700)

## 其他项目推荐

| 项目地址                                                | 开发语言   | 备注                                           |
| ------------------------------------------------------- | ---------- | ---------------------------------------------- |
| https://github.com/mkdir700/chaoxing_auto_sign          | Python     |  超星学习通自动签到脚本&多用户多任务&API      |
| https://github.com/Wzb3422/auto-sign-chaoxing           | TypeScript | 超星学习通自动签到，梦中刷网课       |
| https://github.com/Huangyan0804/AutoCheckin             | Python     | 学习通自动签到，支持手势，二维码，位置，拍照等 |
| https://github.com/aihuahua-522/chaoxing-testforAndroid | Java       | 学习通（超星）自动签到               |
| https://github.com/yuban10703/chaoxingsign              | Python     | 超星学习通自动签到                   |



## 紧急通知

请一定要根据配置说明配置计划时间；防止被判定滥用。
<br>
由于本项目被大量fork并启动actions功能，占用github官方服务器大量资源。部分用户反映无法签到，actions功能被禁止等问题。但是大部分用户仍然正常可以使用；解决方法：1.使用使用Travis Ci运行。学业繁忙，不予教程。2.请访问我的服务器 https://cx.clost.net 但并不保证其稳定性。（目前源码臃肿，修改删减后上传）3.用自己的服务器运行其中的py脚本。


[7]: https://cdn.jsdelivr.net/gh/closty/tuchuang/usr/uploads/2020/04/3749713206.png
[1]: https://cdn.jsdelivr.net/gh/closty/tuchuang/usr/uploads/2020/04/3207755264.jpg
[2]:https://cdn.jsdelivr.net/gh/closty/tuchuang/usr/uploads/2020/04/437025077.jpg
[3]:https://cdn.jsdelivr.net/gh/closty/tuchuang/usr/uploads/2020/04/3185006214.jpg
[4]:https://cdn.jsdelivr.net/gh/closty/tuchuang/usr/uploads/2020/04/977504155.jpg
[5]:https://cdn.jsdelivr.net/gh/closty/tuchuang/usr/uploads/2020/04/1888532943.jpg
[6]:https://cdn.jsdelivr.net/gh/closty/tuchuang/usr/uploads/2020/04/3351341396.jpg
