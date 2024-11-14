import os
import validation

from datetime import datetime as dt

# RICH
from rich.console import Console
from rich.table import box
from rich.panel import Panel
from rich.align import Align

def clear():
    os.system('cls')

def menu_atendimentos():
    console = Console()

    panel = Panel(Align('ATENDIMENTOS', align='center'), width=40, box=box.DOUBLE_EDGE, style='red')
    console.print(panel)

file_clients = os.getcwd().replace("\\", "/") + "/archives/data/clientes.csv"
file_users = os.getcwd().replace("\\", "/") + "/archives/data/users.csv"
file_services = os.getcwd().replace("\\", "/") + "/archives/data/servicos.csv"
file_pets = os.getcwd().replace("\\", "/") + "/archives/data/pets.csv"
file_atendimentos = os.getcwd().replace("\\", "/") + "/archives/data/atendimentos.csv"

def iniciar_atendimento():
    console = Console()

    progress = True
    options = []
    while progress:
        with open(file_clients, 'r') as df:
            next(df)
            linhas = df.readlines()
            for i, row in enumerate(linhas):
                nome_cliente, sexo_cliente, cpf_cliente, celular_cliente, email_celular, codigo_end_postal_cliente, endereco_cliente, bairro_cliente, complemento_cliente, cidade_cliente, estado_cliente = row.split(";")
                console.print(f'[white b][{i + 1}][/] [red b]{nome_cliente} [{cpf_cliente}][/]')
            console.print(f"[white b][{i + 2}][/] [red b]Voltar[/]")

            option_user = int(console.input('[red b]Insira sua opção: [/]'))
            clear()
            if option_user - 1 <= i:
                nome_cliente, sexo_cliente, cpf_cliente, celular_cliente, email_celular, codigo_end_postal_cliente, endereco_cliente, bairro_cliente, complemento_cliente, cidade_cliente, estado_cliente = linhas[option_user - 1].split(";")
                options.extend([cpf_cliente, nome_cliente])
                while progress:
                    with open(file_pets, 'r') as df:
                        next(df)
                        linhas = df.readlines()
                        cont = 0
                        pets = []
                        for row in linhas:
                            id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = row.split(';')
                            if(cpf_dono_pet.strip() == cpf_cliente):
                                pets.append(nome_pet)
                                console.print(f'[white b][{cont + 1}][/] [red b]{nome_pet}[/]')
                                cont += 1
                        console.print(f'[white b][{cont + 1}][/] [red b]Voltar[/]')
                        option_user = int(console.input('[red b]Insira sua opção: [/]'))
                        clear()
                        if option_user <= cont:
                            for row in linhas:
                                id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = row.split(';')
                                if(nome_pet == pets[option_user - 1]):
                                    options.extend([id_pet, nome_pet])

                            with open(file_services, 'r') as df:
                                next(df)
                                linhas = df.readlines()
                                for i, row in enumerate(linhas):
                                    id_servico, descricao_servico, valor_servico, orientacao_servico = row.split(';')
                                    console.print(f'[white b][{i + 1}][/] [red b]{descricao_servico} [{valor_servico}][/]')
                                console.print(f'[white b][{i + 2}][/] [red b]Voltar[/]')
                                option_user = int(console.input('[red b]Insira sua opção: [/]'))
                                clear()
                                if option_user - 1 <= i:
                                    id_servico, descricao_servico, valor_servico, orientacao_servico = linhas[option_user - 1].split(';')
                                    options.extend([id_servico, descricao_servico, validation.transformValue(valor_servico)])

                                    console.print(f'[white b][{options[0]}][/] [red b]{options[1]}[/]')
                                    console.print(f'[white b][{options[2]}][/] [red b]{options[3]}[/]')
                                    console.print(f'[white b][{options[4]}][/] [red b]{options[5]}[/]')
                                    console.print(f'[white b]Valor:[/] [red b]{options[6]}[/]\n')
                                    confirm = console.input('[red b]Para confirmar: SIM | Para negar: NÃO: [/]')

                                    if confirm.upper() == 'SIM':
                                        if os.path.exists(file_atendimentos):
                                            df = open(file_atendimentos, "a")
                                        else:
                                            df = open(file_atendimentos, "a")
                                            df.write("id_servico;id_pet;data_atendimento;data_agendamento;data_conclusao;situacao\n")

                                        atual = dt.now()
                                        data_atendimento = str(atual.day) + '/' + str(atual.month) + '/' + str(atual.year)
                                        with open(file_atendimentos, 'a') as df:
                                            df.write(f'{options[4]};{options[2]};{data_atendimento};;;\n')
                                        progress = False
                                        clear()
                                    elif confirm == 'NÃO':
                                        continue
                                    else:
                                        console.print('[red b]Tente novamente![/]\n')
                                elif option_user == i + 2:
                                    clear()
                                    break

                                else:
                                    console.print('[red b]Opção inválida! Tente novamente! [/]\n')
                        elif option_user == cont + 1:
                            clear()
                            break

                        else:
                            console.print('[red b]Opção inválida! Tente novamente! [/]\n')
            elif option_user == i + 2:
                clear()
                break

            else:
                console.print('[red b]Opção inválida! Tente novamente! [/]\n')

