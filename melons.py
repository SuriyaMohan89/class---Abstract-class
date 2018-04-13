"""Classes for melon orders."""
class AbstractMelonOrder(object):
    """A parent Abstract has all common attributes """

    def __init__(self, species, qty,shipped=False):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        order = self.order_type
        self.shipped = shipped
        tax = self.tax

    def get_total(self):
        """Calculate price including tax"""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    # def mark_shipped(self):
    #     """Record the fact that an order has been shipped"""

    #     self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    def __init__(self, species, qty, country_code, shipped=False):
        self.country_code = country_code
        super(InternationalMelonOrder, self).__init__(species, qty, country_code)

    def get_country_code(self):
        """Return the country code."""
        return self.country_code
        

