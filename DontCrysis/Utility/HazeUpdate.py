#This file is for fusion table - Haze readings update

from httplib2 import Http
from oauth2client.client import SignedJwtAssertionCredentials
from googleapiclient.discovery import build

__author__ = 'Madhavan'

#def main():
    #HazeTable_Update(100,2)

def HazeTable_Update(psi_reading,rowid):
    import json

    client_email = '1067081748386-i94fl2104ima251p4u2s43so40pbncb3@developer.gserviceaccount.com'
    with open("CMSTest-5f1753f2f1a0.p12",'rb') as f:
      private_key = f.read()

    credentials = SignedJwtAssertionCredentials(client_email, private_key,
        'https://www.googleapis.com/auth/fusiontables',sub = 'smadhavan1995@gmail.com')
    http_auth = credentials.authorize(Http())
    #http = Http()

    query1 = "UPDATE 1nVmKmiLsJuRlddKUq0IlufonYZITi5tSYLMlAgMF SET PSI_Readings = " +str(psi_reading)+ " WHERE ROWID = '"+str(rowid)+"'"
    fusion = build('fusiontables', 'v2', http=http_auth)
    Response = fusion.query().sql(sql=query1)

    rep =  Response.execute()
    #print rep
    #print Response.execute().read();
    #sqladmin = build('drive', 'v2', http=http)
    #sqladmin.instances().list().execute();
    return
#if __name__ == "__main__":
  #main()