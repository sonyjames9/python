from art import logo
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser_cipher(start_text, shift_by_pos, cipher_command):
  result = ""
  if cipher_command == "decode":
    shift_by_pos *= -1
  for ch in start_text:
    if ch in alphabet:
      position = alphabet.index(ch)
      new_position = position + shift_by_pos
      if new_position < 0 or new_position > 25:
        new_position = new_position % len(alphabet)
      result += alphabet[new_position]
    else:
      result += ch
  print(f"The {cipher_command}d text is {result}")


end_code = False
while not end_code:
  print(logo)
  command = input("Type 'encode' to encrypt or 'decode' to decrypt : ")
  text = input("Type the input message : ").lower()
  shift_pos = int(input("By how much places do you want to shift : "))

  ceaser_cipher(start_text=text, shift_by_pos=shift_pos,
                cipher_command=command)

  restart = input(
      "Type 'yes' to continue with code or type 'no' to end the code \n")
  os.system('cls || clear')
  if restart == 'no':
    end_code = True
    print('Good bye')

# ceaser_cipher(plain_text='xyz', shift_fwd_by_pos=2, cipher_command=encode)
# ceaser_cipher(plain_text='uvwxyz', shift_fwd_by_pos=6, cipher_command=encode)
# ceaser_cipher(plain_text='abcdefghijklmnopqrst', shift_fwd_by_pos=26, cipher_command=encode)
# ceaser_cipher(plain_text='abc', shift_fwd_by_pos=2, cipher_command=decode)
# ceaser_cipher(plain_text='abcdef', shift_fwd_by_pos=6, cipher_command=decode)
# ceaser_cipher(plain_text='abcdefghijklmnopqrst', shift_fwd_by_pos=2, cipher_command=decode)
