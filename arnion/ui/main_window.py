import tkinter as tk

from arnion.data.departments_data import DepartmentDataHandler, DepartmentDataObject
from arnion.data.employees_data import EmployeeDataHandler, EmployeeDataObject
from arnion.db.mysql_connection import ConnectionHandler
from arnion.ui.departments_data_ui import DepartmentsWindow
from arnion.ui.departments_reports_ui import DepartmentsReportWindow
from arnion.ui.employees_reports_ui import EmployeesReportWindow
from arnion.ui.employees_data_ui import EmployeesWindow
from arnion.ui.emploees_data_ui import EmployeesWindow

class MainWindow:

    #Конструктор
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("310x380")
        self.window.title("SPAN")

        # Добавление метки заголовка
        lbl_title = tk.Label(text="SPAN", font=('Hevletica', 16, 'bold'), fg='#0000cc', justify='center')
        lbl_title.place(x=25, y=15, width=250, height=50)

        # Добавление метки заголовка данных
        lblTitle1 = tk.Label(text="Данные", font=('Hevletica', 12, 'bold'), fg='#0066ff', justify='center')
        lblTitle1.place(x=25, y=55, width=250, height=50)

        # Добавление кнопки данных Отделы
        btn_report = tk.Button(self.window, text="Отделы",
                              font=('Hevletica', 10, 'bold'), bg='#ccffcc', command=self.do_list_departments)
        btn_report.place(x=25, y=100, width=120, height=50)

        # Добавление кнопки данных Сотрудники
        btn_report2 = tk.Button(self.window, text="Сотрудники",
                               font=('Hevletica', 10, 'bold'), bg='#ccffcc', command=self.do_list_employees)
        btn_report2.place(x=160, y=100, width=120, height=50)

        # Добавление метки заголовка отчетов
        lblTitle1 = tk.Label(text="Отчеты", font=('Hevletica', 12, 'bold'), fg='#0066ff', justify='center')
        lblTitle1.place(x=25, y=155, width=250, height=50)

        # Добавление кнопки отчетов Отделы
        btn_report_departments = tk.Button(self.window, text="Отделы",
                               font=('Hevletica', 10, 'bold'), bg='#ccffcc', command=self.do_report_departments)
        btn_report_departments.place(x=25, y=200, width=120, height=50)

        # Добавление кнопки отчетов Сотрудники
        btn_report_employees = tk.Button(self.window, text="Сотрудники",
                                font=('Hevletica', 10, 'bold'), bg='#ccffcc', command=self.do_report_employees)
        btn_report_employees.place(x=160, y=200, width=120, height=50)

        # # Добавление кнопки Тест
        # btn_test = tk.Button(self.window, text="Тест",
        #                       font=('Hevletica', 10, 'bold'), bg='#ccffcc', command=self.do_test)
        # btn_test.place(x=25, y=300, width=120, height=50)

        # Добавление кнопки закрытия программы
        btn_close = tk.Button(self.window, text = "Выход",
                              font = ('Hevletica',10,'bold'), bg='#ccffcc', command= self.close)
        btn_close.place(x=160, y=300, width=120, height=50)

    # Открытие списка "Отделы"
    def do_list_departments(self):
        rpt = DepartmentsWindow()
        rpt.open()

     # Открытие списка "Сотрудники"
    def do_list_employees(self):
        rpt = EmployeesWindow()
        rpt.open()

     # Открытие отчета "Отделы"
    def do_report_departments(self):
        rpt = DepartmentsReportWindow()
        rpt.open()

    # Открытие отчета "Сотрудники"
    def do_report_employees(self):
        rpt = EmployeesReportWindow()
        rpt.open()

     #Функция закрытия главного окна программы
    def close(self):
        self.window.destroy()
    def do_test(self):
        #department = DepartmentDataHandler.select_by_id(3)
        #print(department.department_name)
        #department.department_name = "Отдел работы с клиентами"
        #print(department.department_name)
        #DepartmentDataHandler.update(department)
        #print("Готово!")
        #department = DepartmentDataObject(department_name = "Отдел тестирования")
        #print(department.department_id)
        #DepartmentDataHandler.insert(department)
        #print(department.department_id)
        #print("Готово!")
        employee = EmployeeDataObject(first_name = "Ирина", middle_name = "Алексеевна", last_name = "Иванова", department_id = 3)
        print(employee.emloyee_id)
        EmployeeDataHandler.insert(employee)
        print(employee.emloyee_id)
        print("Готово!")

    # Запуск цикла окна
    def start_mainloop(self):
        self.window.mainloop()