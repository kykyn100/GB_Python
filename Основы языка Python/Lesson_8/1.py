class Data:

    """ Класс 'Дата'
        Инициатор принимает строку вида «день-месяц-год»"""

    class_date = '01-01-1970'

    def __init__(self, date: str) -> None:
        Data.class_date = date

    @classmethod
    def converter(cls):
        cnv = ''.join(cls.class_date.split('-'))
        return int(cnv)

    @staticmethod
    def validator(date):
        import time
        date_str = str(date)
        try:
            time.strptime(date_str, '%d%m%Y')
            print('Все верно!')
        except ValueError:
            print('Неверный формат!')


my_date = '05-03-1988'

Data(my_date)
print(Data.converter())
Data.validator(Data.converter())

