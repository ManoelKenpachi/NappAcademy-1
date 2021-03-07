from datetime import date, datetime


class MyCalendar:

    def __init__(self, *args):
        self.datas = []
        self.add_holiday(*args)

    ''' validando datas | -> comentario indica oque a função deve receber'''
    def validar(self, data) -> date:
        if isinstance(data, date):
            return data
        elif isinstance(data, str):
            try:
                return datetime.strptime(data, '%d/%m/%Y').date()

    def add_holiday(self, *args):
        for data in args:
            add = self.validar(data)
            if add:
                self.datas.append(add)
        # criando uma nova lista sem datas repitidas
        self.datas = list(set(self.datas))

    def check_holiday(self, data):
        return self.validar(data) in self.datas
