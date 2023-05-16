import tkinter
root = tkinter.Tk()
root.title("attrition calculator")


#create function(s)
def calculate_attritioncalculator():
    employeeleft = (3)
    employeeworking = (100)
    attritioncalculator = employeeleft/employeeworking* 100
    print(attritioncalculator)

# create gui
label_employee_left = tkinter.Label(root, text= "EMPLOYEE LEFT: ")
label_employee_left.pack()

label_employee_working = tkinter.Label(root, text="EMPLOYEE WORKING: ")
label_employee_working.pack()


label_attrition_calculator = tkinter.Label(root, text="ATTRITION CALCULATOR: ")
label_attrition_calculator.pack()

entry_employee_left =tkinter.Entry(root)
entry_employee_left.pack()


entry_employee_working =tkinter.Entry(root)
entry_employee_working.pack()

button_calculate = tkinter.Button(root, text="calculate", command=calculate_attritioncalculator)
button_calculate.pack()

root.mainloop()