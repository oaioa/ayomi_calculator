from src.core.schemas import NPIExpression

def compute_npi(expression: NPIExpression) -> float:
    print(f"expression: {expression}")
    stack = []
    tokens = expression.split()

    for token in tokens:
        print(f"Stack: {stack}, Token: {token}")
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(float(token))
        else:
            n1 = stack.pop()
            n2 = stack.pop()

            if token == '+':
                stack.append(n1 + n2)
            elif token == '-':
                stack.append(n2 - n1)
            elif token == '*':
                stack.append(n1 * n2)
            elif token == '/':
                stack.append(n2 / n1)

    return stack[0]