def agendar_atendimento():
    console = Console()

    progress = True
    while progress:
        with open(file_atendimentos, 'r') as df:
            next(df)
            cont = 0
            pets = []
            linhas = df.readlines()
            for row in linhas:
                id_servico, id_pet_atendimentos, data_atendimento, data_agendamento_atendimentos, data_conclusao, situacao = row.split(';')
                situacao = situacao.strip()
                if situacao == '':
                    with open(file_pets, 'r') as df_pets:
                        next(df_pets)
                        linhas = df_pets.readlines()
                        for linha in linhas:
                            id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = linha.split(';')
                            if(id_pet_atendimentos == id_pet):
                                pets.append([id_pet, id_servico])
                                console.print(f'[white b][{cont + 1}][/] [red b]{id_pet} - {nome_pet} [{id_servico}][/]')
                                cont += 1
        console.print(f'[white b][{cont + 1}][/] [red b]Voltar[/]')

        option_user = int(console.input('[red b]Insira sua opção: [/]'))
        clear()
        if option_user <= cont:
            while progress:
                console.print('[white b]Dica: 11/11/2024 (Formato de data)[/]')
                data_agendamento = console.input('[red b]Data de Agendamento: [/]')

                # Validação da data
                if validation.isdata(data_agendamento):
                    with open(file_atendimentos, 'r') as df:
                        next(df)
                        index = 0
                        linhas_atendimentos = df.readlines()
                        for i, row in enumerate(linhas_atendimentos):
                            id_servico, id_pet_atendimentos, data_atendimento, data_agendamento_atendimentos, data_conclusao, situacao = row.split(';')
                            if(id_servico == pets[option_user - 1][1] and id_pet_atendimentos == pets[option_user - 1][0] and situacao.strip() == ''):
                                    situacao = 'Agendado\n'
                                    new_line = id_servico + ';' + id_pet_atendimentos + ';' + data_atendimento + ';' + data_agendamento + ';' + data_conclusao + ';' + situacao
                                    index = i
                                    break
                        linhas_atendimentos.pop(index)
                        with open(file_atendimentos, 'w') as df:
                            df.write('id_servico;id_pet;data_atendimento;data_agendamento;data_conclusao;situacao\n')
                            df.writelines(linhas_atendimentos)
                            df.write(new_line)
                        progress = False
                        clear()
                        console.print('[white b]O agendamento foi realizado com sucesso! [/]\n')
                else:
                    clear()
                    console.print('[red b]Data de Agendamento inválida! Tente novamente! [/]\n')

        elif option_user == cont + 1:
            clear()
            break

        else:
            clear()
            console.print('[red b]Opção inválida! Tente novamente! [/]\n')

