def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    first_line = []
    second_line = []
    separator_line = []
    answer_line = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Each problem must contain three parts (operand1, operator, operand2)."

        operand1, operator, operand2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        first_line.append(operand1.rjust(width))
        second_line.append(operator + ' ' + operand2.rjust(width - 2))
        separator_line.append('-' * width)

        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))

            answer_line.append(answer.rjust(width))

    arranged_problems.append('    '.join(first_line))
    arranged_problems.append('    '.join(second_line))
    arranged_problems.append('    '.join(separator_line))

    if show_answers:
        arranged_problems.append('    '.join(answer_line))

    return '\n'.join(arranged_problems)