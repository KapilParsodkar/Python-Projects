alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(dire,t,s):
    nt=str()
    if dire=="decode":
        s*=-1
    for char in t:
       
        if char in alphabet:
            position =alphabet.index(char)
            new_p=position + s
            new_l=alphabet[new_p]
            nt+=new_l
        else:
            nt+=char
    print(f" the {dire}d result is {nt}")



end=False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    caesar(dire=direction, t=text, s=shift)
    retry=input(" type 'yes' to have a go again or type 'no' to exit :").lower()
    if retry=="no":
        end=True
        print(" kapil says Bye Bye")