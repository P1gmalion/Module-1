def spam(number):
    return 'bulochka'*number


def my_sum(list_of_numbers):
    summa = 0
    for i in list_of_numbers:
        summa += i
    return summa



def shortener(string):
    return " ".join(map(lambda string: string if len(string) < 7 else string[:6] + "*", string.split()))


def compare_ends(words):
    count = 0
    for word in words:
        if (len(word) >= 2) and (word[0] == word[-1]):
            count += 1
    return count







