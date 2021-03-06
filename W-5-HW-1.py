### All Rights Reserved ###

#Copyright (c) ${Society.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

class Society:
    def __init__(self, society_name=None, house_no_of_mem=None, income=None, flat=None):
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat = flat
        self.income = income

    def allocate_flat(self):
        if 25000 <= self.income:
            self.flat = 'A Type'
        elif 20000 <= self.income < 25000:
            self.flat = 'B Type'
        elif 15000 <= self.income < 20000:
            self.flat = 'C Type'
        else:
            self.flat = 'D Type'
        return self.flat

    def input_data(self):
        self.society_name = input('Please enter the society name: ')
        self.house_no_of_mem = input('Please enter society_no_of_mem: ')
        self.income = int(input('Please enter the income as int: '))
        self.flat = self.allocate_flat()

    def show_data(self):
        print('Society_Name: ', self.society_name, ' House_no_of_member: ', self.house_no_of_mem, ' Income: ',
              self.income, ' Flat type: ', self.flat)

t = 0
a = Society()
society = [a]
while True:
    Society.input_data(society[t])
    answer = str(input('Do you want to add new Society Info? (Y/N)')).lower()
    if answer == 'y':
        society.append(Society())
        t += 1
    elif answer == 'n':
        break

for i in range(0, len(society)):
    society[i].show_data()

### All Rights Reserved ###

#Copyright (c) ${Society.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.