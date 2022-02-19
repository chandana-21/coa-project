from sre_constants import NOT_LITERAL


OPC_TABLE = {}

code = []
def get_label(line):
    label = 'nil'
    i = line.find('~')
    if i != -1:
        label = line[:i]
        roline = line[i+1:]
    return label, roline

def pass_one():
    location_counter = 0;

    for line in code:
        label, roline = get_label(line)

























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