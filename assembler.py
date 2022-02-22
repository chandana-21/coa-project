opc_table = {} # stores opcodes of the program like { opcode : bin_opcode }
lab_table = {} # stores Label addresses like { label : location_address }
var_table = {} # stores variables like { variable : [value, location_address, size] }
lit_table = {} # stores literals like { literal : address}

keywords = ['CLA','LAC','SAC','ADD','SUB','BRZ','BRN', 'BRP','INP', 'DSP', 'MUL', 'DIV', 'STP', 'DEC']

code = ['CLA',
        'INP A ',
        'INP B',
        'LAC A; checking comments',
        "SUB '=3'",
        'BRN L2',
        'DSP L1',
        'CLA',
        'BRZ L2',
        'L1 ~ DSP B',
        'CLA',
        'BRZ L2',
        'L2 ~ STP',
        'A DEC ',
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


def add_opcode(opcode, bin_opcode):
    if list(opc_table.keys()).count(opcode)==0:
        opc_table[opcode] = [bin_opcode]


def get_variable(line):
    value = 0
    size = 12
    parts = line.upper().split()
    i = parts.count("DEC")
    if i==0:
        return None, None, None
    elif i>1 or len(parts)>3:
        return 0,0,0 #error
    variable = parts[0].strip()
    if variable.isdigit():
        return 0,0,0 #error
    if len(parts)==3:
        value = parts[2].strip()
        if not value.isdigit():
            return 0,0,0 #error
    value = int(value)
    return variable, value, size   


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
        variable, value, size = get_variable(line)
        if variable==0 and value==0 and size==0:
            return "error"
        if variable==None:
            return "error"
        # To be continued 


def pass_one():

    location_counter = 0

    for line in code:
        roline = check_comment(line)
        label, roline = get_label(roline)

        if label != ' ':
            i = add_label(label, location_counter)
            if i==0:
                print("Error! Label has already been defined once")
            if i==1:
                print("Error!",label, " has been declared as a Variable already!")
            if i==2:
                print("Error!",label, " is a reserved keyword, can't be used as a label")
        
        pass_one_code.append(roline)
        get_opcode(roline)

    return pass_one_code

# code = pass_one()
# print(code)
# print(opc_table)



























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