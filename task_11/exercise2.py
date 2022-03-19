def punc(string: str) -> str:
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in string:  
        if ele in punc:  
            string = string.replace(ele, "") 
    return string

def puncList(lis: list) -> list:
    lis = [punc(i) for i in lis]
    return lis

def most_common_words(filepath: str, number_of_words: int) -> list:
    with open(filepath, 'r+', encoding="utf8") as rf:
        dataList = puncList(rf.read().split())
        unique_words = set(dataList)
        result = []
        for words in unique_words :
            if dataList.count(words) == number_of_words:
                result.append(words)
        return sorted(result)