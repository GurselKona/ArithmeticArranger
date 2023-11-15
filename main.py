def arithmetic_arranger(l_problems, b_calc=False):

  l_upper = []
  l_lower = []
  l_oper = []
  l_length = []
  l_calc = []
  output = ""

  if len(l_problems) > 5:
    output += "Error: Too many problems."
    return output

  # Splitting inputs and filling the lists

  for problem in l_problems:
    l_upper.append(problem.split()[0])
    l_lower.append(problem.split()[2])
    l_oper.append(problem.split()[1])
    l_length.append(max(len(problem.split()[0]), len(problem.split()[2])))

  # Catching errors

  try:
    l_upper = [int(x) for x in l_upper]
    l_lower = [int(x) for x in l_lower]
    if all([True if x <= 9999 else False for x in l_upper]) \
            and all([(True if x <= 9999 else False) for x in l_lower]) is True:
      pass
    else:
      output += "Error: Numbers cannot be more than four digits."
      return output
    if all([(True if x == "+" or x == "-" else False) for x in l_oper]) is True:
      pass
    else:
      output += "Error: Operator must be '+' or '-'."
      return output
  except ValueError:
    output += "Error: Numbers must only contain digits."
    return output

  # Determining and formatting output

  for i in range(len(l_upper)):
    output += f"{int(l_upper[i]):>{l_length[i] + 2}}    " if i != len(
      l_upper) - 1 else f"{int(l_upper[i]):>{l_length[i] + 2}}\n"
  for i in range(len(l_upper)):
    output += f"{l_oper[i]} {int(l_lower[i]):>{l_length[i]}}    " if i != len(
      l_upper) - 1 else f"{l_oper[i]} {int(l_lower[i]):>{l_length[i]}}\n"
  for i in range(len(l_upper)):
    if b_calc == True:
      output += f"{(l_length[i] + 2) * '-'}    " if i != len(l_upper) - 1 else f"{(l_length[i] + 2) * '-'}\n"
    else:
      output += f"{(l_length[i] + 2) * '-'}    " if i != len(l_upper) - 1 else f"{(l_length[i] + 2) * '-'}"

    # Calculate solutions

  if b_calc:
    for i in range(len(l_upper)):
      if l_oper[i] == "+":
        l_calc.append(l_upper[i] + l_lower[i])
      else:
        l_calc.append(l_upper[i] - l_lower[i])
      output += f"{l_calc[i]:>{l_length[i] + 2}}    " if i != len(l_upper) - 1 else f"{l_calc[i]:>{l_length[i] + 2}}"

  return output

if __name__ == '__main__':
  print(arithmetic_arranger(['32 - 698', '1 - 9380', '45 + 43', '123 + 49', '988 + 40'], True))