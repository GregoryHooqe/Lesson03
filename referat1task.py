with open('referatpython.txt', 'r', encoding='utf-8') as f:
    data1 = f.read().replace("\n", "")
    data1 = data1.replace(".", "!")
    print(data1)
    print(len(data1))
    print(len(data1.split()))