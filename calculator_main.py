import sys
from PyQt5.QtWidgets import *
#브랜치 계산기-기능-추가
class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation = QGridLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        self.equation = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(self.equation)

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_number.addWidget(button_plus, 4, 3)
        layout_number.addWidget(button_minus, 3, 3)
        layout_number.addWidget(button_product, 2, 3)
        layout_number.addWidget(button_division, 1, 3)

        #추가연산 버튼 생성
        button_mod = QPushButton("%")
        button_reverse = QPushButton("1/x")
        button_power = QPushButton("x^2")
        button_root = QPushButton("x^.5")

        ### 추가연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_mod.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_reverse.clicked.connect(self.button_reverse_clicked)
        button_power.clicked.connect(self.button_power_clicked)
        button_root.clicked.connect(self.button_root_clicked)

        ### 추가연산 버튼을 layout_operation 레이아웃에 추가
        layout_number.addWidget(button_mod, 0, 0)
        layout_number.addWidget(button_reverse, 1, 0)
        layout_number.addWidget(button_power, 1, 1)
        layout_number.addWidget(button_root, 1, 2)
        
        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("C")
        button_clearentry = QPushButton("CE")
        button_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_clearentry.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_number.addWidget(button_clear, 0, 2)
        layout_number.addWidget(button_clearentry, 0, 1)
        layout_number.addWidget(button_backspace, 0, 3)
        layout_number.addWidget(button_equal, 5, 3)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number - 1, 3)
                layout_number.addWidget(number_button_dict[number], 4 - x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 5, 1)

        ### 소숫점 버튼과 +/- 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 5, 2)

        button_plinus = QPushButton("+/-")
        button_plinus.clicked.connect(self.button_plinus_clicked)
        layout_number.addWidget(button_plinus, 5, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    
    ### 연산에 필요한 임시 값과 연산자를 global 변수로 저장 : 아래 함수 내에서 해당 값에 접근하도록 함
    global temp_val
    temp_val = 0
    
    global temp_op
    temp_op = ""

    ### 0~9까지의 숫자와 소숫점 .을 추가시키는 함수. 이미 소숫점이 화면에 적혀있으면 중복해 적히지 않도록 설정
    def number_button_clicked(self, num):
        equation = self.equation.text()
        if num == "." and num in equation : return
        equation += str(num)
        self.equation.setText(equation)

    ### +, -, *, /, % 5가지 사칙연산. 현재 값을 temp_val에, 연산자를 temp_op에 저장
    def button_operation_clicked(self, operation):
        global temp_val
        temp_val = float(self.equation.text())
        global temp_op
        temp_op = operation
        self.equation.setText("")

    ### 1/x 곱셈역수 설정. 여기부터 +/- 덧셈역수 설정까지의 4개 함수는 현재 화면에 숫자가 있는지의 여부를 따짐
    def button_reverse_clicked(self) :
        equation = self.equation.text()
        if equation != "" :
            equation = str(1/float(self.equation.text()))
            self.equation.setText(equation)

    ### x^2 제곱 설정
    def button_power_clicked(self) :
        equation = self.equation.text()
        if equation != "" :
            equation = str(float(self.equation.text()) ** 2)
            self.equation.setText(equation)

    ### x^.5 제곱근 설정
    def button_root_clicked(self) :
        equation = self.equation.text()
        if equation != "" :
            equation = str(float(self.equation.text()) ** 0.5)
            self.equation.setText(equation)

    ### +/- 덧셈역수 설정
    def button_plinus_clicked(self) :
        equation = self.equation.text()
        if equation != "" :
            if float(equation) < 0:
                self.equation.setText(equation[1:])
            else :
                self.equation.setText("-" + equation)

    ### 등호 =를 누르면, 연산자 temp_op에 저장된 연산자에 따라 서로 다른 연산을 수행한 후 temp_val, temp_op를 초기화
    def button_equal_clicked(self):
        global temp_val
        global temp_op
        if temp_op == "" :
            equation = self.equation.text()
        elif temp_op == "+" :
            equation = str(temp_val + float(self.equation.text()))
        elif temp_op == "-" :
            equation = str(temp_val - float(self.equation.text()))
        elif temp_op == "*" :
            equation = str(temp_val * float(self.equation.text()))
        elif temp_op == "/" :
            equation = str(temp_val / float(self.equation.text()))
        elif temp_op == "%" :
            equation = str(temp_val % float(self.equation.text()))
        self.equation.setText(equation)
        temp_val = 0
        temp_op = ""

    ### 클리어 C, CE는 화면 내 정보 및 temp_val, temp_op를 모두 초기화
    def button_clear_clicked(self):
        global temp_val
        temp_val = 0
        global temp_op
        temp_op = ""
        self.equation.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
