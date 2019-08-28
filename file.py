try:
    f = open('_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
   print(e)
