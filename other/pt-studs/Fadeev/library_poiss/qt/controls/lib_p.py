from PySide6 import QtGui as qtg, QtWidgets as qtw

from qt.py.lib_p import Ui_LibPWindow


class LibPControl(Ui_LibPWindow, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_ui()

    def setup_ui(self):
        super().setupUi(self)
        validator = qtg.QIntValidator(bottom=0)
        self.le_income_requests.setValidator(validator)
        self.le_services_requests.setValidator(validator)

    def connect_ui(self):
        self.pb_find.clicked.connect(self.find)

    def find(self):
        l = int(self.le_income_requests.text())
        u = int(self.le_services_requests.text())
        P0 = 1 - l / u
        Lq = l ** 2 / (u * (u - l))
        Wq = l / (u * (u - l))
        W = 1 / u - l / u * (u - l)
        Pw = l / u
        t = '    '
        self.te_output.setText(
            '\n'.join([
                f'Расчеты при следующих значениях параметров:',
                f'{t}Количество приходящих запросов (з/час):',
                f'{2 * t}λ = {l}',
                f'{t}Скорость обработки запросов (з/час):',
                f'{2 * t}μ = {u}',
                f'Расчеты:',
                f'{t}1. Вероятность того, что в системе нет запросов:',
                f'{2 * t}P(0) = 1 - λ/μ = 1 - {l}/{u} = {P0:.2}',
                f'{t}2. Среднее число запросов в очереди:',
                f'{2 * t}Lq = λ^2 / (μ(μ-λ)) = {l ** 2} / ({u}({u} - {l})) = {Lq:.2}',
                f'{t}3. Среднее время ожидания:',
                f'{2 * t}Wq = λ / (μ(μ-λ)) =  {l} / ({u}({u} - {l})) = {Wq:.2}',
                f'{t}4. Среднее время, которое запрос проводит в системе:',
                f'{2 * t}W = 1 / μ - λ/μ(μ-λ) = 1 / {u} - {l} / {u} * ({u} - {l}) ={W:.2}',
                f'{t}5. Вероятность того, что запросу придется ждать обслуживания:',
                f'{2 * t}Pw = λ / μ = {l} / {u} = {Pw:.2}'
            ])
        )
