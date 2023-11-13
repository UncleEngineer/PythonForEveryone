class Theater:
    # Attribute
    theaterName = 'Uncle Engineer Theater'

    # Constructor
    def __init__(self, title, price):
        self.title = title
        self.price = price

    # Method
    def hello(self):
        print('สวัสดีคุณลูกค้าทุกท่าน')

class Customer(Theater):
    def __init__(self, fullname, age, title, price, seats):
        super().__init__(title, price)
        self.fullname = fullname
        self.age = age
        self.seats = seats
        self.money = 10000

    def buyTicket(self):
        # คำนวณค่าตั๋ว
        self.total = self.price * self.seats

        # หักเงินจากลูกค้า
        self.money -= self.total

        print(f'ชื่อลูกค้า : {self.fullname}')
        print(f'อายุ : {self.age}')
        print(f'เรื่อง : {self.title}')
        print(f'ซื้อ : {self.seats} ที่นั่ง รวมเงิน {self.total}')
        print(f'เหลือเงิน : {self.money} บาท')

# movie01 = Theater('ธี่หยด', 150)
# print(movie01.theaterName)
# print(movie01.title)
# print(movie01.price)
# movie01.hello()
# print('==================================')
# movie02 = Theater('สัปเหร่อ', 120)
# print(movie02.theaterName)
# print(movie02.title)
# print(movie02.price)
# movie02.hello()
# print('==================================')
# movie03 = Theater('เพื่อน(ไม่)สนิท', 80)
# print(movie03.theaterName)
# print(movie03.title)
# print(movie03.price)
# movie03.hello()

custom01 = Customer('สมชาย สบายดี', 20, 'ธี่หยด', 150, 1)
print(custom01.theaterName)
custom01.hello()
custom01.buyTicket()
print('===============================')
custom02 = Customer('สมปอง น้องสมชาย', 35, 'สัปเหร่อ', 120, 2)
print(custom02.theaterName)
custom02.hello()
custom02.buyTicket()
print('===============================')
custom03 = Customer('สมหญิง จริงใจ', 50, 'เพื่อน(ไม่)สนิท', 80, 5)
print(custom03.theaterName)
custom03.hello()
custom03.buyTicket()