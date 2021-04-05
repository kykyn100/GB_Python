"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие
 за приём оргтехники на склад и передачу в определенное подразделение компании.
  Для хранения данных о наименовании и количестве единиц оргтехники,
   а также других данных, можно использовать любую подходящую структуру,
    например словарь."""


class Storage:

    _iid = 0

    office_equipment = {
                        'Storage': [],
                        'IT': [],
                        'Cab_1': [],
                        'Cab_2': []
                        }


class OfficeEquipment(Storage):

    def __init__(self, color, weight):
        Storage._iid += 1
        self._iid = Storage._iid
        self.color = color
        self.weight = weight

    def store_add(self):
        Storage.office_equipment['Storage'] = {self._iid: }

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


# print([x for x in dir(prn_a) if not x.startswith('__')])


prn_a.store_add()
prn_b.store_add()
print(Storage.office_equipment)

