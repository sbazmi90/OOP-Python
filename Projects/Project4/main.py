
# Press the green button in the gutter to run the script.

from Classes import *

M = Manager('Jane Smith', 27858, 2500, 800)
#print(M)


Payment1 = M.calculate_pay()


W=Worker('John Doe', 26589, 1000, 22.5)
Payment2 =W.calculate_pay()
if __name__ == '__main__':
    print(Payment1)
    print("\n")
    print(Payment2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


