## 快速使用

- Fork本项目后进入自己的仓库，点击你的仓库右上角的 Settings，找到 Secrets
    <details>
   <summary> 如何Fork本项目？</summary>
   注册或登陆您的github账号，访问<https://github.com/Closty/chaoxing>进入github的本项目页面中，点击右上角的Fork按钮，如图所示。
   
   ![Fork本项目][7]
   [7]: https://cdn.jsdelivr.net/gh/closty/tuchuang/usr/uploads/2020/04/3749713206.png
   
   </details>
-  点击Add a new secret以配置你的信息
    <details>
   <summary> 如何配置？</summary>
    第一项
      Name：`CHAOXING_USERNAME`
      Value：`填写你的超星账户，最好为11位的手机号`
    第二项
     Name：`CHAOXING_PASSWORD`
      Value：`填写你的超星密码`
	第三项
     Name：`CHAOXING_SCHOOL`
      Value：`填写你的schoolid`#如果CHAOXING_USERNAME中的Value填写的是手机号，则本处填写'None'
	第四项
      Name：`CHAOXING_SERVEROR`
      Value：`填写True或者False`#True代表使用微信提醒，False代表不使用
	 第五项
    - Name：`CHAOXING_SERVER`
      Value：`填写你的server酱SCKEY码，以SCU开头`#申请地址http://sc.ftqq.com/3.version  
	     
 >  不分前后顺序，完成后如下图所示		 不分前后顺序，完成后如下图所示

   ![3ABA6F49DE5D7DB3144B14FC9A7F1809.jpg](https://cdn.jsdelivr.net/gh/closty/tuchuang/usr/uploads/2020/04/437025077.jpg)
   
    </details>
- 设置好环境变量后点击你的仓库上方的 Actions 选项，会打开一个如下的页面，点击 `I understand...` 按钮确认在 Fork 的仓库上启用 GitHub Actions 。
- 最后在你这个 Fork 的仓库内随便改点什么（比如给 README 文件删掉或者增加几个字符）提交一下手动触发一次 GitHub Actions 就可以了 **（重要！！！测试发现在 Fork 的仓库上 GitHub Actions 的定时任务不会自动执行，必须要手动触发一次后才能正常工作）** 。
- <details>
   <summary> 如何查看脚本执行情况？</summary>
**注意：** 为了实现某个链接/帐户访问出错时不中断程序继续尝试下一个，GitHub Actions 的状态将永远是“通过”（显示绿色的✔），请自行检查 GitHub Actions 日志：依次点击`Actions`=>`chaoxing`=>`get_points`=>`Qiandao` 项的输出确定程序执行情况。
![6D6681A2A552E03AE2AEC28B4542F217.jpg](https://cdn.jsdelivr.net/gh/closty/tuchuang/usr/uploads/2020/04/3207755264.jpg)
   
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

## 其他项目推荐

| 项目地址                                                | 开发语言   | 备注                                           |
| ------------------------------------------------------- | ---------- | ---------------------------------------------- |
| https://github.com/mkdir700/chaoxing_auto_sign          | Python     |  超星学习通自动签到脚本&多用户多任务&API      |
| https://github.com/Wzb3422/auto-sign-chaoxing           | TypeScript | 超星学习通自动签到，梦中刷网课       |
| https://github.com/Huangyan0804/AutoCheckin             | Python     | 学习通自动签到，支持手势，二维码，位置，拍照等 |
| https://github.com/aihuahua-522/chaoxing-testforAndroid | Java       | 学习通（超星）自动签到               |
| https://github.com/yuban10703/chaoxingsign              | Python     | 超星学习通自动签到                   |


