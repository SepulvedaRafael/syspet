import os

import identification
import crud
import atendimento

# RICH
from rich.console import Console
from rich.table import Table, box
from rich.align import Align

def menu_geral(self):
    table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')

    table.add_column('SYSPET', justify='center', style='bold red', header_style='bold red')

    if(self == 1):
        table.add_row(Align('Opção inválida! Tente novamente! \n', align='center'))
    table.add_row(Align('[1] Cadastros', align='left'))
    table.add_row(Align('[2] Atendimentos', align='left'))
    table.add_row(Align('[3] Consultas/Relatórios', align='left'))
    table.add_row(Align('[4] Sair', align='left'))

    console = Console()
    console.print(table)

def menu_cadastros(self):
    table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')

    table.add_column('CADASTROS', justify='center', style='bold red', header_style='bold red')

    if(self == 1):
        table.add_row(Align('Opção inválida! Tente novamente! \n', align='center'))
    table.add_row(Align('[1] Usuários', align='left'))
    table.add_row(Align('[2] Clientes', align='left'))
    table.add_row(Align('[3] Pets', align='left'))
    table.add_row(Align('[4] Serviços', align='left'))
    table.add_row(Align('[5] Voltar', align='left'))

    console = Console()
    console.print(table)

def menu_crud(self, aux):
    table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')
    match self:
        case 1:
            table.add_column('USUARIOS', justify='center', style='bold red', header_style='bold red')
            if(aux == 1):
                table.add_row(Align('Opção inválida! Tente novamente! \n', align='center'))
            table.add_row(Align("[1] Cadastrar", align='left'))
            table.add_row(Align("[2] Atualizar", align='left'))
            table.add_row(Align("[3] Apagar", align='left'))
            table.add_row(Align("[4] Consultar", align='left'))
            table.add_row(Align("[5] Voltar", align='left'))

            console = Console()
            console.print(table)

        case 2:
            table.add_column('CLIENTES', justify='center', style='bold red', header_style='bold red')
            if(aux == 1):
                table.add_row(Align('Opção inválida! Tente novamente! \n', align='center'))
            table.add_row(Align("[1] Cadastrar", align='left'))
            table.add_row(Align("[2] Atualizar", align='left'))
            table.add_row(Align("[3] Apagar", align='left'))
            table.add_row(Align("[4] Consultar", align='left'))
            table.add_row(Align("[5] Voltar", align='left'))

            console = Console()
            console.print(table)
        case 3:
            table.add_column('PETS', justify='center', style='bold red', header_style='bold red')
            if(aux == 1):
                table.add_row(Align('Opção inválida! Tente novamente! \n', align='center'))
            table.add_row(Align("[1] Cadastrar", align='left'))
            table.add_row(Align("[2] Atualizar", align='left'))
            table.add_row(Align("[3] Apagar", align='left'))
            table.add_row(Align("[4] Consultar", align='left'))
            table.add_row(Align("[5] Voltar", align='left'))

            console = Console()
            console.print(table)
        case 4:
            table.add_column('SERVIÇOS', justify='center', style='bold red', header_style='bold red')
            if(aux == 1):
                table.add_row(Align('Opção inválida! Tente novamente! \n', align='center'))
            table.add_row(Align("[1] Cadastrar", align='left'))
            table.add_row(Align("[2] Atualizar", align='left'))
            table.add_row(Align("[3] Apagar", align='left'))
            table.add_row(Align("[4] Consultar", align='left'))
            table.add_row(Align("[5] Voltar", align='left'))

            console = Console()
            console.print(table)
        case _:
            console.print("[white b]O argumento não é válido! Tente novamente! [/]\n")

def menu_atendimentos(self):
    table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')

    table.add_column('ATENDIMENTOS', justify='center', style='bold red', header_style='bold red')

    if(self == 1):
        table.add_row(Align('Opção inválida! Tente novamente! \n', align='center'))
    table.add_row(Align("[1] Iniciar Atendimento", align='left'))
    table.add_row(Align("[2] Agendar", align='left'))
    table.add_row(Align("[3] Remarcar", align='left'))
    table.add_row(Align("[4] Cancelar", align='left'))
    table.add_row(Align("[5] Concluir Atendimento", align='left'))
    table.add_row(Align("[6] Voltar", align='left'))

    console = Console()
    console.print(table)

def menu_visao_atendimentos(self):
    table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')

    table.add_column('CONSULTAS', justify='center', style='bold red', header_style='bold red')

    if(self == 1):
        table.add_row(Align('Opção inválida! Tente novamente! \n', align='center'))
    table.add_row(Align('[1] Agendado', align='left'))
    table.add_row(Align('[2] Cancelado', align='left'))
    table.add_row(Align('[3] Efetivado', align='left'))
    table.add_row(Align('[4] Sem agendamento', align='left'))
    table.add_row(Align('[5] Voltar', align='left'))

    console = Console()
    console.print(table)

def finalizar_programa():
    table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')

    table.add_column('SYSPET AGRADECE', justify='center', style='bold red', header_style='bold red')

    table.add_row('Programa finalizado!')

    console = Console()
    console.print(table)

