with open('task6.txt', 'r', encoding='utf-8') as new_file:
    my_dict = {}
    for i in new_file:
        subj, lect, pract, lab = i.split()
        try:
            int(lect)
        except ValueError:
            lect = '0'
        try:
            int(pract)
        except ValueError:
            pract = '0'
        try:
            int(lab)
        except ValueError:
            lab = '0'
        my_dict[subj] = int(lect) + int(pract) + int(lab)
    print(my_dict)
