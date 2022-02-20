opc_table = {} # stores opcodes occuring in the program in format { opcode : [binaryCodeForOpcode, size, inctructionClass] }
lab_table = {} # stores Label addresses { label : location_address }
var_table = {} # stores variables in format { variable : [value,location_address,size] }
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
        

























# OPC_TABLE["CLA"] = ["0000",0]
# OPC_TABLE["LAC"] = ["0001",1]
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
# OPC_TABLE["LAC"] = ["0001" ]
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
