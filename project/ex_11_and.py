from delta import Compiler, Phase


source = '10 && 20 && 30'

c = Compiler('program')
c.realize(source, Phase.EVALUATION)
print()
# print(c.parse_tree_str)
# print(c.symbol_table)
# print()
print(c.wat_code)
print()
print(c.result)
