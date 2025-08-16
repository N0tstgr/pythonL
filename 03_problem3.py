def table():
    for num in range(2, 26):
      filename = f"table{num}.txt"
      with open(f"table{num}.txt", "w") as f:

       for i in range(1, 11):
        f.write(f"{num} X {i} =  {num*i}\n")


table()
