import calendar

class DataToCalendar:

    def __init__(self, year_as_int, month_as_int):
        map_days_week = {
            0 : "Segunda",
            1 : "Terça",
            2 : "Quarta",
            3 : "Quinta",
            4 : "Sexta",
            5 : "Sabado",
            6 : "Domingo"
        }

        mes = calendar.Calendar().monthdatescalendar(year_as_int,month_as_int)
        formato = "%d-%m-%Y"
        list_to_return = list()

        for semana in mes:
            semana_l = []

            for dia in semana:
                wd = int(dia.weekday())
                d = dia.strftime(formato)
                
                semana_l.append(d)

            list_to_return.append(tuple(semana_l))

        self.month_name = calendar.month_name()
        self.data = list_to_return