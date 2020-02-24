from twilio.twiml.messaging_response import MessagingResponse


def check_module_status():
    '''
    Check all connections are working and return back report in message.
    This will be called daily at an set time during the day as a standard
    report helping with maintenance.
    '''
    return "checking device"


def water_plants():
    '''
    Check soil moisture. if needed to be watered then allow to be watered,
    if soil is at perfect level then allow user to over write and water plants
    but give warning.
    Runs auto every day
    '''
    # print(req)
    water_plants_msg = "i shall water the plants now"
    resp = MessagingResponse()

    resp.message("water n dat")
    return str(resp)


def water_tracker():
    '''
    water tracker send a time stamped with soil and light readings to mongoDB
    this is for easy tracking / if needed to stats then its implemented
    '''
    return "tracking your plants to mongo"


def temp_humidity_check():
    '''
    check the temp and humidity and sends me an update with temp and humidty
     of the plants / environment
    '''
    return "telling you the temp and humidity"


def picture_plants():
    '''
    just takes a picture of the plants and send to me.
    can se set up auto 1 week intivals and added to gridfs to track progress
    '''
    return "sending you some plant pics"


def shutdown():
    '''
    kills the process but will be warned/ could be used the restart things

    '''
    return "are you sure about that"
