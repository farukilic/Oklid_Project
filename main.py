def eucledianDistance(x1, y1, x2, y2):
    x1 = float(input("x1 değerini giriniz: "))
    y1 = float(input("y1 değerini giriniz: "))
    x2 = float(input("x2 değerini giriniz: "))
    y2 = float(input("y2 değerini giriniz: "))
    fark_x = x2 - x1
    fark_y = y2 - y1
    fark = (fark_x**2 + fark_y**2)**(1/2)
    return fark
uzunluk = eucledianDistance(0,16,8,0)
Distance = []
Distance.append(uzunluk)
print(Distance)
