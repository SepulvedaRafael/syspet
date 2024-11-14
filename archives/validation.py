# CELULAR
from twilio.rest import Client

# EMAIL
import re
import smtplib
from random import randint
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# CEP
import brazilcep

# DATA
from datetime import datetime

def isnome(self):
    if(len(self) != ''):
        return True
    else:
        return False

def issexo(self):
    if len(self) != 0 and self == "Masculino" or self == "Feminino":
        return True
    else:
        return False


def iscpf(self):
    self = str(self)
    if len(self) == 11:
        if self.count(self[0]) == 11:
            return False
        else:
            first_digit = 0
            second_digit = 0
            # Validação do primeiro digíto - #
            for i in range(0, len(self) - 2):
                first_digit += int(self[i]) * (10 - i)  # Multiplicação dos 9 primeiros
            first_digit = first_digit * 10 % 11
            # Validação do segundo dígito - ##
            for i in range(0, len(self) - 1):
                second_digit += int(self[i]) * (11 - i)
            second_digit = second_digit * 10 % 11

            # Validação final
            if first_digit == int(self[9]) and second_digit == int(self[10]):
                return True
            else:
                return False
    else:
        return False


def iscelular(self):
    self = str(self)
    if len(self) == 11:
        account_sid = "ACa624bd6725dc418bb5bbb8279cb23e63"
        auth_token = "89cc3e466d137ff7b8bae40cdcddfd21"

        cliente = Client(account_sid, auth_token)

        try:
            code = randint(100000, 999999)
            print(code)
            cliente.messages.create(
                from_="+12569523515",
                to=f"+55{int(self)}",
                body=f"""
					Mensagem de confirmação
					{code}
				""",
            )
            print("Enviado com sucesso!")
            coderecebido = int(input("Code recebido: "))
            if coderecebido == code:
                return True
            else:
                print("Código inválido!")
        except Exception as e:
            print(f"Erro ao enviar o código: {e}")
    else:
        return False


def isemail(self):
    # Validação simples e limitada
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    if re.fullmatch(regex, self):
        # Setup email remetente + senha
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        remetente = "shadow83951@gmail.com"
        senha_remetente = "xuuy qhnf mshs zbtt"

        # Mensagem
        msg = MIMEMultipart()
        msg["Subject"] = "Email de confirmação"
        msg["From"] = remetente
        msg["To"] = self
        code = randint(100000, 999999)
        print(code)
        mensagem = f"""
			Mensagem de confirmação
			{code}
		"""

        msg.attach(MIMEText(mensagem, "plain"))

        # Enviando mensagem
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(remetente, senha_remetente)

            server.sendmail(remetente, self, msg.as_string())
            print("Enviado com sucesso!")
            coderecebido = int(input("Code recebido: "))
            if coderecebido == code:
                return True
            else:
                print("Código inválido!")
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

        finally:
            server.quit()
    else:
        return False


def iscep(self):
    if len(self) == 8:
        endereco = brazilcep.get_address_from_cep(f"{self}")

        return (endereco, True)
    else:
        return False


def issenha(self):
    # Critérios:
    # 1. Deve ter de 8 a 32 caracteres
    # 2. Deve ter, no mínimo, uma letra maiúscula, uma letra minúscula, um número  e um caractere especial (!#@$%&)
    regex = r"^(?=.*[A-Z])(?=.*[!#@$%&])(?=.*[0-9])(?=.*[a-z]).{8,32}$"

    if re.fullmatch(regex, self):
        return True
    else:
        return False

def iscategoria(self):
    self = self.lower()
    if(self != ''):
        categorias = ('bovino','canino','felino', 'ave')

        if(self in categorias):
            return True
        else:
            return False
    else:
        return False

def israca(self):
    if(self != ''):
        return True
    else:
        return False

def isdataNascimento(self):
    if(self != ''):
        dia, mes, ano = self.split('/')
        if(len(dia) > 0 and len(dia) <= 2 and len(mes) > 0 and len(mes) <= 2 and len(ano) > 0 and len(ano) <= 4):
            return True
        else:
            return False
    else:
        return False

def checkString(self):
    if(len(self) != ''):
        return True
    else:
        return False

def transformValue(self):
    if(len(self) != ''):
        self = int(self)
        return self
    else:
        return False

def isdata(self):
    if(self != ''):
        data_atual = datetime.today()
        data_em_texto = data_atual.strftime('%d/%m/%Y')
        return True if self >= data_em_texto else False
    else:
        return False