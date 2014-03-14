import requests
import pprint
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

msg = MIMEText("The Sophos Filter is not functioning correctly!")
msg["From"] = "brad.zima@nilesschools.org"
msg["To"] = "brad.zima@nilesschools.org"
msg["Subject"] = "Sophos Filter Error"

url = 'http://sophostest.com/hacking/index.html'
res = requests.get(url, allow_redirects=False)

print 'status_code: ', res.status_code
print 'response_url: ', res.url
print 'headers: '
pprint.pprint(res.headers)
print 'history: ', res.history

if(res.status_code == requests.codes.ok):
		p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
		p.communicate(msg.as_string())