def remarcar_atendimento():
    console = Console()
    with open(file_atendimentos, 'r') as df:
        next(df)
        linhas = df.readlines()
        for row in linhas:
            id_servico, id_pet_atendimentos, data_atendimento, data_agendamento, data_conclusao, situacao = row.split(';')
            if(data_agendamento == ''):
                progress = False
                clear()
                console.print(f'[white b]Não há um agendamento para o pet com ID: {id_pet_atendimentos}. [/]\n')
                break
            else:
                progress = True
    if progress == True:
        while progress:
            with open(file_atendimentos, 'r') as df:
                next(df)
                cont = 0
                pets = []
                linhas_atendimentos = df.readlines()
                for row in linhas_atendimentos:
                    id_servico, id_pet_atendimentos, data_atendimento, data_agendamento_atendimentos, data_conclusao, situacao = row.split(';')
                    situacao = situacao.strip()
                    if(situacao == 'Agendado'):
                        with open(file_pets, 'r') as df_pets:
                            next(df_pets)
                            linhas = df_pets.readlines()
                            for linha in linhas:
                                id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = linha.split(';')
                                if(id_pet_atendimentos == id_pet):
                                    pets.append([id_pet, id_servico])
                                    console.print(f'[white b][{cont + 1}][/] [red b]Data: {data_agendamento_atendimentos.strip()} | {id_pet} - {nome_pet} [{id_servico}][/]')
                                    cont += 1
            console.print(f'[white b][{cont + 1}][/] [red b]Voltar [/]\n')

            option_user = int(console.input('[red b]Insira sua opção: [/]'))
            clear()
            if option_user <= cont:
                while progress:
                    console.print('[white b]Dica: 11/11/2024 (Formato de data)[/]')
                    data_remarcamento = console.input('[red b]Nova Data: [/]')

                    # Validação da data
                    if validation.isdata(data_remarcamento):
                        with open(file_atendimentos, 'r') as df:
                            next(df)
                            index = 0
                            linhas = df.readlines()
                            for i, row in enumerate(linhas):
                                id_servico, id_pet_atendimentos, data_atendimento, data_agendamento_atendimentos, data_conclusao, situacao = row.split(';')
                                if(id_servico == pets[option_user - 1][1] and id_pet_atendimentos == pets[option_user - 1][0] and situacao.strip() == 'Agendado'):
                                    situacao = 'Remarcado\n'
                                    new_line = id_servico + ';' + id_pet_atendimentos + ';' + data_atendimento + ';' + data_remarcamento + ';' + data_conclusao + ';' + situacao
                                    index = i
                                    break
                            linhas.pop(index)
                            with open(file_atendimentos, 'w') as df:
                                df.write('id_servico;id_pet;data_atendimento;data_agendamento;data_conclusao;situacao\n')
                                df.writelines(linhas)
                                df.write(new_line)
                            progress = False
                            clear()
                            console.print('[white b]O reagendamento foi realizado com sucesso! [/]\n')
                    else:
                        clear()
                        console.print('[red b]Data de Agendamento inválida! Tente novamente! [/]\n')

            elif option_user == cont + 1:
                clear()
                break

            else:
                clear()
                console.print('[red b]Opção inválida! Tente novamente! [/]\n')

