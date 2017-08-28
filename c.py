from urllib import request, parse

login_data = parse.urlencode(
    [('username', 'admin'),
     ('password', 'ccc'),
     ('college_name', '广东职业技术学院')
     ]
)
req = request.Request('http://api.szmatch.zxlab.cn:17328/login')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Data:%s' % f.read().decode('utf-8'))
