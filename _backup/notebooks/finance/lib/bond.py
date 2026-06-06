from enum import IntEnum
import math

class CouponModel(IntEnum):
    #: continuous model
    Continuous = 0
    #: discrete model
    Discrete = 1

class CouponBond:

    def __init__(self, principal: float, rate: float, maturity: int, interest_rate: float,
                 model: CouponModel= CouponModel.Discrete ):
        self.principal = principal
        self.rate = rate / 100.0
        self.maturity = maturity
        self.interest_rate = interest_rate / 100.0
        self.model = model

    def present_value(self, x, n):
        if self.model == CouponModel.Discrete:
            return x / math.pow(1.0 + self.interest_rate, n)
        elif self.model == CouponModel.Continuous:
            return x * math.exp(-n * self.interest_rate)
        else:
            raise ValueError("model not supported")


    def calculate_price(self):

        price = 0.0

        # discount the coupon payments
        for t in range(1, self.maturity + 1):
            price += self.present_value(self.principal * self.rate, t)

        # discount principle amount
        price += self.present_value(self.principal, self.maturity)

        return price


class ZeroCouponBond(CouponBond):

    def __init__(self, principal: float, maturity: int, interest_rate: float,
                 model: CouponModel= CouponModel.Discrete):
        super().__init__(principal, 0.0, maturity, interest_rate, model)

if __name__ == '__main__':

    bond = CouponBond(1000, 10.0, 3, 4.0)
    print("Bond price: %.2f" % bond.calculate_price())

    bond = ZeroCouponBond(1000, 2, 4.0)
    print("Bond price: %.2f" % bond.calculate_price())
