a = float(input("ilk kenar uzunluğunu giriniz: "))
b = float(input("ikinci kenar uzunluğunu giriniz: "))
c = float(input("üçüncü kenar uzunluğunu giriniz: "))

s = (a + b + c) / 2

alan = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Üçgenin alanı = %0.2f" %alan)