def clear():
    os.system("cls")

file_clients = os.getcwd().replace("\\", "/") + "/archives/data/clientes.csv"
file_users = os.getcwd().replace("\\", "/") + "/archives/data/users.csv"
file_services = os.getcwd().replace("\\", "/") + "/archives/data/servicos.csv"
file_pets = os.getcwd().replace("\\", "/") + "/archives/data/pets.csv"
file_atendimentos = os.getcwd().replace("\\", "/") + "/archives/data/atendimentos.csv"

if identification.finalizar_programa() == False:
    pass
else:
    autentication, cpf, senha = identification.auth()

try:
    if autentication:
        console = Console()
        clear()
        menu_geral(0)
        while True:
            option = int(console.input("[red b]Insira uma opção: [/]"))
            clear()

            progress = True
            if option == 1:
                menu_cadastros(0)
                while progress:
                    option = int(console.input("[red b]Insira sua opção: [/]"))
                    clear()

                    if option == 1:
                        menu_crud(1, 0)
                        while progress:
                            option = int(console.input("[red b]Insira sua opção: [/]"))
                            clear()

                            if option == 1:
                                crud.cadastrar(1)
                                menu_crud(1, 0)

                            elif option == 2:
                                crud.atualizar(1, cpf)
                                menu_crud(1, 0)

                            elif option == 3:
                                crud.apagar(1, cpf)
                                menu_crud(1, 0)

                            elif option == 4:
                                crud.consultar(1)
                                menu_crud(1, 0)

                            elif option == 5:
                                menu_crud(1, 0)
                                break

                            else:
                                clear()
                                menu_crud(1, 1)

                    elif option == 2:
                        menu_crud(2, 0)
                        while progress:
                            option = int(console.input("[red b]Insira sua opção: [/]"))
                            clear()

                            if option == 1:
                                crud.cadastrar(2)
                                menu_crud(2, 0)

                            elif option == 2:
                                crud.atualizar(2, cpf)
                                menu_crud(2, 0)

                            elif option == 3:
                                crud.apagar(2, cpf)
                                menu_crud(2, 0)

                            elif option == 4:
                                crud.consultar(2)
                                menu_crud(2, 0)

                            elif option == 5:
                                menu_crud(2, 0)
                                break

                            else:
                                clear()
                                menu_crud(2, 1)

                    elif option == 3:
                        menu_crud(3, 0)
                        while progress:
                            option = int(console.input("[red b]Insira sua opção: [/]"))
                            clear()

                            if option == 1:
                                crud.cadastrar(3)
                                menu_crud(3, 0)

                            elif option == 2:
                                crud.atualizar(3, cpf)
                                menu_crud(3, 0)

                            elif option == 3:
                                crud.apagar(3, cpf)
                                menu_crud(3, 0)

                            elif option == 4:
                                crud.consultar(3)
                                menu_crud(3, 0)

                            elif option == 5:
                                menu_crud(3, 0)
                                break

                            else:
                                clear()
                                menu_crud(3, 1)

                    elif option == 4:
                        menu_crud(4, 0)
                        while progress:
                            option = int(console.input("[red b]Insira sua opção: [/]"))
                            clear()

                            if option == 1:
                                crud.cadastrar(4)
                                menu_crud(4, 0)

                            elif option == 2:
                                crud.atualizar(4, cpf)
                                menu_crud(4, 0)

                            elif option == 3:
                                crud.apagar(4, cpf)
                                menu_crud(4, 0)

                            elif option == 4:
                                crud.consultar(4)
                                menu_crud(4, 0)

                            elif option == 5:
                                menu_crud(4, 0)
                                break

                            else:
                                clear()
                                menu_crud(4, 1)

                    elif option == 5:
                        clear()
                        menu_geral(0)
                        break

                    else:
                        clear()
                        menu_cadastros(1)

            elif option == 2:
                menu_atendimentos(0)
                while progress:
                    option = int(console.input('[red b]Insira sua opção: [/]'))
                    clear()

                    if option == 1:
                        atendimento.iniciar_atendimento()

                    elif option == 2:
                        atendimento.agendar_atendimento()

                    elif option == 3:
                        atendimento.remarcar_atendimento()

                    elif option == 4:
                        atendimento.cancelar_atendimento()

                    elif option == 5:
                        atendimento.concluir_atendimento()

                    elif option == 6:
                        clear()
                        menu_geral(0)
                        progress = False

                    else:
                        clear()
                        menu_atendimentos(1)

            elif option == 3:
                menu_visao_atendimentos(0)
                while progress:
                    option = int(console.input('[red b]Insira sua opção: [/]'))
                    clear()

                    if option <= 4:
                        atendimento.atendimentos(option)

                    elif option == 5:
                        clear()
                        menu_geral(0)
                        progress = False

                    else:
                        clear()
                        menu_visao_atendimentos(1)

            elif option == 4:
                clear()
                finalizar_programa()
                break

            else:
                clear()
                menu_geral(1)
except NameError:
    pass