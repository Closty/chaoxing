# -*- coding: utf8 -*-
import os
import time
import urllib3
import asyncio
import re
import json
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# =================配置区start===================

# 学习通账号密码
user_info = {
	'username': os.environ["CHAOXING_USERNAME"],
	'password': os.environ["CHAOXING_PASSWORD"],
	'schoolid': os.environ["CHAOXING_SCHOOL"] # 学号登录才需要填写
}

# server酱
server_chan_sckey = os.environ["CHAOXING_SERVER"]  # 申请地址http://sc.ftqq.com/3.version
server_chan = {
	'status': os.environ["CHAOXING_SERVEROR"] ,  # 如果关闭server酱功能，请改为False
	'url': 'https://sc.ftqq.com/{}.send'.format(server_chan_sckey)
}

# 学习通账号cookies缓存文件路径
cookies_path = "cookies.json"  # cookies.json 保存路径

# activeid保存文件路径
activeid_path = "activeid.txt"

# =================配置区end===================


class AutoSign(object):

	def __init__(self, username, password, schoolid=None):
		"""初始化就进行登录"""
		self.headers = {
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
		self.session = requests.session()
		self.session.headers = self.headers
		# 读取指定用户的cookies
		if self.check_cookies_status(username) is False:
			self.login(password, schoolid, username)
			self.save_cookies(username)

	def save_cookies(self, username):
		"""保存cookies"""
		new_cookies = self.session.cookies.get_dict()
		with open(cookies_path, "r") as f:
			data = json.load(f)
			data[username] = new_cookies
			with open(cookies_path, 'w') as f2:
				json.dump(data, f2)

	def check_cookies_status(self, username):
		"""检测json文件内是否存有cookies,有则检测，无则登录"""
		if "cookies.json" not in os.listdir("./"):
			with open(cookies_path, 'w+') as f:
				f.write("{}")

		with open(cookies_path, 'r') as f:

			# json文件有无账号cookies, 没有，则直接返回假
			try:
				data = json.load(f)
				cookies = data[username]
			except Exception:
				return False

			# 找到后设置cookies
			for u in cookies:
				self.session.cookies.set(u, cookies[u])

			# 检测cookies是否有效
			r = self.session.get('http://i.mooc.chaoxing.com/app/myapps.shtml', allow_redirects=False)
			if r.status_code != 200:
				print("cookies已失效，重新获取中")
				return False
			else:
				print("cookies有效哦")
				return True

	def login(self, password, schoolid, username):
		# 登录-手机邮箱登录
		if schoolid:
			r = self.session.post(
				'http://passport2.chaoxing.com/api/login?name={}&pwd={}&schoolid={}&verify=0'.format(username, password,
				                                                                                     schoolid))
			if json.loads(r.text)['result']:
				print("登录成功")
			else:
				print("登录失败，请检查账号密码是否正确")

		else:
			r = self.session.get(
				'https://passport2.chaoxing.com/api/login?name={}&pwd={}&schoolid=&verify=0'.format(username, password),
				headers=self.headers)
			if json.loads(r.text)['result']:
				print("登录成功")
			else:
				print("登录失败，请检查账号密码是否正确")

	def check_activeid(self, activeid):
		"""检测activeid是否存在，不存在则添加"""
		with open(activeid_path, 'r') as f:
			s = f.read()
			if activeid in s:
				return True
		with open(activeid_path, 'w+') as f:
			f.writelines(activeid)
			return False

	def get_all_classid(self) -> list:
		"""获取课程主页中所有课程的classid和courseid"""
		re_rule = r'<li style="position:relative">[\s]*<input type="hidden" name="courseId" value="(.*)" />[\s].*<input type="hidden" name="classId" value="(.*)" />[\s].*[\s].*[\s].*[\s].*[\s].*[\s].*[\s].*[\s].*[s].*[\s]*[\s].*[\s].*[\s].*[\s].*[\s].*<a  href=\'.*\' target="_blank" title=".*">(.*)</a>'
		r = self.session.get(
			'http://mooc1-2.chaoxing.com/visit/interaction',
			headers=self.headers)
		res = re.findall(re_rule, r.text)
		return res

	async def get_activeid(self, classid, courseid, classname):
		"""访问任务面板获取课程的活动id"""
		# sign_re_rule = r'<div class="Mct" onclick="activeDetail\((.*),2,null\)">[\s].*[\s].*[\s].*[\s].*<dd class="green">.*</dd>'
		# sign_type_re_rule = r'<a href="javascript:;" shape="rect">\[(.*)\]</a>'
		re_rule = r'<div class="Mct" onclick="activeDetail\((.*),2,null\)">[\s].*[\s].*[\s].*[\s].*<dd class="green">.*</dd>[\s]+[\s]</a>[\s]+</dl>[\s]+<div class="Mct_center wid660 fl">[\s]+<a href="javascript:;" shape="rect">(.*)</a>'
		r = self.session.get(
			'https://mobilelearn.chaoxing.com/widget/pcpick/stu/index?courseId={}&jclassId={}'.format(
				courseid, classid), headers=self.headers, verify=False)
		res = re.findall(re_rule, r.text)
		# sign_type = re.findall(sign_type_re_rule, r.text)
		# print(sign_type)
		if res != []:  # 满足签到条件
			return {
				'classid': classid,
				'courseid': courseid,
				'activeid': res[0][0],
				'classname': classname,
				'sign_type': res[0][1]
			}

	def general_sign(self, classid, courseid, activeid):
		"""普通签到"""
		r = self.session.get(
			'https://mobilelearn.chaoxing.com/widget/sign/pcStuSignController/preSign?activeId={}&classId={}&fid=39037&courseId={}'.format(
				activeid, classid, courseid), headers=self.headers, verify=False)
		title = re.findall('<title>(.*)</title>', r.text)[0]
		if "签到成功" not in title:
			# 网页标题不含签到成功，则为拍照签到
			return self.tphoto_sign(activeid)
		else:
			sign_date = re.findall('<em id="st">(.*)</em>', r.text)[0]
			s = {
				'date': sign_date,
				'status': title
			}
			return s

	def hand_sign(self, classid, courseid, activeid):
		"""手势签到"""
		hand_sign_url = "https://mobilelearn.chaoxing.com/widget/sign/pcStuSignController/signIn?&courseId={}&classId={}&activeId={}".format(
			courseid, classid, activeid)
		r = self.session.get(hand_sign_url, headers=self.headers, verify=False)
		title = re.findall('<title>(.*)</title>', r.text)
		sign_date = re.findall('<em id="st">(.*)</em>', r.text)[0]
		s = {
			'date': sign_date,
			'status': title
		}
		return s

	def qcode_sign(self, activeId):
		"""二维码签到"""
		params = {
			'name': '',
			'activeId': activeId,
			'uid': '',
			'clientip': '',
			'useragent': '',
			'latitude': '-1',
			'longitude': '-1',
			'fid': '',
			'appType': '15'
		}
		res = self.session.get('https://mobilelearn.chaoxing.com/pptSign/stuSignajax', params=params)
		s = {
			'date': time.strftime("%m-%d %H:%M", time.localtime()) ,
			'status': res.text
		}
		return s

	def addr_sign(self, activeId):
		"""位置签到"""
		params = {
			'name': '',
			'activeId': activeId,
			'address': '中国',
			'uid': '',
			'clientip': '0.0.0.0',
			'latitude': '-2',
			'longitude': '-1',
			'fid': '',
			'appType': '15',
			'ifTiJiao': '1'
		}
		res = self.session.get('https://mobilelearn.chaoxing.com/pptSign/stuSignajax', params=params)
		s = {
			'date': time.strftime("%m-%d %H:%M", time.localtime()),
			'status': res.text
		}
		return s

	def tphoto_sign(self, activeId):
		"""拍照签到"""
		params = {
			'name': '',
			'activeId': activeId,
			'address': '中国',
			'uid': '',
			'clientip': '0.0.0.0',
			'latitude': '-2',
			'longitude': '-1',
			'fid': '',
			'appType': '15',
			'ifTiJiao': '1',
			'objectId': '5712278eff455f9bcd76a85cd95c5de3'
		}
		res = self.session.get('https://mobilelearn.chaoxing.com/pptSign/stuSignajax', params=params)
		print(res.text)
		s = {
			'date': time.strftime("%m-%d %H:%M", time.localtime()),
			'status': res.text
		}
		return s

	def sign_in(self, classid, courseid, activeid, sign_type):
		"""签到类型的逻辑判断"""
		if self.check_activeid(activeid):
			return
		if "手势" in sign_type:
			# test:('拍照签到', 'success')
			return self.hand_sign(classid, courseid, activeid)

		elif "二维码" in sign_type:
			return self.qcode_sign(activeid)

		elif "位置" in sign_type:
			return self.addr_sign(activeid)

		else:
			# '[2020-03-20 14:42:35]-[签到成功]'
			r = self.general_sign(classid, courseid, activeid)
			return r

	def sign_tasks_run(self):
		"""开始所有签到任务"""
		tasks = []
		sign_msg = {}
		final_msg = []
		# 获取所有课程的classid和course_id
		classid_courseId = self.get_all_classid()

		# 获取所有课程activeid和签到类型
		for i in classid_courseId:
			coroutine = self.get_activeid(i[1], i[0], i[2])
			tasks.append(coroutine)

		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		result = loop.run_until_complete(asyncio.gather(*tasks))

		for d in result:
			if d is not None:
				s = self.sign_in(d['classid'], d['courseid'], d['activeid'], d['sign_type'])
				if not s:
					return
				# 签到课程， 签到时间， 签到状态
				sign_msg = {
					'name': d['classname'],
					'date': s['date'],
					'status': s['status']
				}
				final_msg.append(sign_msg)
		return final_msg


def server_chan_send(msg):
	"""server酱将消息推送至微信"""
	desp = ''
	for d in msg:
		desp = '|  **课程名**  |   {}   |\r| :----------: | :---------- |\r'.format(d['name'])
		desp += '| **签到时间** |   {}   |\r'.format(d['date'])
		desp += '| **签到状态** |   {}   |\r'.format(d['status'])

	params = {
		'text': '您的网课签到消息来啦！！',
		'desp': desp
	}

	requests.get(server_chan['url'], params=params)


def local_run():
	# 本地运行使用
	if "activeid.txt" not in os.listdir("./"):
		with open(activeid_path, 'w+') as f:
			f.write("")
	s = AutoSign(user_info['username'], user_info['password'])
	result = s.sign_tasks_run()
	if result:
		if server_chan['status']:
			server_chan_send(result)
		return result
	else:
		return "暂无签到任务"


if __name__ == '__main__':
	print(local_run())
