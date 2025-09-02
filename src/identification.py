import os
import validation

import csv

from unidecode import unidecode

# RICH
from rich.console import Console
from rich.table import Table, box

def welcome(self):
    table = Table(title=' ', box=box.DOUBLE_EDGE, style='red', width=60)

    table.add_column('WELCOME TO SYSPET', justify='center', style='bold red', header_style='bold red')

    if(self == 1):
        table.add_row('Opção inválida! Tente novamente! \n')
    table.add_row('[white b][1][/] Logar no Syspet')
    table.add_row('[white b][2][/] Registrar-se')
    table.add_row('[white b][3][/] Sair')

    console = Console()
    console.print(table)

def menu_register(self):
    table = Table(title=' ', box=box.DOUBLE_EDGE, style='red', width=60)

    table.add_column('REGISTER TO SYSPET', justify='center', style='bold red', header_style='bold red')

    table.add_row(self)

    console = Console()
    console.print(table)

def menu_login(self):
    table = Table(title=' ', box=box.DOUBLE_EDGE, style='red', width=60)

    table.add_column('LOGIN TO SYSPET', justify='center', style='bold red', header_style='bold red')

    table.add_row(self)

    console = Console()
    console.print(table)

def finalizar_programa():
    if(option == 3):
        table = Table(title=' ', box=box.DOUBLE_EDGE, style='red', width=60)

        table.add_column('SYSPET AGRADECE', justify='center', style='bold red', header_style='bold red')

        table.add_row('Programa finalizado!')

        console = Console()
        console.print(table)
        return False
    else:
        return True

def clear():
    os.system("cls")

file = os.getcwd().replace("\\", "/") + "/data/users.csv"

def auth():
    progress = True
    tip = 'Dica: 12345678912'
    menu_login(tip)
    while progress:
        cpf = console.input("[white b]CPF do User: [/]")

        # Validação do cpf
        if validation.iscpf(cpf):
            # In clientes.csv?
            with open(file, "r", newline="\n") as readercsv:
                read = csv.reader(readercsv, delimiter=";")
                next(read)

                for row in read:
                    cpf_client, senha_client = row[0], row[1]
                    if cpf == cpf_client:
                        clear()
                        tip = 'Informe a senha cadastrada'
                        menu_login(tip)
                        while progress:
                            senha = console.input('[white b]Senha do User: [/]')

                            # Validação da senha
                            if validation.issenha(senha):
                                if senha == senha_client:
                                    progress = False
                                    return [True, cpf, senha]
                                else:
                                    clear()
                                    error = "A senha informada não é a cadastrada."
                                    menu_register(error)
                            else:
                                clear()
                                error = "Senha inválida! Tente novamente."
                                menu_register(error)
        else:
            clear()
            error = "CPF inválido! Tente novamente."
            menu_register(error)

def register():
    progress = True
    # ALTERAR TUDO PARA CSV
    if os.path.exists(file):
        df = open(file, "a")
    else:
        df = open(file, "a")
        df.write("cpf;senha;tipo\n")

    tip = "Dica: 12345678912"
    menu_register(tip)
    while progress:
        cpf = console.input("[white b]CPF do User: [/]")

        # Validação do CPF
        if validation.iscpf(cpf):
            with open(file, "r") as df:
                next(df)
                linhas = df.readlines()
                cpfs = set()
                for row in linhas:
                    cpf_user, senha_user, tipo_user = row.split(";")
                    cpfs.add(cpf_user)

            if cpf not in cpfs:
                with open(file, "a", newline="\n") as df:
                    df.write(f"{unidecode(cpf)};")
                    clear()
                    tip = '''Deve ter entre 8 a 32 caracteres.
Deve ter, no mínimo, uma letra maiúscula e uma minúscula.
Deve ter, no mínimo, um número.
Deve ter, no mínimo, um caracetere especial [!#@$%&].'''
                    menu_register(tip)
                    while progress:
                        senha = console.input('[white b]Senha do User: [/]')

                        # Validação da senha
                        if validation.issenha(senha):
                            df.write(f"{unidecode(senha)};")
                            progress = False
                            clear()
                        else:
                            clear()
                            error = "Senha inválida! Tente novamente!"
                            menu_register(error)
            else:
                clear()
                error = 'CPF já cadastrado! Tente com outro!'
                menu_register(error)
        else:
            clear()
            error = 'CPF inválido! Tente novamente!'
            menu_register(error)

welcome(0)
while True:
    # Menu de entrada
    console = Console()
    option = int(console.input('[white b]Insira sua opção:[/] '))
    clear()

    progress = True
    # Condicional de select
    if option == 1:
        break

    elif option == 2:
        nLinhas = 0
        register()

        with open(file, "r") as df:
            next(df)
            for linha in df:
                if linha[1] != "":
                    nLinhas += 1

        with open(file, "a") as df:
            if nLinhas == 1:
                df.write("Administrador\n")
            else:
                df.write("Usuario\n")
        welcome(0)

    elif option == 3:
        break

    else:
        welcome(1)
