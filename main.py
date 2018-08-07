from bond_type import BondType
from bond import Bond
from datetime import date

bond_type = BondType.TREASURY
maturity_date = date(2020, 6, 30)
bond = Bond(bond_type, 1000, 0.03, 2, maturity_date)
print(bond)
