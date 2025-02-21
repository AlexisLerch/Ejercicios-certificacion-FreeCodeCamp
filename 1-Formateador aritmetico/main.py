def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return  'Error: Too many problems.'

    # Creo un diccionario para almacenar variables
    arranged_problems = {
        'first_line':'',
        'second_line':'',
        'dash_line':'',
        'answer_line':''
    }
    # Creo un for loop para iterar sobre el problema

    for problem in problems:
        # Esto crea un espacio entre operador1, operador y operador2
        operador1, operador, operador2 = problem.split()
        # print(problem.split(), operador1, operador2, operador)
        # Otro operador que no sea + o - return error
        if operador not in ['+' , '-'] :
            return "Error: Operator must be '+' or '-'."

        # Solo acepta digitos
        if not operador1.isdigit() or not operador2.isdigit():
            return 'Error: Numbers must only contain digits.'

        # Cada operador no puede tener mas de 4 digitos
        if len(operador1) > 4 or len(operador2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Create spacing
        width = max(len(operador1), len(operador2)) + 2

        # Agregando al diccionario los valores para hacer la cuentas
        arranged_problems['first_line'] += operador1.rjust(width) + '    '

        arranged_problems['second_line'] += operador + ' ' + operador2.rjust(width - 2) + '    '

        arranged_problems['dash_line'] += '-' * width + '    '

        # If show_answer is true show answer
        if show_answers:
            if operador == '+':
                answer = str(int(operador1) + int(operador2))
            else:
                answer = str(int(operador1) - int(operador2))

            # Ordenando el resultado en el lugar apropiado
            arranged_problems['answer_line'] += answer.rjust(width) + '    ' 

    # Mostar el resultado
    arranged_output = arranged_problems['first_line'].rstrip() + '\n'
    arranged_output += arranged_problems['second_line'].rstrip() + '\n'
    arranged_output += arranged_problems['dash_line'].rstrip()

    if show_answers:
        arranged_output += '\n' + arranged_problems['answer_line'].rstrip()

    return arranged_output
    # return problems

print(f'\n{arithmetic_arranger(["3233 + 1698", "3801 - 2", "45 + 43", "123 + 49"], True)}')

print('______________________________')
