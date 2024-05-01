def hypotenuse(x1, y1, x2, y2):
    fark_x = x1 - x2
    fark_y = y1 - y2
    fark = (fark_x**2 + fark_y**2)**(1/2)
    return fark

uzunluk = hypotenuse(0,16,8,0)
print(uzunluk)




