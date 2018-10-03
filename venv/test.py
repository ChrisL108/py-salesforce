#import requests
import pytz,datetime, pandas as pd
from pandas import DataFrame
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

def SOQL(SOQL):
    qry = sb_sf.query(SOQL)
    print(f"Record Count {qry['totalSize']}")
    isDone = qry['done']

    if isDone == True:
        df = DataFrame(qry['records'])

    while isDone != True:
        try:
            if qry['done'] != True \
            and qry['records']['name'] != "None":
                df = df.append(DataFrame(qry['records']))
                qry = sb_sf.query_more(qry['nextRecordsUrl'], True)
            else:
                df = df.append(DataFrame(qry['records']))
                isDone = True
                print('Complete.')
                break
        except NameError:
            df = DataFrame(qry['records'])
            qry = sb_sf.query_more(qry['nextRecordsUrl'], True)

    df = df.drop('attributes', axis=1)
    return df

#sb_sf.Contact.create({'LastName':'McTesterson', 'FirstName': 'Testy', 'Email':'example@example.com', 'Person_Type__c' : "Customer"})
#tester = sb_sf.query("SELECT Id, Email FROM Contact WHERE LastName = 'McTesterson'")
#df = pd.DataFrame(tester['records'], columns=tester['records'].keys())
#test = SOQL("SELECT Id, Name, site_descriptor__c FROM Order")

