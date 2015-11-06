__author__ = 'Ankur Bansal'

from twilio.rest import TwilioRestClient

def sendsms(request,crisis):
    account_sid = "ACc483999731a8f2a33dcfa3eb467d170a"
    auth_token  = "013bc945f038ae51781b6a98d6943acc"

    client = TwilioRestClient(account_sid, auth_token)

    if(crisis.type==1):
        num = '+6596258220'
        message = 'There is a fire at pincode: %s with severity %d' %(crisis.postalcode,crisis.severity)
    elif(crisis.type==3):
        num = '+6594527250'
        message = 'There is a medical emergency at pincode: %s with severity %d' %(crisis.postalcode, crisis.severity)
    elif(crisis.type==4):
        num = '+6594203032'
        message = 'There is a gas leak at pincode: %s with severity %d' %(crisis.postalcode, crisis.severity)

    client.messages.create(body=message,
    to=num,
    from_="+13345813034",)
