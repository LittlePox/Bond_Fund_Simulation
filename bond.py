


class Bond:
    def __init__(self, bond_type, notional, coupon_rate, frequency, maturity_date):
        self.__bond_type = bond_type
        self.__notional = notional
        self.__coupon_rate = coupon_rate
        self.__frequency = frequency
        self.__maturity_date = maturity_date

    def get_bond_type(self):
        return self.__bond_type

    def get_frequency(self):
        return self.__frequency

    def get_notional(self):
        return self.__notional

    def get_maturity_date(self):
        return self.__maturity_date

    def get_coupon_rate(self):
        return self.__coupon_rate

    def __str__(self):
        return str(self.__bond_type) + " Bond [" + ','.join(str(e) for e in (self.__notional, self.__coupon_rate,
                                                                        self.__frequency, self.__maturity_date))+"]"

