#import requests
import pytz,datetime
from simple_salesforce import Salesforce
from Include.config import sb_user
                            #, pd_user

end = datetime.datetime.now(pytz.UTC) # UTC for SF API

sb_sf = Salesforce(
    username=sb_user["username"],
    password=sb_user["password"],
    security_token=sb_user["security_token"],
    instance_url=sb_user["instance_url"],
    domain=sb_user["domain"]
)

sf.Contact.create({'LastName':'McTesterson', 'FirstName': 'Testy', 'Email':'example@example.com', 'Person_Type__c' : "Customer"})
