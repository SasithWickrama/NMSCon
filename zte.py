import traceback
import requests
from log import getLogger
import xml.etree.ElementTree as ET

logger = getLogger('zte', 'logs/zte')
urlString = "http://10.64.73.49:9090/axis2/services/NeManagementService/";


class Zte:
    def zte(self, indata):

        try:
            xmlfile = open('files/' + self, 'r')
            data = xmlfile.read()


            for key in indata:

                value = indata[key]
                data = data.replace(key,value)

                print(key, value)

            print(data)
            response = requests.request("POST", urlString,
                                        data=data)

            #print(response.request.body)
            #print("============================================")
            #print(response.text)
            
            logger.info("Start : =========================================================================")
            logger.info(response.request.body)
            logger.info("Response : =================================")
            logger.info(response.text)
            logger.info("End   : =========================================================================")
            count=1
            data={}
            root = ET.fromstring(response.content)
            
            for resultc in root.iter('statusCode'):
                ResultCode = resultc.text

            for resultd in root.iter('statusDesc'):
                ResultDesc = resultd.text
            print(ResultCode)  
            print(ResultDesc)            
                
            for movie in root.iter('record'):
                count=count+1
                for param in movie.iter('param'):
                    count=count+1
                    for name in param.iter('name'):
                        if(name.text != 'totalrecord') : 
                            count=count+1  
                            name= name.text        
                            for value in param.iter('value'):
                                if  count == 3 :
                                    value=value.text
                                    if value == 'IPTV':
                                        data[value]=value2                                    
                                    
                                if  count == 4 :
                                    value2=value.text 

                                count=1     
            
            
            print(data)
                    
                

        except Exception as e:
            print("Exception : %s" % traceback.format_exc())
