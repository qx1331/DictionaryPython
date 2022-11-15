txt = input("Ввести текст: ").lower()
txt = txt.replace(",", "")
txt = txt.replace(".", "")

###################
def sorted(text):

    a = text.split()
    spis = []
    for i in a:
        if len(i) > 3:
            spis.append(i)
    spis = set(spis)
    spis = list(spis)
    spis.sort()
    b = "\n".join(spis)
    return b


###########
def maxlen(text):

    text = text.split()
    text = set(text)
    text = list(text)
    text.sort(key=len)
    text.reverse()
    return "\n".join(text[0:5])


###########
def maxfreq(List):
    count = 0
    word = List[0]
    for i in List:
        cur = List.count(i)
        if cur > count and len(i) > 3:
            count = cur
            word = i
    for i in range(List.count(word)):
        txt.remove(word)

    return word


############
uin = int(input(
    "Введiть дiю:\n1. Сортувати слова за алфавітом\n2. Топ 5 найдовших слiв\n3. Топ 5 найчастiше повторюваних слiв\n\t"))
if uin == 1:
    print(sorted(txt))
elif uin == 2:
    print(maxlen(txt))
elif uin == 3:
    while True:
        txt = txt.split()
        for i in range(5):
            print(maxfreq(txt))
        break
