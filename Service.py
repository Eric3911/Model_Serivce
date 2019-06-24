from flask import Flask,request,Response,jsonify
from PIL import Image
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Vehicletype', methods=['POST'])

def Vehicletype():

    # import logging
    # logger = logging.getLogger(__name__)
    # logger.setLevel(level=logging.INFO)
    # handler = logging.FileHandler("log.txt")
    # handler.setLevel(logging.INFO)
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)

    data = request.form.getlist('photo')
    #print len (data)
    #print  "the length of data received",len(data[0])
    # if str(data )=='[]'or len (str(data ))==0:
    #     logger.info ("you should not post empty data!")

    # #print data[0]
    # print data[0][0:500]
    #
    # fout = open('d:\\1a\\receice.txt', 'w')
    # fout.write(data[0])
    # fout.close()

    # data[0] = data[0].replace(" ", "")
    #
    # fout = open('d:\\1a\\remove.txt', 'w')
    # fout.write(data[0])
    # fout.close()

    #data[0]=data[0].replace("\n", "")

    # fout = open('d:\\1a\\receice.txt', 'w')
    # fout.write(data[0])
    # fout.close()

    # missing_padding = 4 - len(data[0]) % 4
    # if missing_padding:
    #     data[0] += b'=' * missing_padding
    import base64
    ori_image_data = base64.b64decode(str(data[0]))
    print ("####################")
    #print (ori_image_data)
    # try:
    #     ori_image_data = base64.b64decode(str(data[0]))
    # except :
    #     logger.info("please make sure your base64 encoding is right")

    b=b""
    #print (type (b))
    b= bytes(ori_image_data)

    byarr = bytearray(b)
    import os
    #receive = os.path.abspath('')+"/photo/"+'receive.jpg'
    receive = "receive.jpg"
    print (receive)
    fout = open(receive, 'wb')
    #print type(byarr)
    fout.write(byarr)
    fout.close()
    import cv2
    #Original = cv2.imread(receive)
    Original = Image.open(receive)

    from yolo import service_detect



    import json
    json_str =service_detect(Original)
    # json_str = json.dumps(photos)
    #print "json:", json_str

    # fout = open('d:\\1a\\test.txt', 'w')
    # fout.write(json_str)
    # fout.close()

    #print json_str
    return json_str
    #return Response(json.dumps(photos), mimetype='application/json')

if __name__ == '__main__':
    #f = open('.\configure\configure.txt', 'r')
    #Port = f.readline().strip('\n')
    #app.run(host='0.0.0.0',port = int(Port))
    app.run(host='0.0.0.0', port=int(3000))