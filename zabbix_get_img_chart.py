import requests
import time
from io import BytesIO
from PIL import Image

# time now
timestamp_now = time.time()

# parameters login
URL = 'http://127.0.0.1:36081'
URL_LOGIN = '{}/index.php?login=1'.format(URL)
USER = 'username'
PASSWORD = 'password'
PARAMETERS_URL = {'name': USER, 'password': PASSWORD, 'enter':'Sign in', 'autologin':'1', 'request':''}

# parameters url
width = '1300'
height = '300'
stime = '20170522112858'    # time init optional
itemids = '25436'
type_chart = '0'    # type of chart 0(lineal) or 1(area)
updateProfile = '1'
profileIdx = 'web.item.graph'
profileIdx2 = itemids
curtime = format(timestamp_now, '.3f')  # time finish
url_chart = '{URL}/chart.php?&itemids={itemids}&type={type_chart}\
            &updateProfile={updateProfile}&profileIdx=web.item.graph\
            &profileIdx2={profileIdx2}\&width={width}&height={height}&screenid=\
            &curtime={curtime}'.format(URL=URL, stime=stime, itemids=itemids,
                type_chart=type_chart, updateProfile=updateProfile,
                profileIdx2=profileIdx2, curtime=curtime, width=width, height=height)

request1 = requests.post(URL_LOGIN, data=PARAMETERS_URL)
request2 = requests.get(url_chart, cookies=request1.cookies)

img = Image.open(BytesIO(request2.content))
width, height = img.size
img.save('nameChart.jpg')