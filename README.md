# 🐶 Syspet

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/PYTHON-000000?style=for-the-badge&logo=python&logoColor=facc56" alt="Python"></a>
<a href="https://www.twilio.com/docs"><img src="https://img.shields.io/badge/TWILIO-000000?style=for-the-badge&logo=twilio&logoColor=f42a43" alt="Twilio"></a>
<a href="https://github.com/Textualize/rich/"><img src="https://img.shields.io/badge/RICH-000000?style=for-the-badge&logo=rich&logoColor=b8ab36" alt="Rich"></a>
<a href="https://pypi.org/project/Unidecode/"><img src="https://img.shields.io/badge/UNIDECODE-000000?style=for-the-badge&logo=unicode&logoColor=5088ea" alt="Unidecode"></a>
<a href="https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br/"><img src="https://img.shields.io/badge/.ENV-000000?style=for-the-badge&logo=dotenv&logoColor=ebd33c" alt="Dotenv"></a>

Esse projeto foi um desafio realizado pelo professor Cristiano Souza da Universidade Paulista, com a finalidade de ensinar a metodologia CRUD, Python e mostrar o potencial da linguagem junto a suas bibliotecas.

Aqui foi possível entender mais sobre a criação de interfaces **CRUD** - *Create, Read, Update and Delete* -, como também os cálculos por trás da verificação do **Cadastro de Pessoa Física (CPF)**, o envio de mensagens de confirmação via celular e email pela plataforma **TWILIO** e o protocolo **SMTP**, respectivamente.

Apesar de faltar vários mecanismos de segurança e implementações necessárias para torná-lo um projeto pessoal técnico, foi uma das melhores experiências de aprendizagem que me propus a dedicar meu tempo e entender profundamente cada estrutura para resolver o problema proposto.

## 💻 Pré-requisitos
Para testar esse projeto, verifique se você possui todos os requisitos:

- Você possui instalado uma versão estável da linguagem `python`.
- Você possui instalado um ambiente de desenvolvimento, como `Visual Studio Code` ou outro de sua preferência.
- Certifique-se de possuir todas as dependências que coincidirem com a sua opção de estudo. Caso contrário, verifique a seção `🚀 Instalando as dependências`.

## 🚀 Instalando as dependências
O Syspet utiliza algumas dependências que são fundamentais para o seu funcionamento, por isso certifique-se de instalar cada uma delas para que o programa funcione normalmente.

*Rich*
```
pip install rich
```

*Unidecode*
```
pip install unidecode
```

*Twilio*
```
pip install twilio
```

*Dotenv*
```
pip install python-dotenv
```

*BrazilCEP:*
```
pip install brazilcep
```

> [!IMPORTANT]
> Para que o Twilio funcione, é necessário criar uma conta e ter um .env com: SID_TWILIO, AUTH_TOKEN_TWILIO, NUMBER_TWILIO, REMETENTE_EMAIL, REMETENTE_PASSWORD. Essa configuração é necessária para que o envio do código de confirmação via email e via celular seja feito.

> [!NOTE]
> Para não utilizar a senha original da conta email disponibilizada, utilize o mecanismo de [Senha de App](https://support.google.com/accounts/answer/185833?hl=pt-BR).

## 📱 Instalação
Para instalar o syspet, basta executar o comando: `git clone https://github.com/SepulvedaRafael/syspet.git`.

Após a clonagem, abra a pasta syspet em um ambiente de desenvolvimento de sua preferência. Em seguida, execute o arquivo denominado `syspet.py`, os demais arquivos dispostos na pasta **src** são complementares a este.

Lembre-se de ter todos as bibliotecas utilizadas no programa para que este funcione adequadamente!

## 📈 Desafios Futuros
- [ ] Implementação de visualizações diferentes para Usuário e Administrador
- [ ] Estilização gráfica das interfaces com Tkinter ou similar.
- [ ] Correção de bugs existentes e outros que venham a surgir.

## 📝 Licença
Esse projeto está sob a *License MIT*. Veja o arquivo *[LICENSE](LICENSE.md)* para mais detalhes.