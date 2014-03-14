# Simple script to check if a website is being filtered by Sophos Web Appliance and send email if not.
#
# Credit for most of code was based on this: http://stackoverflow.com/questions/17152296/different-results-with-python-requests-module-and-curl
# Sendmail code is base on this: http://stackoverflow.com/questions/73781/sending-mail-via-sendmail-from-python
#

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

