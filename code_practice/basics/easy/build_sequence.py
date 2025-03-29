def build_seq(str):
  for i in range(len(str)):
    print(str[i:] + str[:i])

build_seq('abbaa')
