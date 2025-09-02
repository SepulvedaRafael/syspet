import os
from unidecode import unidecode

import validation
from identification import register

# RICH
from rich.console import Console
from rich.table import Table, box
from rich.align import Align
from rich.panel import Panel

file_clients = os.getcwd().replace("\\", "/") + "/data/clientes.csv"
file_users = os.getcwd().replace("\\", "/") + "/data/users.csv"
file_services = os.getcwd().replace("\\", "/") + "/data/servicos.csv"
file_pets = os.getcwd().replace("\\", "/") + "/data/pets.csv"
file_atendimentos = os.getcwd().replace("\\", "/") + "/data/atendimentos.csv"

def clear():
    os.system("cls")

def menu_cadastrar(self, aux):
    console = Console()
    match self:
        case 2:
            if aux == 0:
                panel = Panel(Align('CADASTRAMENTO DE CLIENTE', align='center'), width=60, box=box.DOUBLE_EDGE, style='bold red')
                console.print(panel)
            else:
                table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')
                table.add_column('CADASTRAMENTO DE CLIENTE', justify='center', style='bold red', header_style='bold red')

                table.add_row(aux)
                console.print(table)

        case 3:
            if aux == 0:
                panel = Panel(Align('CADASTRAMENTO DE PET', align='center'), width=60, box=box.DOUBLE_EDGE, style='bold red')
                console.print(panel)
            else:
                table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')
                table.add_column('CADASTRAMENTO DE PET', justify='center', style='bold red', header_style='bold red')

                table.add_row(aux)
                console.print(table)

        case 4:
            if aux == 0:
                panel = Panel(Align('CADASTRAMENTO DE SERVIÇO', align='center'), width=60, box=box.DOUBLE_EDGE, style='bold red')
                console.print(panel)
            else:
                table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')
                table.add_column('CADASTRAMENTO DE SERVIÇO', justify='center', style='bold red', header_style='bold red')

                table.add_row(aux)
                console.print(table)

def menu_atualizar(self, aux):
    console = Console()
    match self:
        case 1:
            if aux == 0:
                panel = Panel(Align('ATUALIZAÇÃO DE USUÁRIO', align='center'), width=60, box=box.DOUBLE_EDGE, style='bold red')
                console.print(panel)
            else:
                table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')
                table.add_column('ATUALIZAÇÃO DE USUÁRIO', justify='center', style='bold red', header_style='bold red')

                table.add_row(aux)
                console.print(table)

        case 2:
            if aux == 0:
                panel = Panel(Align('ATUALIZAÇÃO DE CLIENTE', align='center'), width=60, box=box.DOUBLE_EDGE, style='bold red')
                console.print(panel)
            else:
                table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')
                table.add_column('ATUALIZAÇÃO DE CLIENTE', justify='center', style='bold red', header_style='bold red')

                table.add_row(aux)
                console.print(table)

        case 3:
            if aux == 0:
                panel = Panel(Align('ATUALIZAÇÃO DE PET', align='center'), width=60, box=box.DOUBLE_EDGE, style='red')
                console.print(panel)
            else:
                table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')
                table.add_column('ATUALIZAÇÃO DE PET', justify='center', style='bold red', header_style='bold red')

                table.add_row(aux)
                console.print(table)

        case 4:
            if aux == 0:
                panel = Panel(Align('ATUALIZAÇÃO DE SERVIÇO', align='center'), width=60, box=box.DOUBLE_EDGE, style='bold red')
                console.print(panel)
            else:
                table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')
                table.add_column('ATUALIZAÇÃO DE SERVIÇO', justify='center', style='bold red', header_style='bold red')

                table.add_row(aux)
                console.print(table)

def menu_apagar(self, aux):
    console = Console()
    match self:
        case 1:
            if aux == 0:
                panel = Panel(Align('APAGAR USUÁRIO', align='center'), width=60, box=box.DOUBLE_EDGE, style='bold red')
                console.print(panel)
            else:
                table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')
                table.add_column('APAGAR USUÁRIO', justify='center', style='bold red', header_style='bold red')

                table.add_row(aux)
                console.print(table)

        case 2:
            if aux == 0:
                panel = Panel(Align('APAGAR CLIENTE', align='center'), width=60, box=box.DOUBLE_EDGE, style='bold red')
                console.print(panel)
            else:
                table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')
                table.add_column('APAGAR CLIENTE', justify='center', style='bold red', header_style='bold red')

                table.add_row(aux)
                console.print(table)

        case 3:
            if aux == 0:
                panel = Panel(Align('APAGAR PET', align='center'), width=60, box=box.DOUBLE_EDGE, style='bold red')
                console.print(panel)
            else:
                table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')
                table.add_column('APAGAR PET', justify='center', style='bold red', header_style='bold red')

                table.add_row(aux)
                console.print(table)

        case 4:
            if aux == 0:
                panel = Panel(Align('APAGAR SERVIÇO', align='center'), width=60, box=box.DOUBLE_EDGE, style='bold red')
                console.print(panel)
            else:
                table = Table(title=' ', box=box.DOUBLE_EDGE, style='red')
                table.add_column('APAGAR SERVIÇO', justify='center', style='bold red', header_style='bold red')

                table.add_row(aux)
                console.print(table)

def menu_consultar(self):
    console = Console()
    panel = Panel(Align(self + ' CADASTRADOS', align='center'), width=60, box=box.DOUBLE_EDGE, style='bold red')
    console.print(panel)

def total_consulta(self):
    console = Console()
    panel = Panel(Align(self, align='center'), width=60, box=box.DOUBLE_EDGE, style='white bold')
    console.print(panel)

