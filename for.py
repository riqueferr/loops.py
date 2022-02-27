for i in range(1, 8):
    if i == 5:
        continue
    print(i)

for counter in range(0, 11):
    if counter % 2 == 0:
        print(f'PAR (counter = {counter} == 0)')
    else:
        print(f'ÍMPAR (counter {counter} =! 0)')

for counter_hashtag in range(1, 11):
    print("#" * counter_hashtag)

start = 0
finish = 15 + 1
step = 3
for counter_numbers in range(start, finish, step):
    print(counter_numbers)
