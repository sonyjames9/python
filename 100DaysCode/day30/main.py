try:
  file = open("100DaysCode/day30/a_file.text")
  a_dict = {"key":"value"}
  print(a_dict["sss"])
  print("try block")
except FileNotFoundError:
  file = open("100DaysCode/day30/a_file.text", "w")
  file.write("Something")
  print("FileNotFoundError block")
except KeyError as error_message:
  print(f"The key {error_message} does not exists")
  print("KeyError block")
else:
  content = file.read()
  print(content)
  print("else block")
finally:
  file.close()
  print("finally block")
  