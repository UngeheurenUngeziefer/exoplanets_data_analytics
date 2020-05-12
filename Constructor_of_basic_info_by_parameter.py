# напишем класс, который будет выводить основную информацию по указанному параметру
# чтобы автоматизировать дальнейшее исследование
from Exoplanets_basic_info import list, all_opened_planets, rus_columns, confirmed_planets_table

class ParameterBasicInfo:
    # импортируем две важных таблицы: все открытые планеты и подтверждённые планеты
    # конструктор принимает только имя параметра/столбца таблицы
    def __init__(self, prmtr_name):
        self.name = prmtr_name
        self.rus_name = ''
        self.column = list[self.name]
        self.confirmed_planets_table_with_prmtr = confirmed_planets_table.dropna(subset=[self.name])
        for i in range(len(list.columns.values)):
            if list.columns.values[i] == self.name:
                self.rus_name = rus_columns[i].lower()

    # количество пустых и заполненных полей
    def empty_fields_num(self):
        empty_fields_of_prmtr = list[self.name].isna().sum()
        filled_fields_of_prmtr = all_opened_planets - empty_fields_of_prmtr
        return '\nПустых полей в столбце {}: {}, заполненных: {}'\
            .format(self.rus_name, empty_fields_of_prmtr, filled_fields_of_prmtr)

    # оставляем только подтверждённые планеты
    def confirmed_planets(self):
        num_of_filled_fields_of_prmtr = self.confirmed_planets_table_with_prmtr[self.name].count()
        return '\nПодтверждённых планет, с заполненными полями столбца {}: {}'\
            .format(self.rus_name, num_of_filled_fields_of_prmtr)

    # выводит таблицу с именем планеты и параметром, сортирует по параметру
    def table_prmtr_name(self):
        return self.confirmed_planets_table_with_prmtr.loc[:, ['name', self.name]]\
            .sort_values(by=self.name, ascending=False)

    # выводит наибольший параметр среди планет, далее наименьший
    def biggest_prmtr(self):
        return ('\nСамый большой {} у экзопланет: \n {}'
                .format(self.rus_name.lower(), self.confirmed_planets_table_with_prmtr
                        .loc[:, ['name', self.name]]
                        .sort_values(by=self.name, ascending=False).head(5)))

    def lowest_prmtr(self):
        return ('\nСамый маленький {} у экзопланет: \n {}'
                .format(self.rus_name.lower(), self.confirmed_planets_table_with_prmtr
                        .loc[:, ['name', self.name]]
                        .sort_values(by=self.name, ascending=True).head(5)))

    # функция сравнения с объектом (имя) по параметру (конкретная цифра параметр объекта)
    def obj_comparison(self, obj_name, obj_prmtr):
        results_prmtr_filtered = self.confirmed_planets_table_with_prmtr.iloc[
            (self.confirmed_planets_table_with_prmtr[self.name] - obj_prmtr).abs().argsort()[:5]]

        # находим количество планет меньше и больше нашего объекта
        bigger_value_num = self.confirmed_planets_table_with_prmtr[(self.confirmed_planets_table_with_prmtr
                                                                    [self.name] > obj_prmtr)][self.name].count()
        lesser_value_num = self.confirmed_planets_table_with_prmtr[(self.confirmed_planets_table_with_prmtr
                                                                    [self.name] < obj_prmtr)][self.name].count()

        answer_1 = ('\nПочти такой же {} как и {} имеют: \n {} \n'
                    .format(self.rus_name.lower(), obj_name, results_prmtr_filtered
                            .loc[:, ['name', self.name]]
                            .sort_values(by=self.name, ascending=False)))
        answer_2 = ('\nЭкзопланет {} которых больше чем имеет {}: {}\n'
                    '\nЭкзопланет {} которых меньше чем имеет {}: {}\n'
                    .format(self.rus_name.lower(), obj_name, bigger_value_num,
                            self.rus_name.lower(), obj_name, lesser_value_num))

        if bigger_value_num > lesser_value_num:
            if bigger_value_num == 0:
                bigger_value_num += 0.00001
            elif lesser_value_num == 0:
                lesser_value_num += 0.00001
            superiority = bigger_value_num / lesser_value_num
            string_answer = '\nЭкзопланет {} которых больше чем имеет {} в {:.2f} раз больше'\
                .format(self.rus_name.lower(), obj_name, superiority)
        elif bigger_value_num < lesser_value_num:
            superiority = lesser_value_num / bigger_value_num
            string_answer = '\nЭкзопланет {} которых меньше чем имеет {} в {:.2f} раз больше' \
                .format(self.rus_name.lower(), obj_name, superiority)
        else:
            string_answer = '\nОдинаковое количество экзопланет имеет {} больше и меньше чем имеет {}' \
                .format(self.rus_name.lower(), obj_name)

        return answer_1 + answer_2 + string_answer


def print_basic_info(prmtr, comparison_obj, comparison_prmtr):
    prmtr = ParameterBasicInfo(prmtr)
    print(prmtr.empty_fields_num(), file=open("output.txt", "a"))
    print(prmtr.confirmed_planets(), file=open("output.txt", "a"))
    print(prmtr.biggest_prmtr(), file=open("output.txt", "a"))
    print(prmtr.lowest_prmtr(), file=open("output.txt", "a"))
    print(prmtr.obj_comparison(comparison_obj, comparison_prmtr), file=open("output.txt", "a"))




print_basic_info('lambda_angle', 'Земля', 0)
