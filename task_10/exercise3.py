def get_shortest_word(s: str) -> str:
    word = ""
    all_words = []
    s = s.replace('\n', "")
    s = s.replace('\t', "")
    s = s + " "

    for i in range(len(s)):
        if s[i] != ' ':
            word = word + s[i]
        else:
            all_words.append(word)
            word = ""

    shortest = "The string is empty"

    for i in range(len(all_words)):
        if len(all_words[i]) > 0:
            if len(shortest) > len(all_words[i]):
                shortest = all_words[i]

    return shortest