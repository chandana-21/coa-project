
# Project Title

**FORMAT OF INSTRUCTION**  
Each instruction may include four fields:a label,an operation,an operand and a comment.  
Format of instruction:  

`<label> ~ <opcode> <operand> ; <comment>`

1.**Label field**:It is used for defining a symbol.Label field ends with a tilde(**~**).It can consist of alphanumeric characters,and the first character cannot be a numerical character.
If a duplicate label exists,an error message is shown.The label field must not be one of the keywords (opcodes).  
2.**Operation field**:It defines the operation to be done.Operation field occurs after the label field and must be preceded by one white space character.The operation field must contain opcodes from given table:
  
|Assembly Opcode|Meaning|
|:----------|:--------- |
|CLA|Clear accumulator|
|LAC|	Load into accumulator from address  
|SAC|	Store accumulator contents into address  
ADD|	Add address contents to accumulator contents  
SUB|	Subtract address contents from accumulator contents  
BRZ|	Branch to address if accumulator contains zero  
BRN|	Branch to address if accumulator contains negative value  
BRP|	Branch to address if accumulator contains positive value  
INP|	Read from terminal and put in address  
DSP|	Display value in address on terminal  
MUL|	Multiply accumulator and address contents  
DIV|	Divide accumulator contents by address content. Quotient in R1 and remainder in R2  
STP	Stop execution

3.**Operation field**: This field specifies either the address or the data.The operand field, if required, must follow the operation field, and must be preceded by one white-space character.The variable name cannot be digits alone, it can be alphanumeric.  
4.**Comment field**:It allows the programmer to document the software.The comment field is separated from the operand field (or from the operation field if no operand is required) by one white-space character and begins with a ‘;’.The comment field can contain any ASCII characters.  
5.Each instruction ends with a newline character,the next instruction starts from the next line.  



