from dataclasses import dataclass
from decimal import Decimal

white_list = {"USD": Decimal(1), "EUR": Decimal(0.98), "UAH": Decimal(0.025)}


@dataclass()
class Price:
    amount: Decimal
    currency: str

    def __post_init__(self):
        if self.currency not in white_list:
            raise Exception("There is no such currency in the white list")

    def __str__(self) -> str:
        return f"Price: {self.amount} {self.currency}"

    def __add__(self, other):
        self.coincidence(other)
        return Price(
            amount=(self.amount + other.amount).quantize(Decimal("1.00")),
            currency=self.currency,
        )

    def __sub__(self, other):
        self.coincidence(other)
        return Price(
            amount=(self.amount - other.amount).quantize(Decimal("1.00")),
            currency=self.currency,
        )

    def coincidence(self, other):
        if self.currency != other.currency:
            self.convert()
            other.convert()

    def convert(self):
        self.amount *= white_list[self.currency]
        self.currency = [k for k, v in white_list.items() if v == Decimal(1)][0]
        return self.amount


def main():
    price_a = Price(Decimal(100), "EUR")
    price_b = Price(Decimal(100), "EUR")

    print(f" + {price_a + price_b}")
    print(f" - {price_a - price_b}")


if __name__ == "__main__":
    main()
