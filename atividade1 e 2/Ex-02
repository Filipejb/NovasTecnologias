def main():
  print("Caixa:")
  print_box(5, 10)

  print("\nOval:")
  print_oval(10, 20)

  print("\nLosango:")
  print_diamond(5)



def print_box(height, width):
  for i in range(height):
      if i == 0 or i == height - 1:
          print("*" * width)
      else:
          print("*" + " " * (width - 2) + "*")

def print_oval(height, width):
  if height % 2 == 0:
      height += 1 
  center_x = width / 2
  center_y = height / 2

  for y in range(height):
      line = ""
      for x in range(width):
          if ((x - center_x) / (width / 2)) ** 2 + ((y - center_y) / (height / 2)) ** 2 <= 1:
              line += "*"
          else:
              line += " "
      print(line)


def print_diamond(height):

  for i in range(1, height + 1):
      print(" " * (height - i) + "*" * (2 * i - 1))

  
  for i in range(height - 1, 0, -1):
      print(" " * (height - i) + "*" * (2 * i - 1))


if __name__ == "__main__":
  main()

