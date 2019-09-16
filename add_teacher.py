import requests

# 登录url


lgn_url = 'http://localhost/admin.php?m=mgr/admin.chklogin&ajax=1'
lgn_data = {
    'username': 'admin',
    'password': 'admin',
}

data2 = requests.post(url=lgn_url, data=lgn_data)
# 获取的headers数据为字
cookies = data2.cookies['PHPSESSID']

# 添加教师接口
add_teacher_url = 'http://localhost/admin.php?m=mgr/member2.saveMemberInfo&id='

phpid = {
    'PHPSESSID': '{}'.format(cookies)
}

add_teacher_data = {
    'username':'13899999999',
    'realname':'nibaba',
    'password':'123456',
    'sex':'0',
    'roleid':'5',
    'orid1':'120',
    'email':'test001@test.com',
    'phone':'13899999999',
    'location_p':'河南省',
    'location_c':'信阳市',
    'location_a':'罗山县',
    'address':'yourhome',
    'introduce':'i am ',
    'type': '1'
}

result = requests.post(url=add_teacher_url, data=add_teacher_data, cookies=phpid)

print(result.text)
