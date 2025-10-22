rator_stack, operand_stack):
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
        operator_