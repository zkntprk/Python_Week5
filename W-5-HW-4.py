### All Rights Reserved ###

#Copyright (c) ${Customer_buying_items.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

class Customer(object):
    def __init__(self, name=None, last_name=None, customer_id=0):
        self.name = name
        self.last_name = last_name
        self.customer_id = customer_id

    def get_customer_info(self):
        self.name = input("Please enter your name: ")
        self.last_name = input("Please enter your surname: ")
        self.customer_id = input("Please enter your customer ID: ")

class Items:
    def __init__(self, item_name=None, price=0.0, qty=0, price_tobe_paid=0.0, discount=0, items_bought=None):

        self.price = price
        self.qty = qty
        self.discount = discount
        self.price_tobe_paid = price_tobe_paid
        self.item_name = item_name
        self.total_price = float(self.price) * float(self.qty)
        self.Items_bought=items_bought

    def shopping_card(object):
        shopping_list.append(object.item_name)

    def calculate_discount(self):
        if self.total_price >= 4000:
            self.discount = 25
        elif 4000 >= self.total_price >= 2000:
            self.discount = 15
        else:
            self.discount = 10
        self.price_tobe_paid = (float(self.total_price) - float(self.total_price) * float(self.discount) / 100)
        return self.discount,self.price_tobe_paid

    def get_total_amount(self,piece):
        pay=float(self.price_tobe_paid / self.qty) * piece
        return pay


class multi(Customer,Items):
    def __init__(self,item_name=None, price=0.0, qty=0 ,should_pay=0 ,pieces=0, customer_dis=0, customer_total_price=0):
        self.should_pay=should_pay
        self.customer_dis=customer_dis
        self.customer_total_price=customer_total_price
        self.pieces=pieces
        Items.__init__(self)
        Customer.__init__(self)

    def __str__(self):
        return f'Customer_Name: {self.name}  Customer_Surname: {self.last_name} Customer_ID: {self.customer_id} \n' \
               f'Items: {self.Items_bought} \n' \
               f'Total_Pieces: {self.pieces}  Customer_Total_Price: {self.customer_total_price} Customer_Discount: %{self.customer_dis}  Final_Payment: {self.should_pay}'.format(self=self)

a=multi() #creat an object
a.get_customer_info()
shopping_list = []  # Items that buying from customer

# Market ITEMS LIST                                 # Item-Price-qty
Market_Items = [Items('Chocolate', 5, 100), Items('Chips', 1.25, 2200), Items('Band', 2.5, 123),
                Items('Bread', 1, 5000), Items("Laptop", 2000, 30), Items("Ring", 0.5,1500)]  # Items that selling in Market

for i in range(len(Market_Items)):
    Items.calculate_discount(Market_Items[i])

for i in range(len(Market_Items)):
    answer = input(f'Do you want to add {Market_Items[i].item_name} to your basket?(Y/N)').lower()
    if answer == 'y':
        multi.shopping_card(Market_Items[i])
        piece=int(input(f'How many {Market_Items[i].item_name} pieces you want to buy? '))
        a.pieces+=piece
        a.customer_total_price+=Market_Items[i].price*piece #without discount price
        a.should_pay+= Market_Items[i].get_total_amount(piece) #with discount price
        a.total_price+=Market_Items[i].total_price
        a.price_tobe_paid+=Market_Items[i].price_tobe_paid
    else:
        continue

a.customer_dis= round(((a.total_price-a.price_tobe_paid)/a.total_price*100),2) #average discount at total
a.Items_bought=shopping_list[:]
print(a)

### All Rights Reserved ###

#Copyright (c) ${Customer_buying_items.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.