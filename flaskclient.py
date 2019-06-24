import requests
import cv2

import base64
with open("/home/xl/1/1.jpg", 'rb') as fin:

    image_data = fin.read()
    base64_data = base64.b64encode(image_data)

    # fout = open('d:\\1a\\base64_content.txt', 'w')
    # fout.write(base64_data.decode())
    # fout.close()

user_info = {'photo': base64_data}
#user_info = {'photo': 'asasd'}
#print type(user_info)
r = requests.post("http://192.168.218.57:3000/Vehicletype", data=user_info)
print (r.text)
#print r.text
# print type(r)
# print type(r.text)
# print r.text
# print type (r.text)
import json
#
#
#
# json_str = json.dumps(r.text)
# print "json:",json_str
# print r.text
# print type (r.text)
#jd = json.loads(r.text)

# for name in jd:
#     #print name
#     #print ("hihi")
#     #print name
#     #print type (name)
#     pname= name.pop("name")
#     #print pname
#     pdata = name.pop("content")
#     import base64
#     ori_image_data = base64.b64decode(pdata)
#     fout = open('D:\\13\\'+pname, 'wb')
#     fout.write(ori_image_data)
#     fout.close()

#
# fout = open('d:\\1a\\test.txt', 'w')
# fout.write(r.text)
# fout.close()
