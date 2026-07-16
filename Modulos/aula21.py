import os
import pathlib
from dotenv import load_dotenv
import string
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

#CAMINHO ARQUIVO HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula21.html'

#DADOS DO REMETENTE e DESTINATARIO
remetente = os.getenv('FROM_EMAIL', '')
destinarario = remetente

#CONFIGURAÇÔES SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

#MENSAGEM DE TEXTO

with open(CAMINHO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read()
    template = string.Template(texto_arquivo)
    texto_email = template.substitute(nome='Lucas')

#TRANSFORMAR NOSSA MENSAGEM EM  MIMEMultipart

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to']= destinarario
mime_multipart['subject'] = 'Este é o Assunto do E-mail'#ASSUNTO DO EMAIL


corpo_email = MIMEText(texto_email, 'html', 'utf-8')

mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-MAIL enviado com sucesso!')