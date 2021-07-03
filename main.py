# Created during the course "100 Days of Code - The Complete Python Pro Bootcamp for 2021" on udemy.com website

# Caesar Cipher - basic encryption algorithm
# Places letters in the text a certain distance in the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def change_the_text(input_text, f_shift, f_direction):
    output_text = ""
    if f_direction == "d":
        f_shift *= -1
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + f_shift) % (len(alphabet))
            output_text += alphabet[new_position]
        else:
            output_text += char
    print(output_text)

go_out = False
while not go_out:

    direction = input("Type 'E' to encrypt, type 'D' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    change_the_text (input_text=text, f_shift=shift, f_direction=direction)

    next_step = input("Input Q to quit the Caesar Cipher. ").lower()
    if (next_step == "q"):
        go_out = True