def cadastrar(self):
    console = Console()
    match self:
        case 1:
            register()
            console.print("[red b]Dica: Usuário ou Administrador[/]")
            tipo_user = console.input("[white b]Digite o tipo desse CPF: [/]")
            with open(file_users, "a", newline="\n") as df:
                df.write(f"{unidecode(tipo_user)}\n")
            clear()
            console.print('[white b]\nO usuário foi cadastrado com sucesso![/]', justify='center', width=60)

        case 2:
            progress = True
            menu_cadastrar(self, 0)
            if os.path.exists(file_clients):
                df = open(file_clients, "a")
            else:
                df = open(file_clients, "a")
                df.write("nome;sexo;cpf;celular;email;codigo_end_postal;endereco;bairro;complemento;cidade;estado\n")
            while progress:
                nome_cliente = console.input("[white b]Nome Completo: [/]")

                # Validação do nome
                if validation.isnome(nome_cliente.strip()):
                    with open(file_clients, "a", newline="\n") as df:
                        df.write(f"{unidecode(nome_cliente)};")
                        clear()
                        tip = 'Dica: Masculino ou M | Feminino ou F.'
                        menu_cadastrar(self, tip)
                        while progress:
                            sexo_cliente = console.input("[white b]Sexo: [/]")

                            # Validação do sexo
                            if validation.issexo(sexo_cliente):
                                df.write(f"{unidecode(sexo_cliente)};")
                                clear()
                                tip = 'Dica: 12345678912'
                                menu_cadastrar(self, tip)
                                while progress:
                                    cpf_cliente = console.input("[white b]CPF: [/]")

                                    # Validação do CPF
                                    if validation.iscpf(cpf_cliente):
                                        df.write(f"{unidecode(cpf_cliente)};")
                                        clear()
                                        tip = 'Informe o seu DDD e número de celular sem -.'
                                        menu_cadastrar(self, tip)
                                        while progress:
                                            celular_cliente = console.input("[white b]Celular: +55[/]")

                                            # Validação do Celular
                                            if validation.iscelular(celular_cliente):
                                                df.write(f"{celular_cliente};")
                                                clear()
                                                tip = 'Provedores suportados: Hotmail, Gmail, Yahoo e Outlook.'
                                                menu_cadastrar(self, tip)
                                                while progress:
                                                    email_cliente = console.input("[white b]Email: [/]")

                                                    # Validação do Email
                                                    if validation.isemail(email_cliente):
                                                        df.write(f"{email_cliente};")
                                                        clear()
                                                        tip = 'Informe apenas os números do CEP.'
                                                        menu_cadastrar(self, tip)
                                                        while progress:
                                                            codigo_end_postal_cliente = console.input("[white b]CEP: [/]").rstrip()

                                                            # Validação do CEP
                                                            endereco, cep = validation.iscep(codigo_end_postal_cliente)
                                                            if cep:
                                                                df.write(f'{unidecode(endereco['cep'])};{unidecode(endereco['street'])};{unidecode(endereco['district'])};{unidecode(endereco['complement'])};{unidecode(endereco['city'])};{unidecode(endereco['uf'])}\n' )
                                                                progress = False
                                                                clear()
                                                                console.print('[white b]\nO cliente foi cadastrado com sucesso![/]', justify='center', width=60)
                                                            else:
                                                                clear()
                                                                error = 'CEP inválido! Tente novamente!\n'
                                                                menu_cadastrar(self, error)
                                                    else:
                                                        clear()
                                                        error = 'Email inválido! Tente novamente!\n'
                                                        menu_cadastrar(self, error)
                                            else:
                                                clear()
                                                error = 'Número de celular inválido! Tente novamente!\n'
                                                menu_cadastrar(self, error)
                                    else:
                                        clear()
                                        error = 'CPF inválido! Tente novamente!\n'
                                        menu_cadastrar(self, error)
                            else:
                                clear()
                                error = 'Sexo inválido! Tente novamente!\n'
                                menu_cadastrar(self, error)
                else:
                    clear()
                    error = 'Nome inválido! Tente novamente!\n'
                    menu_cadastrar(self, error)

        case 3:
            progress = True
            menu_cadastrar(self, 0)
            if os.path.exists(file_pets):
                df = open(file_pets, 'a')
            else:
                df = open(file_pets, 'a')
                df.write('id_pet;nome_pet;categoria_pet;raca_pet;data_nascimento_pet;cpf_dono_pet\n')
            while progress:
                id_pet = console.input('[white b]ID do Pet: [/]')

                # Validação do ID
                if(validation.checkString(id_pet)):
                    with open(file_pets, 'a', newline='\n') as df:
                        df.write(f'{unidecode(id_pet)};')
                        clear()
                        menu_cadastrar(self, 0)
                        while progress:
                            nome_pet = console.input('[white b]Nome do Pet: [/]')

                            # Validação do Nome
                            if(validation.isnome(nome_pet)):
                                df.write(f'{unidecode(nome_pet)};')
                                clear()
                                tip = 'Categorias: Ave | Bovino | Canino | Felino'
                                menu_cadastrar(self, tip)
                                while progress:
                                    categoria_pet = console.input('[white b]Categoria do Pet: [/]')

                                    # Validação da Categoria
                                    if(validation.iscategoria(categoria_pet)):
                                        df.write(f'{unidecode(categoria_pet)};')
                                        clear()
                                        menu_cadastrar(self, 0)
                                        while progress:
                                            raca_pet = console.input('[white b]Raça do Pet: [/]')

                                            # Validação da Raça
                                            if(validation.israca(raca_pet)):
                                                df.write(f'{unidecode(raca_pet)};')
                                                clear()
                                                menu_cadastrar(self, 0)
                                                while progress:
                                                    data_nascimento_pet = console.input('[white b]Data de Nascimento do Pet: [/]')

                                                    # Validação da Data de Nascimento
                                                    if(validation.isdataNascimento(data_nascimento_pet)):
                                                        df.write(f'{unidecode(data_nascimento_pet)};')
                                                        clear()
                                                        menu_cadastrar(self, 0)
                                                        while progress:
                                                            cpf_dono_pet = console.input('[white b]CPF do Dono do Pet: [/]')

                                                            # Validação do CPF do Dono
                                                            if(validation.iscpf(cpf_dono_pet)):
                                                                df.write(f'{unidecode(cpf_dono_pet)}\n')
                                                                progress = False
                                                                clear()
                                                                console.print('[white b]\nO pet foi cadastrado com sucesso![/]', justify='center', width=60)
                                                            else:
                                                                clear()
                                                                error = 'CPF do Dono do Pet inválido! Tente novamente!\n'
                                                                menu_cadastrar(self, error)
                                                    else:
                                                        clear()
                                                        error = 'Data de Nascimento do Pet inválida! Tente novamente!\n'
                                                        menu_cadastrar(self, error)
                                            else:
                                                clear()
                                                error = 'Raça do Pet inválido! Tente novamente!\n'
                                                menu_cadastrar(self, error)
                                    else:
                                        clear()
                                        error = 'Categoria do Pet inválida! Tente novamente!\n'
                                        menu_cadastrar(self, error)
                            else:
                                clear()
                                error = 'Nome do Pet inválido! Tente novamente!\n'
                                menu_cadastrar(self, error)
                else:
                    clear()
                    error = 'ID do Pet inválido! Tente novamente!\n'
                    menu_cadastrar(self, error)

        case 4:
            progress = True
            menu_cadastrar(self, 0)
            if(os.path.exists(file_services)):
                df = open(file_services, 'a')
            else:
                df = open(file_services, 'a')
                df.write('id_servico;descricao_servico;valor_servico;orientacao_servico\n')
            while progress:
                id_servico = console.input('[white b]Id do Serviço: [/]')

                # Validação do ID
                if(validation.checkString(id_servico)):
                    with open(file_services, 'a', newline='\n') as df:
                        df.write(f'{unidecode(id_servico)};')
                        clear()
                        menu_cadastrar(self, 0)
                        while progress:
                            descricao_servico = console.input('[white b]Descrição do Serviço: [/]')

                            # Validação da Descrição
                            if(validation.checkString(descricao_servico)):
                                df.write(f'{unidecode(descricao_servico)};')
                                clear()
                                menu_cadastrar(self, 0)
                                while progress:
                                    valor_servico = console.input('[white b]Valor do Serviço: [/]')

                                    # Validação do Valor
                                    if(validation.checkString(valor_servico)):
                                        df.write(f'{unidecode(valor_servico)};')
                                        clear()
                                        menu_cadastrar(self, 0)
                                        while progress:
                                            orientacao_servico = console.input('[white b]Orientação do Serviço: [/]')

                                            # Validação da Orientação
                                            if(validation.checkString(orientacao_servico)):
                                                df.write(f'{unidecode(orientacao_servico)}\n')
                                                progress = False
                                                clear()
                                                console.print('[white b]\nO serviço foi cadastrado com sucesso![/]', justify='center', width=60)
                                            else:
                                                clear()
                                                error = 'Orientação do Serviço inválido! Tente novamente!\n'
                                                menu_cadastrar(self, error)
                                    else:
                                        clear()
                                        error =' Valor do Serviço inválido! Tente novamente!\n'
                                        menu_cadastrar(self, error)
                            else:
                                clear()
                                error = 'Descrição do Serviço inválido! Tente novamente!\n'
                                menu_cadastrar(self, error)
                else:
                    clear()
                    error = 'ID do Serviço inválido! Tente novamente!\n'
                    menu_cadastrar(self, error)

