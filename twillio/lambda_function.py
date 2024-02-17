import os
import json
from twilio.rest import Client
import boto3

DYNAMODB_TABLE ="XXX";
deviceID = 'XXX'
REGION_NAME = "XXX" #Region

def lambda_handler(event, context):
    print(event)
    from_number = os.environ['FROM_NUMBER']
    destination_number = os.environ['TO_NUMBER']
    h = json.dumps(event)
    k = json.loads(h)
    message = k['Records'][0]['dynamodb']
    #message = json.loads(event['Records'][0]['dynamodb'])
    #message = json.loads(event['Records'][0]['AlarmeHe1'])
    #json.loads(event['Records'][0]['Sns']['Message'])
    notification_composer(message,from_number, destination_number)
    print(message)


def notification_composer(message,from_number, destination_number):

    #state = message["detail"]["state"]
    #instanceId = message["detail"]["instance-id"]
    
    if message != None and 'Track_AlarmeHe1' in message["NewImage"]:
        subject = "Alteração Alarme de Pressão de Hélio 1"
        Ux = int(message["NewImage"]["Ux"]["N"])
        alarme = message["NewImage"]["AlarmeHe1"]["S"]
        data = message["NewImage"]["DataConectado"]["S"]
        hora = message["NewImage"]["HoraConectado"]["S"]
        pressao_atual = message["NewImage"]["Pressao_He1"]["N"]
        message_body = f"🚨*Atenção!*🚨 \n\n Olá Aline, aqui é a TariX.\n\nNote que, a pressão de alarme foi alterada para  *{alarme}* bar . \n\nA pressão atual do seu cilindro é de *{pressao_atual}* bar."
    
    elif message != None and 'Disparo_AlarmeHe1_v1' in message["NewImage"]:
        subject = "Alerta de Baixa Pressão Cilindro Hélio 1"
        Ux = int(message["NewImage"]["Ux"]["N"])
        alarme = (message["NewImage"]["AlarmeHe1"]["S"])
        data = message["NewImage"]["DataAlarme"]["S"]
        hora = message["NewImage"]["HoraAlarme"]["S"]
        troca = message["NewImage"]["PrevisaoDeTroca"]["S"]
        pressao_atual = (message["NewImage"]["Pressao_He1"]["S"])
        message_body = f"🚨*Atenção!*🚨 \n\n Olá Aline, aqui é a TariX.\n\nNote que, a pressão do seu cilindro de Hélio chegou no limite de apenas 10% superior do que a pressão de alarme especificado. \n\nPressão atual cilindro de Hélio 1: *{pressao_atual}* bar. \n\n Pressão de Alarme: *{alarme}* bar. \n\nTempo Estimado até a finalização do cilindro: *{troca}* dias."
       
    
    
    elif message != None and  'FORNECEDOR_GASES' in message["NewImage"]:
        
        subject = "Alteração do Fornecedor de Hélio 1"
        Ux = int(message["NewImage"]["Ux"]["N"])
        fornecedor_de_gases = message["NewImage"]["FORNECEDOR_GASES"]["S"] 
        data = message["NewImage"]["DATAX"]["S"]
        hora = message["NewImage"]["HORA"]["S"]
        gases_id = message["NewImage"]["idGas"]["S"]
        message_body = f"🚨*Atenção!*🚨 \n\n Olá Aline, aqui é a TariX.\n\nNote que, o seu fornecedor de gases para *{gases_id}* foi alterado para  *{fornecedor_de_gases}* . \n\n A data e hora da alteração foi *{data}* às *{hora}*."
        
    elif message != None and  'FORNECEDOR_INSTALACAO' in message["NewImage"]:
        
        subject = "Alteração do Fornecedor da Instalação de Gases"
        Ux = int(message["NewImage"]["Ux"]["N"])
        fornecedor_instalacao = message["NewImage"]["FORNECEDOR_INSTALACAO"]["S"] 
        data = message["NewImage"]["DATAX"]["S"]
        hora = message["NewImage"]["HORA"]["S"]
        gases_id = message["NewImage"]["idGas"]["S"]
        message_body = f"🚨*Atenção!*🚨 \n\nOlá Aline, aqui é a TariX. \n\nNote que, o seu fornecedor da instalação de gases para *{gases_id}* foi alterado para  *{fornecedor_instalacao}* . \n\nA data e hora da alteração foi *{data}* às *{hora}*."
        
    insertRegistry(deviceID, Ux, subject, message_body, data, hora)    
    send_whatsapp_message(message_body, from_number, destination_number)

def send_whatsapp_message(message_body, from_number, destination_number):
    #Credenciais e parametros Twilio
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages.create( 
                                  from_=from_number,
                                  body=message_body,
                                  to=destination_number
                              )
    print(f"Mensagem enviada para {destination_number} com sucesso! ID Twilio: " + message.sid)
    
    """ Dynamodb functions """


def insertRegistry(deviceID, Ux, subject , message_body, data, hora):
    dynamodb = boto3.resource('dynamodb', region_name=REGION_NAME)
    table = dynamodb.Table(DYNAMODB_TABLE)
    response = table.put_item(
        Item={
            'deviceID': deviceID,
            'Ux': Ux,
            'subject' : subject,
            'message_TariX': message_body,
            'data': data,
            'hora': hora,
        }
    )
    print(f"Registro inserido na Tabela *{DYNAMODB_TABLE}* com sucesso! {response}")