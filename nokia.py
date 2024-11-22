import traceback

from log import getLogger

logger = getLogger('nokia', 'logs/nokia')
urlString = "http://172.25.37.96:8080/soap/services/ApcRemotePort/9.6";

class Nokia:
    def nokia(self, data):
        try:
            xmlfile = open('files/'+self, 'r')
            body = xmlfile.read()

            print('nokia')

        except Exception as e:
            print("Exception : %s" % traceback.format_exc())
