import re
import sys
import json
from huawei import Huwwei
from zte import Zte
from nokia import Nokia

data = json.loads(re.sub('\'', '\"', sys.argv[3]))

#print(data)
#print(data['SubscriptionId'])
#print(data['Quantity'])

if sys.argv[1] == 'HUAWEI':
    result = Huwwei.huawei(sys.argv[2], data)


elif sys.argv[1] == 'ZTE':
    result = Zte.zte(sys.argv[2], data)


elif sys.argv[1] == 'NOKIA':
    result = Nokia.nokia(sys.argv[2], data)

else:
    print('Invalid MSAN')
