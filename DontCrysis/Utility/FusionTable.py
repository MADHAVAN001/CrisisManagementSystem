#this function is for importing data into the fusion table for markers
__author__ = 'Madhavan'

from httplib2 import Http
from oauth2client.client import SignedJwtAssertionCredentials
from googleapiclient.discovery import build

#def main():
#    update("Fire",639811,"Earthquake",639811)

def insert(name_event,postcode):
    #import json

    client_email = '1067081748386-i94fl2104ima251p4u2s43so40pbncb3@developer.gserviceaccount.com'
    with open("CMSTest-5f1753f2f1a0.p12",'rb') as f:
      private_key = f.read()

    credentials = SignedJwtAssertionCredentials(client_email, private_key,
        'https://www.googleapis.com/auth/fusiontables',sub = 'smadhavan1995@gmail.com')
    http_auth = credentials.authorize(Http())
    #http = Http()
    event = "Fire"
    query1 = "INSERT INTO 1lrwBUW2WdOCgC-BRr8qG9jmSgjYOF7lBPt3xKQfr(Event,Location) VALUES('" + name_event + "',"+str(postcode)+")"
    fusion = build('fusiontables', 'v2', http=http_auth)
    Response = fusion.query().sql(sql=query1)

    rep =  Response.execute()
    #print Response.execute().read();
    #sqladmin = build('drive', 'v2', http=http)
    #sqladmin.instances().list().execute();
    return

def update(old_name_event,old_postcode,new_name_event,new_postcode):
    client_email = '1067081748386-i94fl2104ima251p4u2s43so40pbncb3@developer.gserviceaccount.com'
    with open("CMSTest-5f1753f2f1a0.p12",'rb') as f:
      private_key = f.read()

    credentials = SignedJwtAssertionCredentials(client_email, private_key,
        'https://www.googleapis.com/auth/fusiontables',sub = 'smadhavan1995@gmail.com')
    http_auth = credentials.authorize(Http())
    #http = Http()
    query1 = "SELECT rowid FROM 1lrwBUW2WdOCgC-BRr8qG9jmSgjYOF7lBPt3xKQfr WHERE Event = '"+old_name_event+"' AND Location = "+str(old_postcode)
    fusion = build('fusiontables', 'v2', http=http_auth)
    Response = fusion.query().sql(sql=query1)

    rep =  Response.execute()
    #print rep['rows'][0][0]
    rowid = rep['rows'][0][0]
    query2 = "UPDATE 1lrwBUW2WdOCgC-BRr8qG9jmSgjYOF7lBPt3xKQfr SET Event = '"+new_name_event+"', Location = "+str(new_postcode)+" WHERE rowid = '"+str(rowid)+"'"
    Response2 = fusion.query().sql(sql=query2)
    rep2 =  Response2.execute()
    #print rep2;
    #print Response.execute().read();
    #sqladmin = build('drive', 'v2', http=http)
    #sqladmin.instances().list().execute();
    return

def delete(name_event,postcode):
    client_email = '1067081748386-i94fl2104ima251p4u2s43so40pbncb3@developer.gserviceaccount.com'
    with open("CMSTest-5f1753f2f1a0.p12",'rb') as f:
      private_key = f.read()

    credentials = SignedJwtAssertionCredentials(client_email, private_key,
        'https://www.googleapis.com/auth/fusiontables',sub = 'smadhavan1995@gmail.com')
    http_auth = credentials.authorize(Http())
    #http = Http()
    query1 = "SELECT rowid FROM 1lrwBUW2WdOCgC-BRr8qG9jmSgjYOF7lBPt3xKQfr WHERE Event = '"+name_event+"' AND Location = "+str(postcode)
    fusion = build('fusiontables', 'v2', http=http_auth)
    Response = fusion.query().sql(sql=query1)

    rep =  Response.execute()
    #print rep['rows'][0][0]
    rowid = rep['rows'][0][0]
    query2 = "DELETE FROM 1lrwBUW2WdOCgC-BRr8qG9jmSgjYOF7lBPt3xKQfr WHERE rowid = '"+str(rowid)+"'"
    Response2 = fusion.query().sql(sql=query2)
    rep2 =  Response2.execute()
    print rep2;
    #print Response.execute().read();
    #sqladmin = build('drive', 'v2', http=http)
    #sqladmin.instances().list().execute();
    return

#if __name__ == "__main__":
#  main()