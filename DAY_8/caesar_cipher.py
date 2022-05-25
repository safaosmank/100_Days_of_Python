import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(text_input, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for i in text_input:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            text_input += i
    print(f"Here's the {cipher_direction}d result: {cipher_text}")


end = False

while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25
    ceasar(text_input=text, shift_amount=shift, cipher_direction=direction)

    Continue = input("Type 'yes' if want to go again. Otherwise type 'no'.\n").lower()
    if Continue == "no":
        end = True
        print("Goodbye")