def count_hi(str):
  result = 0
  for i in range(len(str)-1):
    if str[i:i+2] == "hi":
      result += 1
  return result
