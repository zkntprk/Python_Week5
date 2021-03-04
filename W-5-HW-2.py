### All Rights Reserved ###

#Copyright (c) ${Items_Info.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

class ItemInfo:
    def __init__(self, item, item_code=0, price=None, qty=None, discount=None, net_price=None):
        self.item = item
        self.item_code = item_code
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price

    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        elif 10 < self.qty < 20:
            self.discount = 15
        else:
            self.discount = 20
        return int(self.discount)

    def buy(self):
        self.item_code = input(f"Please enter the {self.item}'s item code: ")
        self.price = float(input(f"Please enter the {self.item}'s price: "))
        self.qty = int(input(f"Please enter the {self.item}'s qty(quantity in stock): "))
        ItemInfo.calculate_discount(self)
        self.net_price = (float(self.price * self.qty) - self.discount)

    def show_all(self):
        return print(
            f"Item: {self.item}  Item_Code: {self.item_code}  Item_Price: {self.price}  Item_qty: {self.qty}  Item_discount: {self.discount}  Item_Net_Price: {self.net_price}")

t = 0
items = []
while True:
    items.append(ItemInfo(input("Please enter an item name: ")))
    items[t].buy()
    answer = str(input('Do you want to add new Item Info? (Y/N)')).lower()
    if answer == 'y':
        t += 1
    elif answer == 'n':
        break

for i in items:
    ItemInfo.show_all(i)

### All Rights Reserved ###

#Copyright (c) ${Items_Info.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.