from typing_extensions import Annotated
from pydantic import  AfterValidator
import re

def validate_npi(query:str)->str:
    query = re.sub(r'[\+\-\*\/]',lambda x: ' ' + x.group(0)+' ', query)
    stack = []
    tokens = query.split()


    for token in tokens:
        if token.isdigit():
            stack.append(float(token))
        else:
            if len(stack) < 2:
                raise ValueError("Invalid NPI expression: insufficient operands")

            n1 = stack.pop()
            n2 = stack.pop()

            if token not in ['+', '-', '*', '/']:
                raise ValueError(f"Unknown operator: {token}")

            stack.append(1)

    if len(stack) != 1:
        raise ValueError("Invalid NPI expression: remaining operands in stack")

    return query.strip().replace("  ", " ")

NPIExpression = Annotated[str, AfterValidator(validate_npi)]