def cancelar_atendimento():
    console = Console()
    progress = True
    while progress:
        with open(file_atendimentos, 'r') as df:
            next(df)
            cont = 0
            pets = []
            linhas = df.readlines()
            for row in linhas:
                id_servico, id_pet_atendimentos, data_atendimento, data_agendamento, data_conclusao, situacao = row.split(';')
                situacao = situacao.strip()
                if situacao != 'Cancelado' and situacao != 'Efetivado' and situacao != '':
                    with open(file_pets, 'r') as df_pets:
                        next(df_pets)
                        linhas = df_pets.readlines()
                        for linha in linhas:
                            id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = linha.split(';')
                            if(id_pet_atendimentos == id_pet):
                                pets.append([id_pet, id_servico])
                                console.print(f'[white b][{cont + 1}][/] [red b]{id_pet} - {nome_pet} [{id_servico}][/]')
                                cont += 1
        console.print(f'[white b][{cont + 1}][/] [red b]Voltar[/] \n')

        option_user = int(console.input('[red b]Insira sua opção: [/]'))
        clear()
        if option_user <= cont:
            with open(file_atendimentos, 'r') as df:
                next(df)
                index = 0
                linhas = df.readlines()
                for i, row in enumerate(linhas):
                    id_servico, id_pet_atendimentos, data_atendimento, data_agendamento, data_conclusao, situacao = row.split(';')
                    if(id_servico == pets[option_user - 1][1] and id_pet_atendimentos == pets[option_user - 1][0] and situacao.strip() != 'Cancelado' and situacao.strip() != 'Efetivado' and situacao.strip() != ''):
                        situacao = 'Cancelado\n'
                        new_line = id_servico + ';' + id_pet_atendimentos + ';' + data_atendimento + ';' + data_agendamento + ';' + data_conclusao + ';' + situacao
                        index = i
                        break
                linhas.pop(index)
                with open(file_atendimentos, 'w') as df:
                    df.write('id_servico;id_pet;data_atendimento;data_agendamento;data_conclusao;situacao\n')
                    df.writelines(linhas)
                    df.write(new_line)
                progress = False
                clear()
                console.print('[white b]O atendimento foi cancelado com sucesso! [/]\n')

        elif option_user == cont + 1:
            clear()
            break

        else:
            clear()
            console.print('[red b]Opção inválida! Tente novamente! [/]\n')

def concluir_atendimento():
    console = Console()
    progress = True
    while progress:
        with open(file_atendimentos, 'r') as df:
            next(df)
            cont = 0
            pets = []
            linhas = df.readlines()
            for row in linhas:
                id_servico, id_pet_atendimentos, data_atendimento, data_agendamento, data_conclusao, situacao = row.split(';')
                situacao = situacao.strip()
                if situacao != 'Cancelado' and situacao != 'Efetivado' and situacao != '':
                    with open(file_pets, 'r') as df_pets:
                        next(df_pets)
                        linhas = df_pets.readlines()
                        for linha in linhas:
                            id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = linha.split(';')
                            if(id_pet_atendimentos == id_pet):
                                pets.append([id_pet, id_servico])
                                console.print(f'[white b][{cont + 1}][/] [red b]{id_pet} - {nome_pet} [{id_servico}][/]')
                                cont += 1
        console.print(f'[white b][{cont + 1}][/] [red b]Voltar[/]\n')

        option_user = int(console.input('[red b]Insira sua opção: [/]'))
        clear()
        if option_user <= cont:
            with open(file_atendimentos, 'r') as df:
                next(df)
                index = 0
                linhas_atendimentos = df.readlines()
                for i, row in enumerate(linhas_atendimentos):
                    id_servico, id_pet_atendimentos, data_atendimento, data_agendamento, data_conclusao, situacao = row.split(';')
                    if(id_servico == pets[option_user - 1][1] and id_pet_atendimentos == pets[option_user - 1][0] and situacao.strip() != 'Cancelado' and situacao.strip() != 'Efetivado' and situacao.strip() != ''):
                            situacao = 'Efetivado\n'
                            atual = dt.now()
                            data_conclusao = str(atual.day) + '/' + str(atual.month) + '/' + str(atual.year)
                            new_line = id_servico + ';' + id_pet_atendimentos + ';' + data_atendimento + ';' + data_agendamento + ';' + data_conclusao + ';' + situacao
                            index = i
                            break
                linhas_atendimentos.pop(index)
                with open(file_atendimentos, 'w') as df:
                    df.write('id_servico;id_pet;data_atendimento;data_agendamento;data_conclusao;situacao\n')
                    df.writelines(linhas_atendimentos)
                    df.write(new_line)
                progress = False
                clear()
                console.print('[white b]O atendimento foi efetivado com sucesso! [/]\n')

        elif option_user == cont + 1:
            clear()
            break

        else:
            clear()
            console.print('[red b]Opção inválida! Tente novamente! [/]\n ')

