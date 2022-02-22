opc_table = {} # stores opcodes occuring in the program in format { opcode : [bin_opcode, size, inctructionClass] }
lab_table = {} # stores Label addresses { label : location_address }
var_table = {} # stores variables in format { variable : [value, location_address, size] }
lit_table = {} # stores literals in format { literal : address}

keywords = ['CLA','LAC','SAC','ADD','SUB','BRZ','BRN', 'BRP','INP', 'DSP', 'MUL', 'DIV', 'STP', 'DW']

code = []
pass_one_code = []

def check_comment(line):
    i = -1
    i = line.find(';')
    if i!=-1:
        line = line[:i].strip()
    return line 

def get_label(line):
    i = -1
    label = 'nil'
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
        return 0
    elif duplicate_variable(label):
        return 1
    elif label in keywords :
        return 2
    else:
        lab_table[label] = location_counter
        return 3

def add_opcode()

def get_opcode(line):
    opcodes = line.upper().split()

    if opcodes.count('CLA') + opcodes.count('LAC') + opcodes.count('SAC') + opcodes.count('ADD') + opcodes.count('SUB') + opcodes.count('BRZ') + opcodes.count('BRN') + opcodes.count('BRP') + opcodes.count('INP') + opcodes.count('DSP') + opcodes.count('MUL') + opcodes.count('DIV') + opcodes.count('STP') + opcodes.count('DW') > 1:
        return 0 # error declare opcodes only once

    if opcodes.count('CLA') == 1:
        add_opcode('CLA' )
    elif opcodes.count('LAC') == 1:
        add_opcode('LAC' )
    elif opcodes.count('SAC') == 1:
        add_opcode('SAC')
    elif opcodes.count('ADD') == 1:
        add_opcode('ADD')
    elif opcodes.count('SUB') == 1:
        add_opcode('SUB' )
    elif opcodes.count('BRZ') == 1:
        add_opcode('BRZ' )
    elif opcodes.count('BRN') == 1:
        add_opcode('BRN' )
    elif opcodes.count('BRP') == 1:
        add_opcode('BRP' )
    elif opcodes.count('INP') == 1:
        add_opcode('INP' )
    elif opcodes.count('DSP') == 1:
        add_opcode('DSP' )
    elif opcodes.count('MUL') == 1:
        add_opcode('MUL' )
    elif opcodes.count('DIV') == 1:
        add_opcode('DIV' )
    elif opcodes.count('STP') == 1:
        add_opcode('STP')
    else:
        pass
    
    
    
    

def pass_one():
    location_counter = 0;

    for line in code:
        roline = check_comment(line)
        label, roline = get_label(roline)
        if label != 'nil':
            i = add_label(label, location_counter)
            if i==0:
                print("Error! Label has already been defined once")
            if i==1:
                print("Error!",label, " has been declared as a Variable already!")
            if i==2:
                print("Error!",label, " is a reserved keyword, can't be used as a label")
        
        pass_one_code.append(roline)
        get_opcode(roline)
        

























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
# OPC_TABLE["CLA"] = ["0000" ]
# OPC_TABLE["LA"] = ["0001" ]
# OPC_TABLE["SAC"] = ["0010" ]
# OPC_TABLE["ADD"] = ["0011" ]
# OPC_TABLE["SUB"] = ["0100" ]
# OPC_TABLE["BRZ"] = ["0101" ]
# OPC_TABLE["BRN"] = ["0110" ]
# OPC_TABLE["BRP"] = ["0111" ]
# OPC_TABLE["INP"] = ["1000" ]
# OPC_TABLE["DSP"] = ["1001" ]
# OPC_TABLE["MUL"] = ["1010" ]
# OPC_TABLE["DIV"] = ["1011" ]
# OPC_TABLE["STP"] = ["1100" ]