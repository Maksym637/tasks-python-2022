with open('data/unsorted_names.txt', 'r+') as rf:
    with open('data/sorted_names.txt', 'w') as wf:
        data = rf.readlines()
        data.sort()
        res = list(map(lambda s: s.strip(), data))
        for line in res:
            wf.write(line + '\n')