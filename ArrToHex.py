def decode(data):
    code = ""
    for i in data:
        if i > 0:
            code += "1"
        else:
            code += "0"

    value = hex(int(code,2))
    print value
    return value
