def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


for num in range(1, 101):
    if primo(num):
        print(" é primo.")
    else:
        print(" não é primo.")