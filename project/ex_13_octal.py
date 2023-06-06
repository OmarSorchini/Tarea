# Author: A01749389 Omar Rodrigo Sorchini Puente
from delta import Compiler, Phase


source = '#o20000000000'

c = Compiler('program')
c.realize(source, Phase.EVALUATION)
print()
print(c.parse_tree_str)
print()
print(c.wat_code)
print()
print(c.result)
