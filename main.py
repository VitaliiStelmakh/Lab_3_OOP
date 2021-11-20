masss = []

def sortsum():
    N = len(masss)
    for i in range(N - 1):
        m = masss[i]
        p = i
        for j in range(i + 1, N):
            if m < masss[j]:
                m = masss[j]
                p = j

        if p != i:
            t = masss[i]
            masss[i] = masss[p]
            masss[p] = t


class My_List:
    mass = []

    def __init__(self, m):
        self.mass = m

    def add(self, elem):
        self.mass.extend(elem.mass)
        return self.mass

    def __iadd__(self, other):
        self.add(other)
        return self

    def delete(self, n):
        del (self.mass[n])
        return self.mass

    def vivod_revers(self):
        a = self.mass
        a = list(reversed(a))
        return (self.mass, a)

    def sum(self):
        total = 0
        for i in range(len(self.mass)):
            total += int(self.mass[i])
        return total

    def sort(self):
        a = sorted(self.mass)
        return a

    def __lt__(self, other):
        if self.sum() < other.sum():
            return True
        else:
            return False

    def __str__(self):
        return '({})'.format(self.mass)

menu = 1
while menu == 1:
    n = int(input("Виберіть дію \n"
                  "1-додати об'єкт \n"
                  "2-додати елемент у список \n"
                  "3-вилучити елемент за індексом\n"
                  "4-сортування списку\n"
                  "5-виведення елементів списку від початку і від кінця\n"
                  "6-обчислення суми елементів\n"
                  "7-відсортувати по умові завдання\n"
                  "8-порівняння двох списків за сумою(перевантаження <)\n"
                  "9-додати елемент у список(перевантаження +=) \n"
                  "10-додати до списку з найбільшою сумою елементи списку з найменшою сумою\n"
                  "11 - Вивід елементів перевантаженям функції\n"
                  "0-вийти з програми\n"))

    if (n == 1):
        t = 1
        element = []
        while t == 1:
            while t == 1:
                qqq = input("Введіть елемент списку\n")
                element.append(int(qqq))
                t = int(input("Бажаєте додати ще елемент списку? так - 1, ні - інше число\n"))
            a = My_List(element)
            masss.append(a)
            element = []
            t = int(input("Бажаєте додати ще екземпляр класу? так - 1, ні - інше число\n"))

    elif (n == 2):
        i = int(input("Виберіть до якого екземпляру додати елемент\n"))
        add = input("Введіть елемент\n")
        print(str(masss[i - 1].add(My_List(int([add])))))

    elif (n == 3):
        i = int(input("Виберіть від якого екземпляру відняти елемент\n"))
        d = int(input("Введіть номер елементу\n"))
        print(str(masss[i - 1].delete(d - 1)))

    elif (n == 4):
        for i in range(len(masss)):
            print(str(masss[i].sort()))

    elif (n == 5):
        for i in range(len(masss)):
            print(str(masss[i].vivod_revers()))

    elif (n == 6):
        for i in range(len(masss)):
            print(str(masss[i].sum()))


    elif (n == 7):
        N = len(masss)
        sortsum()
        for i in range(len(masss)):
            print(str((str(masss[i].mass) + " Сума = " + str(masss[i].sum()))))

    elif (n == 8):
        print("виберіть екзкмпляри для порівняння")
        a= int(input())
        b= int(input())
        if masss[a-1]<masss[b-1]:
            print(str(str(masss[a-1].mass) + "<" + str(masss[b-1].mass)))
        else:
            print (str(str(masss[a-1].mass) + ">=" + str(masss[b-1].mass)))

    elif (n == 9):
        i = int(input("Виберіть до якого екземпляру додати елемент\n"))
        add = int(input("Введіть елемент\n"))
        masss[i - 1] += My_List([add])
    elif (n == 10):

       sortsum()
       N = len(masss)
       masss[0] += masss[N-1]

    elif (n == 11):
        for i in range(len(masss)):
            print(str(masss[i]))

    elif (n == 0):
        menu = 0
    else:
        print("Некоректне введення\n")

