# // MODULES //


# // CREATING MODULES //
import sys
import sales
from sales import calc_shipping, calc_tax

calc_shipping()
calc_tax()

# another way:
# (import sales)
sales.calc_shipping()


# // COMPILED PYTHON FILES //
# python creates combined version of file in .pyc format and is stored in form of bytecode.


# // MODULE SEARCH PATH //
# import sys
# all directories got printed
print(sys.path)
