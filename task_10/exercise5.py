def count_letters(text: str) -> dict:
  result = dict()
  for letter in text:
    if letter not in result:
      result[letter] = 0
    result[letter] += 1
  return result