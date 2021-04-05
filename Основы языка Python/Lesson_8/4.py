class Storage:
    pass


class OfficeEquipment(Storage):

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight


class Printer(OfficeEquipment):

    def __init__(self, color, weight, dev_type, brand, lpm, price):
        super().__init__(color, weight)
        self.dev_type = dev_type
        self.brand = brand
        self.lpm = lpm
        self.price = price


class Scanner(OfficeEquipment):

    def __init__(self, color, weight, dev_type, brand, price):
        super().__init__(color, weight)
        self.dev_type = dev_type
        self.brand = brand
        self.price = price


class Xerox(OfficeEquipment):

    def __init__(self, color, weight, dev_type, price):
        super().__init__(color, weight)
        self.dev_type = dev_type
        self.price = price


prn_a = Printer('black', '3 kg', 'FFD', 'HP', '20', '80000')
prn_b = Printer('white', ' 3 kg', 'FFD', 'Conica', '36', '120000')

scan_a = Scanner('white', '1,5 kg', 'slim', 'HP', '15000')
scan_b = Scanner('black', '1,7 kg', 'extra small', 'Canon', '10000')

xrx_a = Xerox('black', '3 kg', 'auto', '6000')
xrx_b = Xerox('black', '4 kg', 'manual', '4000')
