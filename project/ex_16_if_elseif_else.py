# Author: A01749389 Omar Rodrigo Sorchini Puente
from delta import Compiler, Phase


source = '''
var x, y;
x = 5;
if x - 5 {
    y = 1;
} else if x * 0 {
    y = 2;
} else if x - x {
    y = 3;
} else if x / x - 1 {
    y = 4;
} else {
    y = x;
}
y
'''

c = Compiler('program')
c.realize(source, Phase.EVALUATION)
print()
# print(c.parse_tree_str)
# print(c.symbol_table)
# print()
print(c.wat_code)
print()
print(c.result)
