n = 10
while not n == 0:
    print(n)
    n -= 1

counter_hashtag = 1
while counter_hashtag < 10 + 1:
    print("#" * counter_hashtag)
    counter_hashtag += 1

counter_hashtag_two = 1
while True:
    if counter_hashtag_two <= 10:
        print(f'Dê 0 a 9 = {counter_hashtag_two}')
        counter_hashtag_two += 1
    elif 11 <= counter_hashtag_two <= 20:
        print(f'Dê 11 a 20 = {counter_hashtag_two}')
        counter_hashtag_two += 1
    else:
        break
