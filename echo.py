import datetime
import logging
from zeep import Client
from zeep.wsse.username import UsernameToken
from zeep.wsse.utils import WSU
from zeep.plugins import HistoryPlugin

history = HistoryPlugin()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('zeep.transports')
logger.setLevel(logging.DEBUG)

timestamp_token = WSU.Timestamp()
today_datetime = datetime.datetime.today()
expires_datetime = today_datetime + datetime.timedelta(minutes=10)
timestamp_elements = [
    WSU.Created(today_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")),
]

timestamp_token.extend(timestamp_elements)
# user_name_token = UsernameToken('abc', 'def', timestamp_token=timestamp_token)
user_name_token = UsernameToken('westminsteruser1', 'W3Rf8HnBy47f', use_digest=False, timestamp_token=timestamp_token)

wsdl = 'https://trgcisweb.veolia.co.uk/CISServices/WasteService.svc?wsdl'

client = Client(wsdl, wsse=user_name_token)

try:
    response = client.service.GetServices()
    print(response)
except Exception as e:
    print("An error occurred:", str(e))
