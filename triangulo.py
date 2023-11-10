
a = (input("Digite o valor de a: "))
b = (input("Digite o valor de b: "))
c = (input("Digite o valor de c: "))

 s = (a + b + c) / 2
 area = (s * (s - a) * (s - b) * (s - c)) ** 0.5


if a < b + c and b < a + c and c < a + b:

    print( "Os valores formam um triângulo e a área é: " , area)
else:

    print("Os valores não formam um triângulo.")