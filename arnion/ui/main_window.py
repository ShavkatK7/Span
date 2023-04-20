import tkinter as tk

from arnion.data.employees_data import EmployeeDataHandler
from arnion.ui.departments_reports_ui import DepartmentsReportWindow
from arnion.ui.employees_reports_ui import EmployeesReportWindow


class DepartmentsReportWindow:
 from arnion.ui.departments_reports_ui import DepartmentsReportWindow


class EmployeesDataHandler:
    pass


class EmployeesReportHandler:
    pass


class MainWindow:

    # Конструктор
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("310x380")
        self.window.title("SPAN")

        # Добавление метки заголовка
        lbl_title = tk.Label(text="SPAN", font=('Helvetica', 16, 'bold'), fg='#0000cc', justify='center')
        lbl_title.place(x=25, y=55, width=250, height=50)

        # Добавление метки заголовка данных
        lbl_title = tk.Label(text="Данные", font=('Helvetica', 12, 'bold'), fg='#0066ff', justify='center')
        lbl_title.place(x=25, y=55, width=250, height=50)

        # Добавление кнопки данных "Отделы"
        btn_report = tk.Button(self.window, text="Отделы",
                               font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.do_report_departments)
        btn_report.place(x=25, y=100, width=120, height=50)

        # Добавление кнопки данных "Сотрудники"
        btn_close = tk.Button(self.window, text="Сотрудники",
                              font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.do_report_employees)
        btn_close.place(x=160, y=100, width=120, height=50)

        # Добавление кнопки заголовка отчетов
        lbltitle1 = tk.Label(text="Отчёты", font=('Helvetica', 12, 'bold'), fg='#0066ff', justify='center')
        lbltitle1.place(x=25, y=155, width=250, height=50)

        # Добавление кнопки заголовка "Отделы"
        btn_report = tk.Button(self.window, text="Отделы",
                               font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.do_report_departments)
        btn_report.place(x=25, y=200, width=120, height=50)

        # Добавление кнопки отчетов "Сотрудники"
        btn_close = tk.Button(self.window, text="Сотрудники",
                              font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.do_report_employees)
        btn_close.place(x=160, y=200, width=120, height=50)

        # Добавление кнопки закрытия "Тест"
        btn_test = tk.Button(self.window, text="Тест",
                             font=('Helvetica', 10, 'bold'), bg='#ffffcc', command=self.do_test)
        btn_test.place(x=25, y=300, width=120, height=50)

        # Добавление кнопки закрытия программы
        btn_close = tk.Button(self.window, text="Выход",
                              font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.close)
        btn_close.place(x=160, y=300, width=120, height=50)

    # Функция Тест"
    def do_test(self):
        employees = EmployeeDataHandler.select_list()
        for employee in employees:
            print(employee.get_full_name())

    # Открытие отчета "Отделы"
    def do_report_departments(self):
        rpt = DepartmentsReportWindow()
        rpt.open()

    # Открытие отчета "Сотрудники"
    def do_report_employees(self):
        rpt = EmployeesReportWindow()
        rpt.open()

    # Функция закрытия главного окна программы
    def close(self):
        self.window.destroy()

    # Запуск цикла окна
    def start_mainloop(self):
        self.window.mainloop()
