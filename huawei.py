import traceback

from log import getLogger


logger = getLogger('huawei', 'logs/huawei')
url = "http://huaweincefanoss.intranet.slt.com.lk:30102/wsdl";

class Huwwei:
    def huawei(self, data):

        try:
            xmlfile = open('files/'+self, 'r')
            body = xmlfile.read()

            print('huawei')

        except Exception as e:
            print("Exception : %s" % traceback.format_exc())
