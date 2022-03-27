#!/usr/bin/python3


# Author Md Shohidul Islam 2816885


# It's provide single token every time
def lexan():
    global mitr
    try:
        return next(mitr)
    except StopIteration:
        return ''


# matching the lookahead with the character if it's match then provide next character
def match(ch):
    global lookahead

    if ch == lookahead:
        lookahead = lexan()
    else:
        print('Error: Token Mismatch')
        exit()


# Interpreter starting from this prog() method
def prog():
    global lookahead
    global_decl()
    let_in_end()
    while lookahead == 'let':
        let_in_end()


# Declare global variable with data
def global_decl():
    global lookahead
    global global_variable  # dictionary set global variable name and value as key pair with variable type
    val_type = type()
    id = id_list(val_type)

    match(lookahead)
    exp = expr_list(val_type)
    match(lookahead)
    for i in range(len(exp)):
        global_variable[id[i]] = (exp[i], val_type)

    if lookahead == ';':
        match(';')
        return global_variable


def let_in_end():
    global lookahead

    match('let')
    ld = decl()
    match('in')
    val_type = type()
    match('(')
    result = expr(val_type)
    print(result)  # Print the output for the given test case
    ld.clear()  # Once local variable data being used then reset the local variable dictionary for next interation
    match(')')
    match('end')

    if lookahead == ';':
        match(';')

        return
    else:
        print('Error: In let in ')
        exit()


# Declare local variable in a dictionary
def decl():
    global lookahead
    global l_dic

    val_type = type()
    id = id_list(val_type)
    match(lookahead)
    exp = expr_list(val_type)

    for i in range(len(exp)):
        l_dic[id[i]] = (exp[i], val_type)

    if lookahead == ';':
        match(';')
    return l_dic


# This return the variable name
def id_list(val_type):
    global lookahead

    a = [lookahead]
    match(lookahead)

    while lookahead == ',':
        match(',')
        a.append(lookahead)
        lexan()
    return a


# Return variable data that set to id
def expr_list(val_type):
    global lookahead
    a = []
    ex = expr(val_type)

    a.append(ex)
    match(lookahead)

    while lookahead == ',' or lookahead == 'm':
        match(',') if lookahead == ',' else ''
        ex = expr(val_type)
        a.append(ex)
        match(lookahead)

    return a


# This return variable type
def type():
    global lookahead

    if lookahead == 'int' or lookahead == 'real':
        val = lookahead
        match(lookahead)
        return val

    else:
        print('Error: wrong type')


# Addition and subtraction of the variable happened here
def expr(exp_type):
    global lookahead

    val = term(exp_type)

    while lookahead == '+' or lookahead == '-':

        if lookahead == '+':
            match('+')
            val += term(exp_type)

        else:

            match('-')
            val -= term(exp_type)

    return val


# Multiplication and division of the variable happened here
def term(exp_type):
    global lookahead
    val = factor(exp_type)
    while lookahead == '*' or lookahead == '/':

        if lookahead == '*':
            match('*')
            val *= factor(exp_type)
        elif lookahead == '/':
            match('/')
            val /= factor(exp_type)
        else:
            print('Error: In term')
    return val


# Power of the variable data return here
def factor(exp_type):
    global lookahead

    val = base(exp_type)
    if lookahead == '^':
        match('^')
        val = pow(val, factor(exp_type))
    return val


def base(exp_type):
    global lookahead

    # If data pattern like (value) thus then return data
    if lookahead == '(':
        match('(')
        val = expr(exp_type)
        match(')')

        return val

    # if the value is integer then return value ; checking digits or not
    elif lookahead.isdigit():
        val = int(lookahead)
        if exp_type != 'int':
            exit()
        return val

    # checking number float or not
    elif '.' in lookahead:
        return float(lookahead)

    # here check the variable is existed in local or global variable dictionary and return the value from the dictionary
    elif lookahead in l_dic or lookahead in global_variable:
        if lookahead in l_dic:  # First check in the local dictionary data
            val = lookahead
            match(lookahead)
            # If the data is int then value of the string convert in integer. Else value convert in float.
            return int(l_dic[val][0]) if l_dic[val][1] == 'int' else float(
                l_dic[val][0])
        else:  # check data in the global variable dictionary
            val = lookahead
            match(lookahead)
            # If the data is int then value of the string convert in integer. Else value convert in float.
            return int(global_variable[val][0]) if global_variable[val][1] == 'int' else float(
                global_variable[val][0])

    elif lookahead == 'int' or lookahead == 'real':

        type()

        if lookahead == '(':
            match(lookahead)
            if lookahead in l_dic:
                value = int(l_dic[lookahead][0]) if l_dic[lookahead][1] == 'int' else float(
                    l_dic[lookahead][0])
            else:
                value = int(global_variable[lookahead][0]) if global_variable[lookahead][1] == 'int' else float(
                    global_variable[lookahead][0])

            match(lookahead)
            match(')')
            return value

    else:
        print('Error: in base')


if __name__ == '__main__':  # main function

    import sys  # system call for command line file input

    l_dic = {}  # set local variable data to this dictionary
    global_variable = {}  # # set global variable data to this dictionary
    infile = open(sys.argv[1], 'r')  # reading file
    wlist = infile.read().split()  # split the file based on space between 2 characters or words
    mitr = iter(wlist)  # iterable token list

    lookahead = next(mitr)  # lookahead for the fist token

    prog()

    if lookahead == '':
        exit()
        print('pass')
    else:
        print("Syntax Error1")
