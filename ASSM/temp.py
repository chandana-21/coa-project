reserved_opcodes = {"CLA":(0,0), "LAC":(1,1), "SAC":(2,1), "ADD":(3,1), "SUB":(4,1), "BRZ":(5,1), "BRN":(6,1), "BRP":(7,1), "INP":(8,1), "DSP":(9,1), "MUL":(10,1), "DIV":(11,1), "STP":(12,0)}

sym_table = {}
opc_table = []
error_table = []

with open('inp.txt','r') as file:
  asm_file = file.readlines()

def print_sym_table():
  print("\n********* SYMBOL TABLE *********")
  print("--------------------------------")
  print("Symbol\t|\tLocation")
  print("--------------------------------")
  for symbol,location in sym_table.items():
    print(symbol," \t|\t",format(location, "08b"))
  print("")

def print_opc_table():
  print("********* opcode TABLE *********")
  print("--------------------------------")
  print(" Location\t|\topcode")
  print("--------------------------------")
  for i in opc_table:
    print(format(i[0], "08b"),"\t|\t",format(i[1], "04b"))
  print("")


def check_valid_variable(symbol,line_num):
    try:
        k = int(symbol[0])
        error_table.append([line_num,"ERROR! Symbol cannot start with a number in " + symbol])
        return False
    except:
        pass
    if (symbol in reserved_opcodes):
        error_table.append([line_num,"ERROR! opcode already used as a variable, try using a different variable name"])
        return False
    valid_chars = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    flag = 0
    for character in symbol:
        if character not in valid_chars:
            flag = 1
            error_table.append([line_num,"ERROR! Invalid character found in " + character + " in symbol " + symbol])
    if flag == 1:
        return False
    return True

def check_comment(line):
    if (';' in line):
        return True
    else:
        return False
        
def check_symbol(line):
    if('~' in line):
        return True
    return False

def add_symbol(line, lc, line_num):
    symbol = line.split('~')[0]
    if (len(symbol) == 0):
        error_table.append([line_num,"ERROR! No symbol found"])
        return
    if (symbol in reserved_opcodes):
        error_table.append([line_num,"ERROR! opcode used as a label already, try using a different opcode "])
        return
    if(symbol in sym_table):
      if type(sym_table[symbol]) != type(5):
        if(sym_table[symbol][0] == -2):
          error_table.append([line_num,"ERROR! Variable " + symbol + " a label already, try using a different variable"])
          return
      else:
        error_table.append([line_num,"ERROR! Symbol " + symbol +" has already been declared"])
        return
    if(check_valid_variable(symbol, line_num)==False):
        return
    sym_table[symbol] = lc

def pass_one(loc_ctr):
  line_num = 0
  while line_num != len(asm_file):
    line = asm_file[line_num]
    if(check_comment(line)):
        line = line.split(';')[0]
        line = line.strip()
        if(len(line) == 0):
            line_num += 1
            continue
    if(check_symbol(line)):
      add_symbol(line, loc_ctr, line_num)
      line = line.split('~')[1]

    line = line.split()

    opcode = line[0] #test

    # if (line_num == len(asm_file) - 1):
        # if(opcode != 'STP'):
        #     error_table.append([line_num,"ERROR! Expected end statement STP at the end"])
    if opcode in reserved_opcodes.keys():
      opc_table.append([loc_ctr, reserved_opcodes[opcode][0]])
    else:
        error_table.append([line_num,"ERROR! " + opcode + " opcode not recognized"])
    line = line[1:]
    print(line)
    if (opcode in reserved_opcodes):
        if reserved_opcodes[opcode][1] != len(line):
            error_table.append([line_num,"ERROR! " + opcode + " expects " + str(reserved_opcodes[opcode][1]) + " number of arguments " + "but " + str(len(line)) + " given"])

    for var in line:
      if var not in sym_table:
        if(check_valid_variable(var,line_num)==False):
            continue
        if ('BR' in opcode):
            sym_table[var] = (-1,line_num)
        else:
            sym_table[var] = (-2,line_num)
      else:
        if ('BR' in opcode and sym_table[var][0] == -2):
            error_table.append([line_num,"ERROR! Invalid jump location " + var + " since it's already used as a variable"])
        if('BR' not in opcode and sym_table[var][0] == -1):
            error_table.append([line_num,"ERROR! Invalid use of " + var + ", it has already been used as a jump location"])

    line_num += 1
    loc_ctr += 1
  return loc_ctr


def get_variables(lc):
  for symbol in sym_table:
    if type(sym_table[symbol]) == type((1,1)):
      if sym_table[symbol][0] == -2:
        sym_table[symbol] = lc
        lc += 1
      elif sym_table[symbol][0] == -1:
        error_table.append([sym_table[symbol][1],"ERROR: Label " + symbol  + " used but not defined"])
  return lc

def pass_two(ofile):
  line_num = 0
  while line_num != len(asm_file):
    line = asm_file[line_num]
    if(check_comment(line)):
        line = line.split(';')[0]
        line = line.strip()
        if(len(line) == 0):
            line_num += 1
            continue
    if(check_symbol(line)):
      line = line.split('~')[1]
    line = line.split()
    opcode = line[0]
    if opcode in reserved_opcodes.keys():
      ofile.write(format(reserved_opcodes[line[0]][0], "04b"))
    line = line[1:]


    # if(len(line) == 0):
    #   ofile.write(format(0,"08b"))
    # else:
    #   for var in line:
    #     ofile.write(format(sym_table[var],"08b"))
    
    ofile.write("\n")
    line_num += 1


loc_ctr = pass_one(0)

get_variables(loc_ctr)
if(len(error_table) == 0):
  with open("out.txt","w+") as ofile:
    pass_two(ofile)
  print_sym_table()
  print('================================\n')
  print_opc_table()
else:
    for i in error_table:
        print (i[1],"at line " + str(i[0]+1))