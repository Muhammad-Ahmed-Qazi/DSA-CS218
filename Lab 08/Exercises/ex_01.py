from stack import Stack

operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0, ')': 0}

def is_higher_precedence(op1, op2):
    return operators[op1] > operators[op2]

def calculate(op, b, a):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b
    elif op == '^': return a ** b

# def operate(operator, operator_stack, operand_stack):
#     if operator == '(':
#         operator_stack.push(operator)
#         return
#     while operators[operator] <= operators[operator_stack.top()]:
#         topOp = operator_stack.pop()
#         if topOp in operators and topOp not in '()':
#             right = operand_stack.pop()
#             left = operand_stack.pop()
#             result = calculate(topOp, right, left)
#             operand_stack.push(result)
#         elif topOp == '(' and operator == ')':
#             return
#     operator_stack.push(operator)
#     return

def operate(operator, operator_stack, operand_stack):
    if operator == '(':
        operator_stack.push(operator)
        return

    while (
        operator_stack.top() != '(' and
        (
            operators[operator] < operators[operator_stack.top()] or
            (operators[operator] == operators[operator_stack.top()] and operator != '^')
        )
    ):
        topOp = operator_stack.pop()
        if topOp not in '()':
            right = operand_stack.pop()
            left = operand_stack.pop()
            result = calculate(topOp, right, left)
            operand_stack.push(result)
        elif topOp == '(' and operator == ')':
            return

    if operator != ')':
        operator_stack.push(operator)
    else:
        operator_stack.pop()  # pop '('

def infix_to_postfix(expression):
    stack = Stack()
    p = None
    i = 0
    tokens = expression.split() + [')']
    token  = tokens[0]
    stack.push('(')

    while stack.is_empty() == False:
        if token not in operators:
            p = (p + ' ' + token) if p else token
        elif token == '(':
            stack.push(token)
        elif token in operators and token != ')':
            while stack.is_empty() == False and stack.top() != '(' and is_higher_precedence(stack.top(), token):
                p = (p + ' ' + stack.pop()) if p else stack.pop()
            stack.push(token)
        elif token == ')':
            while stack.is_empty() == False and stack.top() != '(':
                p = (p + ' ' + stack.pop()) if p else stack.pop()
            stack.pop()
        if i < len(tokens) - 1:
            i += 1
            token = tokens[i]
    
    return p

def evaluate_infix(expression):
    operator_stack = Stack()
    operand_stack  = Stack()
    tokens = expression.split() + [')']
    operator_stack.push('(')

    for token in tokens:
        if token not in operators:
            operand_stack.push(int(token))
        else:
                operate(token, operator_stack, operand_stack)
        print(token, "|", operator_stack.display(), "|", operand_stack.display())

    return operand_stack.pop()

def evaluate_postfix(expression):
    stack  = Stack()
    i = 0
    tokens = expression.split() + [')']
    token  = tokens[0]

    while token != ')':
        if token not in operators:
            stack.push(int(token))
        else:
            right = stack.pop()
            left  = stack.pop()
            stack.push(calculate(token, right, left))
        i += 1
        token = tokens[i]
    
    return stack.pop()

# Main program
if __name__ == '__main__':
    # infix = '3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'
    infix = '( 6 + 5 ) * 4 - 9'
    postfix = infix_to_postfix(infix)
    print(f'Infix: {infix}')
    print(f'Postfix: {postfix}')
    print(f'Infix Evaluation: {evaluate_infix(infix)}')
    print(f'Postfix Evaluation: {evaluate_postfix(postfix)}')