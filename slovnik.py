from collections import Counter

txt = input("Ввести текст: ").lower()
txt = txt.replace(",", "").replace(".", "")

def sorted(text):
    List = []
    for i in text.split():
        if len(i) > 3:
            List.append(i)
    List = list(set(List))
    List.sort()
    joined = "\n".join(List)
    return joined


def maxlen(text):
    text = text.split()
    text = list(set(text))
    text.sort(key=len)
    text.reverse()
    for i in text[0:5]:
        print(f'{i} - {len(i)} characters')
    return ""

def most_common_words(text):
    symb = '!@#$%^&*().,/\|`~"№;:?-+_'
    for i in text:
        if i in symb:
            text = text.replace(i, '')
    text = text.split()
    newtxt=[]
    for w in text:
        if len(w) > 3:
            newtxt.append(w)
    most_common_el = Counter(newtxt).most_common(5)
    for i in most_common_el:
        print(f'{i[0]} - {i[1]} times')
    return ''


uin = int(input(
    "Введiть дiю:\n"
    "1. Сортувати слова за алфавітом\n"
    "2. Топ 5 найдовших слiв\n"
    "3. Топ 5 найчастiше повторюваних слiв\n\t"))

if uin == 1:
    print(sorted(txt))
elif uin == 2:
    print(maxlen(txt))
elif uin == 3:
    print(most_common_words(txt))