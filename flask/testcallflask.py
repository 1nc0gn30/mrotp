from flask import Flask, Response

app = Flask(__name__)

@app.route('/voice.xml', methods=['GET', 'POST'])
def voice():
    twiml = '<?xml version="1.0" encoding="UTF-8"?><Response><Say>Hello, this is a test Twilio voice call.</Say></Response>'
    response = Response(twiml, mimetype='application/xml')
    return response

if __name__ == '__main__':
    app.run(debug=True)
