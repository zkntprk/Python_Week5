### All Rights Reserved ###

#Copyright (c) ${Product_Profit.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

class Product(object):
    def __init__(self, product_id=0, product_name=None, product_purchase_price=0, product_sale_price=0, remarks=None):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price
        self.Remarks = remarks

    def set_remarks(self):
        self.marj = self.product_sale_price - self.product_purchase_price
        if self.marj < 0:
            self.remarks = "Loss"
        elif self.marj > 0:
            self.remarks = "Profit"
        else:
            self.remarks = "Neither Loss Nor Profit"
        return self.remarks

    def set_details(self):
        self.product_id = str(input("Please enter Product ID: "))
        self.product_name = str(input('Please enter Product Name: '))
        self.product_purchase_price = float(input('Please enter Product Purchase Price: '))
        self.product_sale_price = float(input("Please enter Product Sale Price: "))
        Product.set_remarks(self)

    def get_details(self):
        return print(
            f"Product ID= {self.product_id}  Product Name= {self.product_name}  Product Purchase Price= {self.product_purchase_price}  Product Sale Price= {self.product_sale_price}  Product Remaks= {self.remarks}")

t = 0
products = []
while True:
    products.append(Product(str(input("Please enter an product name: "))))
    products[t].set_details()
    answer = str(input('Do you want to add new Product Info? (Y/N)')).lower()
    if answer == 'y':
        t += 1
    elif answer == 'n':
        break

for i in products:
    Product.get_details(i)

### All Rights Reserved ###

#Copyright (c) ${Product_Profit.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.