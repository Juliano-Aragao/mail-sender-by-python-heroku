import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>API Notificação</p>
    <p>Python mail - by Julian</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Acesso ao cadastro 2"
    msg['From'] = 'julianoesa@gmail.com'
    msg['To'] = 'julianoesa@gmail.com'
    password = 'zzzzzzzzzzzz'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
    
enviar_email()
