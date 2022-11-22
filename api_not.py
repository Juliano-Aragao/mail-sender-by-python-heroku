import smtplib
import email.message
import requests

#pegar api de notificação 

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dicionario = requisicao.json()

print(requisicao)
print(requisicao.json())

cotacao = float(requisicao_dicionario['USDBRL']['bid'])
print(20*"#")
print(cotacao)

#logica de envio de e-mail



def enviar_email(cotacao):  
    corpo_email = f"""
    <p>API Notificação</p>
    <p> Information log controll<p/>
     <p>API Notificação number {cotacao}</p>
    <p>Python mail - by Julian</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Acesso ao cadastro 2"
    msg['From'] = 'julianoesa@gmail.com'
    msg['To'] = 'julianoesa@gmail.com'
    password = 'busylacolsauaode'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
    
    
if cotacao  < 5.40 :  
    enviar_email(cotacao)
    
    
# deploy - heroku    