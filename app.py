from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Looking to send emails in production? Check out our Email API/SMTP product!
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'c8c8e5aa6095ff'
app.config['MAIL_PASSWORD'] = '161da9b507e2d0'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'default@gmail.com'  # <-- user email will be here , Link HTMl PAGE

mail = Mail(app)

@app.route("/")
def index():
    recipient = ["backendrunner2@gmail.com"]
    subject = "Test Mail"
    message_body = "Come to Gym ASAPPPPPPPPP............"

    msg = Message(subject=subject, recipients=recipient)
    msg.body = message_body

    try:
        mail.send(msg)
        return "Mail sent successfully"
    except Exception as e:
        return "Error sending email: " + str(e)

if __name__ == '__main__':
    app.run(debug=True)