def atendimentos(self):
    console = Console()
    match self:
        case 1:
            progress = True
            while progress:
                menu_atendimentos()
                with open(file_atendimentos, 'r') as df:
                    next(df)
                    cont = 0
                    linhas = df.readlines()
                    for row in linhas:
                        id_servico, id_pet_atendimentos, data_atendimento, data_agendamento, data_conclusao, situacao = row.split(';')
                        situacao = situacao.strip()
                        if(situacao == 'Agendado' or situacao == 'Remarcado'):
                            with open(file_pets, 'r') as df_pets:
                                next(df_pets)
                                linhas_pets = df_pets.readlines()
                                for row in linhas_pets:
                                    id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = row.split(';')
                                    if(id_pet == id_pet_atendimentos):
                                        console.print(f'[white b][{cont + 1}][/] [red b]Data: {data_agendamento} - {id_pet_atendimentos} {nome_pet}[/]')
                                        cont += 1
                print('')
                console.print(f'[white b]TOTAL DE ATENDIMENTOS AGENDADOS: {cont}[/]')
                print('')
                progress = False

        case 2:
            progress = True
            while progress:
                menu_atendimentos()
                with open(file_atendimentos, 'r') as df:
                    next(df)
                    cont = 0
                    linhas = df.readlines()
                    for row in linhas:
                        id_servico, id_pet_atendimentos, data_atendimento, data_agendamento, data_conclusao, situacao = row.split(';')
                        situacao = situacao.strip()
                        if(situacao == 'Cancelado'):
                            with open(file_pets, 'r') as df_pets:
                                next(df_pets)
                                linhas_pets = df_pets.readlines()
                                for row in linhas_pets:
                                    id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = row.split(';')
                                    if(id_pet == id_pet_atendimentos):
                                        console.print(f'[white b][{cont + 1}][/] [red b]Data: {data_agendamento} - {id_pet_atendimentos} {nome_pet}[/]')
                                        cont += 1
                print('')
                console.print(f'[white b]TOTAL DE ATENDIMENTOS CANCELADOS: {cont}[/]')
                print('')
                progress = False

        case 3:
            progress = True
            while progress:
                menu_atendimentos()
                with open(file_atendimentos, 'r') as df:
                    next(df)
                    cont = 0
                    linhas = df.readlines()
                    for row in linhas:
                        id_servico, id_pet_atendimentos, data_atendimento, data_agendamento, data_conclusao, situacao = row.split(';')
                        situacao = situacao.strip()
                        if(situacao == 'Efetivado'):
                            with open(file_pets, 'r') as df_pets:
                                next(df_pets)
                                linhas_pets = df_pets.readlines()
                                for row in linhas_pets:
                                    id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = row.split(';')
                                    if(id_pet == id_pet_atendimentos):
                                        console.print(f'[white b][{cont + 1}][/] [red b]Data: {data_agendamento} - {id_pet_atendimentos} {nome_pet}[/]')
                                        cont += 1
                print('')
                console.print(f'[white b]TOTAL DE ATENDIMENTOS EFETIVADOS: {cont}[/]')
                print('')
                progress = False

        case 4:
            progress = True
            while progress:
                menu_atendimentos()
                with open(file_atendimentos, 'r') as df:
                    next(df)
                    cont = 0
                    linhas = df.readlines()
                    for row in linhas:
                        id_servico, id_pet_atendimentos, data_atendimento, data_agendamento, data_conclusao, situacao = row.split(';')
                        situacao = situacao.strip()
                        if(situacao == ''):
                            with open(file_pets, 'r') as df_pets:
                                next(df_pets)
                                linhas_pets = df_pets.readlines()
                                for row in linhas_pets:
                                    id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = row.split(';')
                                    if(id_pet == id_pet_atendimentos):
                                        console.print(f'[white b][{cont + 1}][/] [red b]{id_pet_atendimentos} {nome_pet}[/]')
                                        cont += 1
                print('')
                console.print(f'[white b]TOTAL DE ATENDIMENTOS SEM AGENDAMENTO: {cont}[/]')
                print('')
                progress = False