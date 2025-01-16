class Kiosk:
    def __init__(self):
        # 문제 2-1의 답을 입력하세요.
        self.menu = ['americano', 'latte', 'mocha', 'yuza_tea', 'green_tea', 'choco_latte']
        self.price = [2000, 3000, 3000, 2500, 2500, 3000]
        self.order_options = {'menu_option':{'msg':'음료 번호를 입력하세요 : ',
                                             'allow_inputs':[x + 1 for x in range(len(self.menu))],
                                             'error_msg':'없는 메뉴입니다. 다시 주문해 주세요.'},
                              'add_menu_option':{'msg':'추가 주문은 음료 번호를, 지불은 0을 누르세요 : ',
                                                 'allow_inputs':list(range(len(self.menu)+1)),
                                                 'error_msg':'없는 메뉴입니다. 다시 주문해 주세요.'},
                              'temp_option':{'msg':'HOT 음료는 1을, ICE 음료는 2를 입력하세요 : ',
                                             'allow_inputs':[1, 2],
                                             'error_msg':'1과 2 중 하나를 입력하세요.\n'}}
        self.temp_dic = {1:'HOT', 2:'ICE'}
        self.order_menu = []  # 주문 리스트
        self.order_price = []  # 가격 리스트
        self.price_sum = 0
    # 메뉴 출력 메서드
    def menu_print(self):
        for index, (menu, price) in enumerate(zip(self.menu, self.price)):
            print(f" {index+1} {menu} : {price} '원' ")

    #사용자 입력 및 수 이외의 값 입력시 에러 처리
    def input_from_user(self, option):
        try:
            user_input = int(input(option['msg']))
            if user_input in option['allow_inputs']:
                return user_input
            
            raise ValueError
        except ValueError as ve:
            print(option['error_msg'])
            return self.input_from_user(option)

    # 주문 메서드
    def menu_select(self):
        is_first = True
        n = 1
        while n != 0:
            # 메뉴 물어보기
            if is_first :
                n = self.input_from_user(self.order_options['menu_option'])
                is_first = False
            else :
                n = self.input_from_user(self.order_options['add_menu_option'])

            if n == 0:
                print("주문이 완료되었습니다.")
                print(self.order_menu, self.order_price)  # 확인을 위한 리스트를 출력합니다.
                break

            self.order_price.append(self.price[n-1])  # 가격 리스트에 추가합니다.
            self.price_sum += self.price[n-1]  # 선택 음료의 가격

            # 음료 온도 물어보기
            t = self.input_from_user(self.order_options['temp_option'])
            self.temp = self.temp_dic[t]

            self.order_menu.append(self.temp + ' ' + self.menu[n-1])  # 주문 리스트에 추가합니다.

            # 문제 2-2의 답을 입력하세요.
            print(f" 주문음료 {self.temp} {self.menu[n-1]} : {self.price[n-1]} 원 ")  # 온도 속성을 추가한 주문 결과 출력
            print(f" 총 금액 : {self.price_sum} 원")

    def input_str(self, option) :
        choose = input("결제 방법을 입력해주세요. -현금: 'cash' or 1 -카드 'card' or 2 ")
        if choose not in option:
            print("입력하신 결제 수단이 없습니다. 다시 입력해주세요.")
            return self.input_str(option)
        
        return choose

    def pay(self):
        pay_option = {'1':'직원을 호출하겠습니다.',
                      'cash':'직원을 호출하겠습니다.',
                      '2':'IC칩 방향에 맞게 카드를 꽂아주세요.',
                      'card':'IC칩 방향에 맞게 카드를 꽂아주세요.'}

        pay_method = self.input_str(pay_option)
        print(str(pay_option[pay_method]))
    def table(self):
        # 외곽
        print('⟝' + '-' * 30 + '⟞')
        for i in range(5):
            print('|' + ' ' * 31 + '|')

        # 주문 상품명 : 해당 금액
        for menu, price in zip(self.order_menu, self.order_price):
          print(f"     {menu} : {price}")
        print('     합계 금액 :', self.price_sum)

        # 외곽
        for i in range(5):
            print('|' + ' ' * 31+ '|')
        print('⟝' + '-' * 30 + '⟞')
