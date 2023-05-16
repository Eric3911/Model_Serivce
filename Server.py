from io import BytesIO
import tornado
import tornado.ioloop
import tornado.web
import os
import json
import json.decoder
from PyPDF2 import PdfFileMerger
from ocr_pdf_text_main import pyMuPDF_fitz


class Handler(tornado.web.RequestHandler):
    def post(self):
        pdf_file = self.request.files.get('file', None)
        print('1:', pdf_file)
        pdf_file = BytesIO(pdf_file[0].body)
        # print('2:', pdf_file)

        pdf_merger = PdfFileMerger()
        pdf_merger.append(pdf_file)
        output = open('C:/Users/86183/Desktop/TOCR/00123.pdf', "wb")
        pdf_merger.write(output)
        output.close()
        pdfpath = os.path.join(os.getcwd(), "C:/Users/86183/Desktop/TOCR/")
        pdfPath = os.path.join(pdfpath, "00123.pdf")
        imagePath ='C:/Users/86183/Desktop/TOCR/'

        # TODO 此处调用算法接口
        PDF_res = pyMuPDF_fitz(pdfPath, imagePath)
        # print(PDF_res)
        self.finish(json.dumps(str(PDF_res)))
        print(type(PDF_res))


class ImageServer(object):
    def __init__(self, port):
        self.port = port

    def process(self):
        app = tornado.web.Application([(r"/pdfOCR", Handler)], )
        app.listen(self.port)
        tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    server_port = "8089"
    server = ImageServer(server_port)
    print("begin server")
    server.process()