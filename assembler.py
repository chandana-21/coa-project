opc_table = {} # stores opcodes of the program like { opcode : bin_opcode }
lab_table = {} # stores Label addresses like { label : location_address }
var_table = {} # stores variables like { variable : [value, location_address] }
lit_table = {} # stores literals like { literal : [value, location_address]}

keywords = ['CLA','LAC','SAC','ADD','SUB','BRZ','BRN', 'BRP','INP', 'DSP', 'MUL', 'DIV', 'STP', 'DEC']

code = ['CLA',
        'INP A ',
        'INP B',
        'LAC A ; checking comments',
        "SUB =3",
        'BRN L2',
        'DSP L1',
        'CLA',
        'BRZ L2',
        'L1 ~ DSP B',
        'CLA',
        'BRZ L2',
        'L2 ~ STP',
        'A DEC ',
        # 'L2 ~ STP',
        'B DEC 125']

pass_one_code = []


def check_comment(line):
    i = -1
    i = line.find(';')
    if i!=-1:
        line = line[:i].strip()

    return line 


def get_label(line):
    i = -1
    label = ' '
    i = line.find('~')
    if i != -1:
        label = line[:i].strip()
        line = line[i+1:].strip()

    return label, line


def duplicate_label(label):
    if list(lab_table.keys()).count(label)>0:
        return True
    else:
        return False


def duplicate_variable(label):
    if list(var_table.keys()).count(label)>0:
        return True
    else:
        return False


def add_label(label, location_counter):
    if duplicate_label(label):
        return 0 #error
    elif duplicate_variable(label):
        return 1 #error
    elif label in keywords :
        return 2 #error
    else:
        lab_table[label] = location_counter
        return 3


def label_error(num,label):
    if num==0:
        print("Error!",label, " has been declared as a Label already!")
    if num==1:
        print("Error!",label, " has been declared as a Variable already!")
    if num==2:
        print("Error!",label, " is a Reserved Keyword, can't be used as a Label")
        


def add_opcode(opcode, bin_opcode):
    if list(opc_table.keys()).count(opcode)==0:
        opc_table[opcode] = [bin_opcode]


def get_opcode(line):
    opcodes = line.upper().split()

    if opcodes.count('CLA') + opcodes.count('LAC') + opcodes.count('SAC') + opcodes.count('ADD') + opcodes.count('SUB') + opcodes.count('BRZ') + opcodes.count('BRN') + opcodes.count('BRP') + opcodes.count('INP') + opcodes.count('DSP') + opcodes.count('MUL') + opcodes.count('DIV') + opcodes.count('STP') + opcodes.count('DEC') > 1:
        return 0 # error! declare opcodes only once

    if opcodes.count('CLA') == 1:
        add_opcode('CLA',"0000" )

    elif opcodes.count('LAC') == 1:
        add_opcode('LAC', "0001")

    elif opcodes.count('SAC') == 1:
        add_opcode('SAC', "0010")

    elif opcodes.count('ADD') == 1:
        add_opcode('ADD', "0011")

    elif opcodes.count('SUB') == 1:
        add_opcode('SUB', "0100")
    elif opcodes.count('BRZ') == 1:
        add_opcode('BRZ', "0101")

    elif opcodes.count('BRN') == 1:
        add_opcode('BRN', "0110")

    elif opcodes.count('BRP') == 1:
        add_opcode('BRP', "0111")

    elif opcodes.count('INP') == 1:
        add_opcode('INP', "1000")

    elif opcodes.count('DSP') == 1:
        add_opcode('DSP', "1001")

    elif opcodes.count('MUL') == 1:
        add_opcode('MUL', "1010")

    elif opcodes.count('DIV') == 1:
        add_opcode('DIV', "1011")

    elif opcodes.count('STP') == 1:
        add_opcode('STP',"1100")
    else:
        pass
        # variable, value = get_variable(line)#, size
        # # if variable==0 and value==0 : #and size==0
        # #     return "error"
        # if variable==None:
        #     return "error"
        # num = add_variable(variable, value)#, size
        # if num==0:
        #     print("Error!",variable, " has been declared as a Label already!")
        # if num==1:
        #     print("Error!",variable, " has been declared as a Variable already!")
        # if num==2:
        #     print("Error!",variable, " is a Reserved Keyword, can't be used as a Variable")


def get_variable(line):
    value = 0 # default value of the variable
    # size = 12
    parts = line.upper().split()
    i = parts.count('DEC')
    # print(i)#test
    # print(parts)#test
    if i==0:
        return None, None #error
    if i>1 or len(parts)>3:
        return None, None #error
    variable = parts[0].strip()
    if variable.isdigit():
        return None, None #error
    if i==1 and len(parts)==3:
        value = parts[2].strip()
        if not value.isdigit():
            # print("n")#test
            return None, None #error
    value = int(value)
    return variable, value#, size   


def add_variable(variable, value): #, size
    if duplicate_label(variable):
        return 0 #error
    elif duplicate_variable(variable):
        return 1 #error
    elif variable in keywords :
        return 2 #error
    else:
        var_table[variable] = [value, -1]
        return 3


def variable_error(num,variable):
    if num==0:
        print("Error!",variable, " has been declared as a Label already!")
    if num==1:
        print("Error!",variable, " has been declared as a Variable already!")
    if num==2:
        print("Error!",variable, " is a Reserved Keyword, can't be used as a Variable")


def add_literal(literal):
    if list(lit_table.keys()).count(literal) == 0:
        parts = literal.split()
        if len(parts)>1:
            return 0
        if len(parts)==1 and literal[1:].isdigit():
            value = literal[1:]
            lit_table[literal] = [value,-1]


def get_literal(line):
    c = line.count('=')
    if c>1:
        return 0
    else:
        i = line.find('=')
        if i!=-1:
            literal = line[i:]
            add_literal(literal)


def address_to_symbols(location_counter):
    for i in lit_table:
        lit_table[i][1] = location_counter
        location_counter = location_counter + 12
    for i in var_table:
        var_table[i][1] = location_counter
        location_counter = location_counter + 12


def pass_one():

    location_counter = 0

    for line in code:
        roline = check_comment(line)
        label, roline = get_label(roline)

        if label != ' ':
            i = add_label(label, location_counter)
            label_error(i,label)
            
        pass_one_code.append(roline)
        get_opcode(roline) 

        variable, value = get_variable(roline)
        if variable != None:
            # print("yes",variable,value)#test
            i = add_variable(variable, value)
            variable_error(i,variable)

        get_literal(roline)# works till here 
        location_counter = location_counter + 12
        
    address_to_symbols(location_counter)
    return pass_one_code

code = pass_one()
print("********* code after pass one ********* \n",code)
print("********* opcode table *********\n", opc_table)
print("********* label table *********\n", lab_table)
print("********* literal table *********\n", lit_table)
print("********* variable table *********\n",var_table)



























# OPC_TABLE["CLA"] = ["0000",0]
# OPC_TABLE["LA"] = ["0001",1]
# OPC_TABLE["SAC"] = ["0010",1]
# OPC_TABLE["ADD"] = ["0011",1]
# OPC_TABLE["SUB"] = ["0100",1]
# OPC_TABLE["BRZ"] = ["0101",1]
# OPC_TABLE["BRN"] = ["0110",1]
# OPC_TABLE["BRP"] = ["0111",1]
# OPC_TABLE["INP"] = ["1000",1]
# OPC_TABLE["DSP"] = ["1001",1]
# OPC_TABLE["MUL"] = ["1010",1]
# OPC_TABLE["DIV"] = ["1011",1]
# OPC_TABLE["STP"] = ["1100",0]