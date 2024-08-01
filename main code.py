while True:

    num_1 = input('Digite um número: ')

    num_2 = input('Digite outro número: ')

    op = input('Digite um operador [+, -, /, *]: ')

    invalido = None

    op_permitido = '+-/*'

  

    try:

        num_1_flt = float(num_1)

        num_2_flt = float(num_2)

        invalido = True

    except ValueError:

        invalido = None

  

    if op not in op_permitido:

        print('Operador inválido.')

        continue

  

    if len(op) > 1:

        print('Digite apenas um operador.')

        continue

  

    if invalido is None:

        print('Erro, operação inválida.')

        continue

  

    if op == '+':

        print(num_1_flt + num_2_flt)

  

    elif op == '-':

        print(num_1_flt - num_2_flt)

  

    elif op == '/':

        if num_2_flt == 0:

            print('Erro, divisão por zero.')

        else:

            print(num_1_flt / num_2_flt)

  

    elif op == '*':

        print(num_1_flt * num_2_flt)

  

    else:

        print('Erro...')

  

    sair = input('Deseja terminar? [s/n]: ').lower().startswith('s')

  

    if sair:

        break
