'''
class Laptop:

    def __init__(self, c, m, ra, ro, co, w, p):

        self.company = c
        self.model = m
        self.ram = ra
        self.rom = ro
        self.colour = co
        self.weight = w
        self.price = p


    def __str__(self):

        return f"\nCompany:{self.company}, Model :{self.model}, RAM :{self.ram},\nROM:{self.rom}, Colour :{self.colour}, Weight :{self.weight},\nprice:{self.price}"



l1 = Laptop('hp', "27b", '8GB', '1TB', 'Black', '7kg', 40000)

l2 = Laptop('Asus', '20A', '4GB', '500GB', 'White', '7kg', 28000)

l3 = Laptop('hp', '21A', '8GB', '2TB', 'White', '10kg', 50000)

l4 = Laptop('DELL', 'G7', '12GB', '1TB', 'Black', '8kg', 60000)

l5 = Laptop('Lenovo', 'L8', '12GB', '1TB', 'Black', '9kg', 45000)

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)

'''
#output of dictionary       
a ={}
print(type(a))
a[2] = 1
print(a)
a[1] = [2, 3, 4]
print(a)
print(type(a))
print(a[1][0])


a = [12, 13, 14, [10, 12, 13]]

print(a[3])

b = a[3] + [23]

print(b)




























