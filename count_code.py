def count_code(str):
  result = 0
  for i in range(len(str) - 3):
    if (str[i:i+2] + " " + str[i+3] == "co e"):
      result += 1
  return result
