def primo(x):
    count = 0
    if x == 1:
        return True
    else:
        for i in range(1,x+1):
            if x % i == 0:
                count += 1
        if count == 2:
            return True
        else:
            return False
total = 0
atual = 2
while total < 51:
    if primo(atual):
        total += 1
        print(atual, end='-')
    atual += 1