def atualizar(self, cpf):
    console = Console()
    def atualizar_user(self, option_user):
        match self:
            case 1:
                senha_trade = console.input('[white b]Nova senha: [/]')
                with open(file_users, 'r') as df:
                    next(df)
                    linhas = df.readlines()
                    index = 0
                    for i, row in enumerate(linhas):
                        cpf_user, senha_user, tipo_user = row.split(';')
                        if(cpf_user == cpfs[option_user - 1]):
                            new_line = cpf_user + ';' + senha_trade + ';' + tipo_user
                            index = i
                            break
                    linhas.pop(index)
                    with open(file_users, 'w') as df:
                        df.write('cpf;senha;tipo\n')
                        df.writelines(linhas)
                        df.write(new_line)
                    progress = False

            case 2:
                with open(file_users, 'r') as df:
                    next(df)
                    linhas = df.readlines()
                    index = 0
                    for i, row in enumerate(linhas):
                        cpf_user, senha_user, tipo_user = row.split(';')
                        if (cpf_user == cpfs[option_user - 1]):
                            if(tipo_user.strip() == 'Usuario'):
                                tipo_user = 'Administrador\n'
                            else:
                                tipo_user = 'Usuario\n'
                            new_line = cpf_user + ';' + senha_user + ';' + tipo_user
                            index = i
                            break
                    linhas.pop(index)
                    with open(file_users, 'w') as df:
                        df.write('cpf;senha;tipo\n')
                        df.writelines(linhas)
                        df.write(new_line)
                    progress = False
        clear()
        console.print('[white b]\nA atualização do cliente foi realizada com sucesso![/]', justify='center', width=60)

    def atualizar_cliente(self, option_user):
        match self:
            case 1:
                nome_trade = console.input("[white b]Novo Nome: [/]")
                if validation.isnome(nome_trade):
                    with open(file_clients, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        nome_cliente, sexo_cliente, cpf_cliente, celular_cliente, email_celular, codigo_end_postal_cliente, endereco_cliente, bairro_cliente, complemento_cliente, cidade_cliente, estado_cliente = linhas[option_user - 1].split(";")
                        new_line = nome_trade + ";" + sexo_cliente + ";" + cpf_cliente + ";" + celular_cliente + ";" + email_celular + ";" + codigo_end_postal_cliente + ";" + endereco_cliente + ";" + bairro_cliente + ";" + complemento_cliente + ";" + cidade_cliente + ";" + estado_cliente
                        linhas.pop(option_user - 1)
                        with open(file_clients, "w") as df:
                            df.write("nome;sexo;cpf;celular;email;codigo_end_postal;endereco;bairro;complemento;cidade;estado\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    clear()
                    console.print("[red b]\nNome inválido! Tente novamente![/]", justify='center', width=60)

            case 2:
                sexo_trade = console.input("[white b]Novo Sexo: [/]")
                if validation.issexo(sexo_trade):
                    with open(file_clients, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        nome_cliente, sexo_cliente, cpf_cliente, celular_cliente, email_celular, codigo_end_postal_cliente, endereco_cliente, bairro_cliente, complemento_cliente, cidade_cliente, estado_cliente = linhas[option_user - 1].split(";")
                        new_line = nome_cliente + ";" + sexo_trade + ";" + cpf_cliente + ";" + celular_cliente + ";" + email_celular + ";" + codigo_end_postal_cliente + ";" + endereco_cliente + ";" + bairro_cliente + ";" + complemento_cliente + ";" + cidade_cliente + ";" + estado_cliente
                        linhas.pop(option_user - 1)
                        with open(file_clients, "w") as df:
                            df.write("nome;sexo;cpf;celular;email;codigo_end_postal;endereco;bairro;complemento;cidade;estado\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    clear()
                    console.print("[red b]\nSexo inválido! Tente novamente![/]", justify='center', width=60)

            case 3:
                cpf_trade = console.input("[white b]Novo CPF: [/]")
                if validation.iscpf(cpf_trade):
                    with open(file_clients, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        nome_cliente, sexo_cliente, cpf_cliente, celular_cliente, email_celular, codigo_end_postal_cliente, endereco_cliente, bairro_cliente, complemento_cliente, cidade_cliente, estado_cliente = linhas[option_user - 1].split(";")
                        new_line = nome_cliente + ";" + sexo_cliente + ";" + cpf_trade + ";" + celular_cliente + ";" + email_celular + ";" + codigo_end_postal_cliente + ";" + endereco_cliente + ";" + bairro_cliente + ";" + complemento_cliente + ";" + cidade_cliente + ";" + estado_cliente
                        linhas.pop(option_user - 1)
                        with open(file_clients, "w") as df:
                            df.write("nome;sexo;cpf;celular;email;codigo_end_postal;endereco;bairro;complemento;cidade;estado\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    clear()
                    console.print("[red b]\nCPF inválido! Tente novamente! [/]", justify='center', width=60)

            case 4:
                celular_trade = console.input("[white b]Novo Número de Celular: +55[/]")
                if validation.iscelular(celular_trade):
                    with open(file_clients, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        nome_cliente, sexo_cliente, cpf_cliente, celular_cliente, email_celular, codigo_end_postal_cliente, endereco_cliente, bairro_cliente, complemento_cliente, cidade_cliente, estado_cliente = linhas[option_user - 1].split(";")
                        new_line = nome_cliente + ";" + sexo_cliente + ";" + cpf_cliente + ";" + celular_trade + ";" + email_celular + ";" + codigo_end_postal_cliente + ";" + endereco_cliente + ";" + bairro_cliente + ";" + complemento_cliente + ";" + cidade_cliente + ";" + estado_cliente
                        linhas.pop(option_user - 1)
                        with open(file_clients, "w") as df:
                            df.write("nome;sexo;cpf;celular;email;codigo_end_postal;endereco;bairro;complemento;cidade;estado\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    clear()
                    console.print("[red b]\nNúmero de celular inválido! Tente novamente! [/]", justify='center', width=60)

            case 5:
                email_trade = console.input("[white b]Novo Email: [/]")
                if validation.isemail(email_trade):
                    with open(file_clients, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        nome_cliente, sexo_cliente, cpf_cliente, celular_cliente, email_celular, codigo_end_postal_cliente, endereco_cliente, bairro_cliente, complemento_cliente, cidade_cliente, estado_cliente = linhas[option_user - 1].split(";")
                        new_line = nome_cliente + ";" + sexo_cliente + ";" + cpf_cliente + ";" + celular_cliente + ";" + email_trade + ";" + codigo_end_postal_cliente + ";" + endereco_cliente + ";" + bairro_cliente + ";" + complemento_cliente + ";" + cidade_cliente + ";" + estado_cliente
                        linhas.pop(option_user - 1)
                        with open(file_clients, "w") as df:
                            df.write("nome;sexo;cpf;celular;email;codigo_end_postal;endereco;bairro;complemento;cidade;estado\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    console.print("[red b]\nEmail inválido! Tente novamente! [/]", justify='center', width=60)

            case 6:
                codigo_end_postal_trade = console.input("[white b]Novo CEP: [/]")
                endereco_novo, cep = validation.iscep(codigo_end_postal_trade)
                if cep:
                    with open(file_clients, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        nome_cliente, sexo_cliente, cpf_cliente, celular_cliente, email_celular, codigo_end_postal_cliente, endereco_cliente, bairro_cliente, complemento_cliente, cidade_cliente, estado_cliente = linhas[option_user - 1].split(";")
                        new_line = nome_cliente + ";" + sexo_cliente + ";" + cpf_cliente + ";" + celular_cliente + ";" + email_celular + ";" + unidecode(endereco_novo["cep"]) + ";" + unidecode(endereco_novo["street"]) + ";" + unidecode(endereco_novo["district"]) + ";" + unidecode(endereco_novo["complement"]) + ";" + unidecode(endereco_novo["city"]) + ";" + unidecode(endereco_novo["uf"]) + "\n"
                        linhas.pop(option_user - 1)
                        with open(file_clients, "w") as df:
                            df.write("nome;sexo;cpf;celular;email;codigo_end_postal;endereco;bairro;complemento;cidade;estado\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    console.print("[red b]\nCEP inválido! Tente novamente! [/]", justify='center', width=60)

    def atualizar_pet(self, option_user):
        match self:
            case 1:
                nome_pet_trade = console.input("[white b]Novo Nome do Pet: [/]")
                if validation.isnome(nome_pet_trade):
                    with open(file_pets, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = linhas[option_user - 1].split(";")
                        new_line = id_pet + ';' + nome_pet_trade + ';' + categoria_pet + ';' + raca_pet + ';' + data_nascimento_pet + ';' + cpf_dono_pet
                        linhas.pop(option_user - 1)
                        with open(file_pets, "w") as df:
                            df.write("id_pet;nome_pet;categoria_pet;raca_pet;data_nascimento_pet;cpf_dono_pet\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    clear()
                    console.print("[red b]\nNome do Pet inválido! Tente novamente! [/]", justify='center', width=60)

            case 2:
                categoria_pet_trade = console.input("[white b]Nova Categoria do Pet: [/]")
                if validation.iscategoria(categoria_pet_trade):
                    with open(file_pets, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = linhas[option_user - 1].split(";")
                        new_line = id_pet + ';' + nome_pet + ';' + categoria_pet_trade + ';' + raca_pet + ';' + data_nascimento_pet + ';' + cpf_dono_pet
                        linhas.pop(option_user - 1)
                        with open(file_pets, "w") as df:
                            df.write("id_pet;nome_pet;categoria_pet;raca_pet;data_nascimento_pet;cpf_dono_pet\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    console.print("[red b]\nCategoria do Pet inválido! Tente novamente! [/]", justify='center', width=60)

            case 3:
                raca_pet_trade = console.input("[white b]Nova Raça do Pet: [/]")
                if validation.israca(raca_pet_trade):
                    with open(file_pets, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = linhas[option_user - 1].split(";")
                        new_line = id_pet + ';' + nome_pet + ';' + categoria_pet + ';' + raca_pet_trade + ';' + data_nascimento_pet + ';' + cpf_dono_pet
                        linhas.pop(option_user - 1)
                        with open(file_pets, "w") as df:
                            df.write("id_pet;nome_pet;categoria_pet;raca_pet;data_nascimento_pet;cpf_dono_pet\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    clear()
                    console.print("[red b]\nRaça do Pet inválido! Tente novamente! [/]", justify='center', width=60)

            case 4:
                data_nascimento_pet_trade = console.input("[white b]Nova Data de Nascimento do Pet: [/]")
                if validation.isdataNascimento(data_nascimento_pet_trade):
                    with open(file_pets, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = linhas[option_user - 1].split(";")
                        new_line = id_pet + ';' + nome_pet + ';' + categoria_pet + ';' + raca_pet + ';' + data_nascimento_pet_trade + ';' + cpf_dono_pet
                        linhas.pop(option_user - 1)
                        with open(file_pets, "w") as df:
                            df.write("id_pet;nome_pet;categoria_pet;raca_pet;data_nascimento_pet;cpf_dono_pet\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    clear(0)
                    console.print("[red b]\nData de Nascimento do Pet inválido! Tente novamente! [/]", justify='center', width=60)

            case 5:
                cpf_dono_pet_trade = console.input("[white b]Novo CPF do Dono do Pet: [/]")
                if validation.iscpf(cpf_dono_pet_trade):
                    with open(file_pets, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = linhas[option_user - 1].split(";")
                        new_line = id_pet + ';' + nome_pet + ';' + categoria_pet + ';' + raca_pet + ';' + data_nascimento_pet + ';' + cpf_dono_pet_trade + '\n'
                        linhas.pop(option_user - 1)
                        with open(file_pets, "w") as df:
                            df.write("id_pet;nome_pet;categoria_pet;raca_pet;data_nascimento_pet;cpf_dono_pet\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    clear()
                    console.print("[red b]\nCPF do Dono do Pet inválido! Tente novamente! [/]", justify='center', width=60)

    def atualizar_servico(self, option_user):
        match self:
            case 1:
                descricao_servico_trade = console.input("[white b]Nova Descrição do Serviço: [/]")
                if validation.checkString(descricao_servico_trade):
                    with open(file_services, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        id_servico, descricao_servico, valor_servico, orientacao_servico = linhas[option_user - 1].split(";")
                        new_line = id_servico + ';' + descricao_servico_trade + ';' + valor_servico + ';' + orientacao_servico
                        linhas.pop(option_user - 1)
                        with open(file_services, "w") as df:
                            df.write("id_servico;descricao_servico;valor_servico;orientacao_servico\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    clear()
                    console.print("[red b]\nDescrição do Serviço inválido! Tente novamente! [/]", justify='center', width=60)

            case 2:
                valor_servico_trade = console.input("[white b]Nova Valor do Serviço: [/]")
                if validation.checkString(valor_servico_trade):
                    with open(file_services, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        id_servico, descricao_servico, valor_servico, orientacao_servico = linhas[option_user - 1].split(";")
                        new_line = id_servico + ';' + descricao_servico + ';' + valor_servico_trade + ';' + orientacao_servico
                        linhas.pop(option_user - 1)
                        with open(file_services, "w") as df:
                            df.write("id_servico;descricao_servico;valor_servico;orientacao_servico\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    clear()
                    console.print("[red b]\nValor do Serviço inválido! Tente novamente! [/]", justify='center', width=60)

            case 3:
                orientacao_servico_trade = console.input("[white b]Nova Orientação do Serviço: [/]")
                if validation.checkString(orientacao_servico_trade):
                    with open(file_services, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        id_servico, descricao_servico, valor_servico, orientacao_servico = linhas[option_user - 1].split(";")
                        new_line = id_servico + ';' + descricao_servico + ';' + valor_servico + ';' + orientacao_servico_trade + '\n'
                        linhas.pop(option_user - 1)
                        with open(file_services, "w") as df:
                            df.write("id_servico;descricao_servico;valor_servico;orientacao_servico\n")
                            df.writelines(linhas)
                            df.write(new_line)
                else:
                    clear()
                    console.print("[red b]\nOrientação do Serviço inválido! Tente novamente! [/]", justify='center', width=60)

    match self:
        case 1:
            progress = True
            while progress:
                menu_atualizar(self, 0)
                with open(file_users, "r") as df:
                    next(df)
                    cont = 0
                    cpfs = []
                    linhas = df.readlines()
                    for row in linhas:
                        cpf_user, senha_user, tipo_user = row.split(";")
                        if cpf_user != cpf:
                            cpfs.append(cpf_user)
                            console.print(f"[white b][{cont + 1}][/] [red b]{cpf_user}[/]")
                            cont += 1
                console.print(f"[white b][{cont + 1}][/] [red b]Voltar[/]")

                option_user = int(console.input("[white b]Insira sua opção: [/]"))
                clear()
                if option_user <= cont:
                    while progress:
                        menu_atualizar(self, 0)
                        console.print("[white b][1][/] [red b]Senha[/]")
                        console.print("[white b][2][/] [red b]Tipo[/]")
                        console.print("[white b][3][/] [red b]Voltar[/]")
                        option = int(console.input("[white b]Insira sua opção: [/]"))
                        print("")
                        if option <= 2:
                            atualizar_user(option, option_user)
                            progress = False
                            clear()
                            console.print('[white b]\nA atualização do usuário foi realizada com sucesso![/]', justify='center', width=60)
                        elif option == 3:
                            clear()
                            break
                        else:
                            console.print('[red b]\nOpção inválida! Tente novamente![/]', justify='center', width=60)

                elif option_user == cont + 1:
                    clear()
                    break

                else:
                    clear()
                    error = '[red b]Opção inválida! Tente novamente! [/]\n'
                    menu_cadastrar(self, error)

        case 2:
            progress = True
            while progress:
                menu_atualizar(self, 0)
                with open(file_clients, "r") as df:
                    next(df)
                    linhas = df.readlines()
                    for i, row in enumerate(linhas):
                        nome_cliente, sexo_cliente, cpf_cliente, celular_cliente, email_celular, codigo_end_postal_cliente, endereco_cliente, bairro_cliente, complemento_cliente, cidade_cliente, estado_cliente = row.split(";")
                        console.print(f"[white b][{i + 1}][/] [red b]{nome_cliente} [{cpf_cliente}][/]")
                console.print(f"[white b][{i + 2}][/] [red b]Voltar[/]")

                option_user = int(console.input("[white b]Insira sua opção: [/]"))
                clear()
                if option_user - 1 <= i:
                    while progress:
                        menu_atualizar(self, 0)
                        console.print("[white b][1][/] [red b]Nome[/]")
                        console.print("[white b][2][/] [red b]Sexo[/]")
                        console.print("[white b][3][/] [red b]CPF[/]")
                        console.print("[white b][4][/] [red b]Celular[/]")
                        console.print("[white b][5][/] [red b]Email[/]")
                        console.print("[white b][6][/] [red b]CEP[/]")
                        console.print("[white b][7][/] [red b]Voltar[/]")
                        option = int(console.input("[white b]Insira sua opção: [/]"))
                        print("")
                        if option <= 6:
                            atualizar_cliente(option, option_user)
                            progress = False
                            clear()
                            console.print('[white b]\nA atualização do cliente foi realizada com sucesso![/]', justify='center', width=60)
                        elif option == 7:
                            clear()
                            break
                        else:
                            console.print("[red b]\nOpção inválida! Tente novamente![/]", justify='center', width=60)
                elif option_user == i + 2:
                    clear()
                    break

                else:
                    clear()
                    error = '[red b]Opção inválida! Tente novamente! [/]\n'
                    menu_atualizar(self, error)

        case 3:
            progress = True
            while progress:
                menu_atualizar(self, 0)
                with open(file_pets, "r") as df:
                    next(df)
                    linhas = df.readlines()
                    for i, row in enumerate(linhas):
                        id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = row.split(";")
                        console.print(f"[white b][{i + 1}][/] [red b]{nome_pet} [{cpf_dono_pet.strip()}][/]")
                console.end_captureprint(f"[white b][{i + 2}][/] [red b]Voltar[/]")

                option_user = int(console.input("[white b]Insira sua opção: [/]"))
                clear()
                if option_user - 1 <= i:
                    while progress:
                        menu_atualizar(self, 0)
                        console.print("[white b][1][/] [red b]Nome[/]")
                        console.print("[white b][2][/] [red b]Categoria[/]")
                        console.print("[white b][3][/] [red b]Raça[/]")
                        console.print("[white b][4][/] [red b]Data de nascimento[/]")
                        console.print("[white b][5][/] [red b]CPF do Dono[/]")
                        console.print("[white b][6][/] [red b]Voltar[/]")
                        option = int(console.input("[white b]Insira sua opção: [/]"))
                        print("")
                        if option <= 5:
                            atualizar_pet(option, option_user)
                            progress = False
                            clear()
                            console.print('[white b]\nA atualização do pet foi realizada com sucesso![/]', justify='center', width=60)
                        elif option == 6:
                            clear()
                            break
                        else:
                            console.print("[red b]\nOpção inválida! Tente novamente![/]", justify='center', width=60)
                elif option_user == i + 2:
                    clear()
                    break

                else:
                    clear()
                    error = '[red b]Opção inválida! Tente novamente! [/]\n'
                    menu_atualizar(self, error)

        case 4:
            progress = True
            while progress:
                menu_atualizar(self, 0)
                with open(file_services, "r") as df:
                    next(df)
                    linhas = df.readlines()
                    for i, row in enumerate(linhas):
                        id_servico, descricao_servico, valor_servico, orientacao_servico = row.split(";")
                        console.print(f"[white b][{i + 1}][/] [red b]{descricao_servico}[/]")
                console.print(f"[white b][{i + 2}][/] [red b]Voltar[/]")

                option_user = int(console.input("[white b]Insira sua opção: [/]"))
                clear()
                if option_user - 1 <= i:
                    while progress:
                        menu_atualizar(self, 0)
                        console.print("[white b][1][/] [red b]Descrição[/]")
                        console.print("[white b][2][/] [red b]Valor[/]")
                        console.print("[white b][3][/] [red b]Orientação[/]")
                        console.print("[white b][4][/] [red b]Voltar[/]")
                        option = int(console.input("[white b]Insira sua opção: [/]"))
                        print("")
                        if option <= 3:
                            atualizar_servico(option, option_user)
                            progress = False
                            clear()
                            console.print('[white b]\nA atualização do serviço foi realizada com sucesso![/]', justify='center', width=60)
                        elif option == 4:
                            clear()
                            break
                        else:
                            console.print("[red b]\nOpção inválida! Tente novamente![/]", justify='center', width=60)
                elif option_user == i + 2:
                    clear()
                    break

                else:
                    clear()
                    error = 'Opção inválida! Tente novamente!\n'
                    menu_atualizar(self, error)

def apagar(self, cpf):
    console = Console()
    match self:
        case 1:
            progress = True
            while progress:
                menu_apagar(self, 0)
                with open(file_users, "r") as df:
                    next(df)
                    cont = 0
                    cpfs = []
                    linhas = df.readlines()
                    for row in linhas:
                        cpf_user, senha_user, tipo_user = row.split(";")
                        if cpf_user != cpf:
                            cpfs.append(cpf_user)
                            console.print(f"[white b][{cont + 1}][/] [red b]{cpf_user}[/]")
                            cont += 1
                console.print(f"[white b][{cont + 1}][/] [red b]Voltar[/]")
                option_user = int(console.input("[white b]Insira sua opção: [/]"))
                if option_user <= cont:
                    with open(file_users, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        cpf_user, senha_user, tipo_user = linhas[option_user].split(";")
                        if option_user == 1:
                            linhas.pop(option_user - 1)
                        elif option_user > 1:
                            if cpf_user == cpf:
                                linhas.pop(option_user - 1)
                            else:
                                linhas.pop(option_user)
                        with open(file_users, "w") as df:
                            df.write("cpf;senha;tipo\n")
                            df.writelines(linhas)
                        progress = False
                        clear()
                        console.print('[white b]\nO usuário foi apagado com sucesso![/]', justify='center', width=60)
                elif option_user == cont + 1:
                    clear()
                    break

                else:
                    clear()
                    error = 'Opção inválida! Tente novamente! \n'
                    menu_apagar(self, error)

        case 2:
            progress = True
            while progress:
                menu_apagar(self, 0)
                with open(file_clients, "r") as df:
                    next(df)
                    linhas = df.readlines()
                    for i, row in enumerate(linhas):
                        nome_cliente, sexo_cliente, cpf_cliente, celular_cliente, email_celular, codigo_end_postal_cliente, endereco_cliente, bairro_cliente, complemento_cliente, cidade_cliente, estado_cliente = row.split(";")
                        console.print(f"[white b][{i + 1}][/] [red b]{nome_cliente} [{cpf_cliente}][/]")
                console.print(f"[white b][{i + 2}][/] [red b]Voltar[/]")

                option_user = int(console.input("[white b]Insira sua opção: [/]"))
                clear()
                if option_user - 1 <= i:
                    with open(file_clients, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        nome_cliente, sexo_cliente, cpf_cliente, celular_cliente, email_celular, codigo_end_postal_cliente, endereco_cliente, bairro_cliente, complemento_cliente, cidade_cliente, estado_cliente = linhas[option_user - 1].split(";")
                        linhas.pop(option_user - 1)

                    with open(file_clients, "w") as df:
                        df.write("nome;sexo;cpf;celular;email;codigo_end_postal;endereco;bairro;complemento;cidade;estado\n")
                        df.writelines(linhas)
                    progress = False
                    clear()
                    console.print('[white b]\nO cliente foi apagado com sucesso![/]', justify='center', width=60)

                elif option_user == i + 2:
                    clear()
                    break

                else:
                    clear()
                    error = 'Opção inválida! Tente novamente! \n'
                    menu_apagar(self, error)

        case 3:
            progress = True
            while progress:
                with open(file_pets, "r") as df:
                    next(df)
                    linhas = df.readlines()
                    for i, row in enumerate(linhas):
                        id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = row.split(";")
                        console.print(f"[white b][{i + 1}][/] [red b]{nome_pet} [{cpf_dono_pet.strip()}][/]")
                console.print(f"[white b][{i + 2}][/] [red b]Voltar[/]")

                option_user = int(console.input("[white b]Insira sua opção: [/]"))
                clear()
                if option_user - 1 <= i:
                    with open(file_pets, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = linhas[option_user - 1].split(";")
                        linhas.pop(option_user - 1)

                    with open(file_pets, "w") as df:
                        df.write("nome;sexo;cpf;celular;email;codigo_end_postal;endereco;bairro;complemento;cidade;estado\n")
                        df.writelines(linhas)
                    progress = False
                    clear()
                    console.print('[white b]\nO pet foi apagado com sucesso![/]', justify='center', width=60)

                elif option_user == i + 2:
                    clear()
                    break

                else:
                    clear()
                    error = 'Opção inválida! Tente novamente! \n'
                    menu_apagar(self, error)

        case 4:
            progress = True
            while progress:
                with open(file_services, "r") as df:
                    next(df)
                    linhas = df.readlines()
                    for i, row in enumerate(linhas):
                        id_servico, descricao_servico, valor_servico, orientacao_servico = row.split(";")
                        console.print(f"[white b][{i + 1}][/] [red b]{descricao_servico}[/]")
                console.print(f"[white b][{i + 2}][/] [red b]Voltar[/]")

                option_user = int(console.input("[white b]Insira sua opção: [/]"))
                clear()
                if option_user - 1 <= i:
                    with open(file_services, "r") as df:
                        next(df)
                        linhas = df.readlines()
                        id_servico, descricao_servico, valor_servico, orientacao_servico = linhas[option_user - 1].split(";")
                        linhas.pop(option_user - 1)

                    with open(file_services, "w") as df:
                        df.write("id_servico;descricao_servico;valor_servico;orientacao_servico\n")
                        df.writelines(linhas)
                    progress = False
                    clear()
                    console.print('[white b]\nO serviço foi apagado com sucesso![/]', justify='center', width=60)

                elif option_user == i + 2:
                    clear()
                    break

                else:
                    clear()
                    error = 'Opção inválida! Tente novamente! \n'
                    menu_apagar(self, error)

def consultar(self):
    console = Console()
    match self:
        case 1:
            progress = True
            while progress:
                menu_consultar('USUÁRIOS')
                with open(file_users, "r") as df:
                    next(df)
                    linhas = df.readlines()
                    for i, row in enumerate(linhas):
                        cpf_user, senha_user, tipo_user = row.split(";")
                        console.print(f"[white b][{i + 1}][/] [red b]{cpf_user}[/]")
                total = f'TOTAL DE USUÁRIOS: {i + 1}'
                total_consulta(total)
                progress = False

        case 2:
            progress = True
            while progress:
                menu_consultar('CLIENTES')
                with open(file_clients, "r") as df:
                    next(df)
                    linhas = df.readlines()
                    for i, row in enumerate(linhas):
                        nome_cliente, sexo_cliente, cpf_cliente, celular_cliente, email_celular, codigo_end_postal_cliente, endereco_cliente, bairro_cliente, complemento_cliente, cidade_cliente, estado_cliente = row.split(";")
                        console.print(f"[white b][{i + 1}][/] [red b]{nome_cliente} [{cpf_cliente}][/]")
                    total = f'TOTAL DE CLIENTES: {i + 1}'
                    total_consulta(total)
                    progress = False

        case 3:
            progress = True
            while progress:
                menu_consultar('PETS')
                with open(file_pets, "r") as df:
                    next(df)
                    linhas = df.readlines()
                    for i, row in enumerate(linhas):
                        id_pet, nome_pet, categoria_pet, raca_pet, data_nascimento_pet, cpf_dono_pet = row.split(";")
                        console.print(f"[white b][{i + 1}][/] [red b]{nome_pet} [{cpf_dono_pet.strip()}][/]")
                    total = f'TOTAL DE PETS: {i + 1}'
                    total_consulta(total)
                    progress = False

        case 4:
            progress = True
            while progress:
                menu_consultar('SERVIÇOS')
                with open(file_services, "r") as df:
                    next(df)
                    linhas = df.readlines()
                    for i, row in enumerate(linhas):
                        id_servico, descricao_servico, valor_servico, orientacao_servico = row.split(";")
                        console.print(f"[white b][{i + 1}][/] [red b]{descricao_servico}[/]")
                    total = f'TOTAL DE SERVIÇOS: {i + 1}'
                    total_consulta(total)
                    progress = False