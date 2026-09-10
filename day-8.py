from alphabet import alphabets# cieser cifer
from enc_dec_function import ceasercyfer
from logo import logo_ceaser_cypher
print(logo_ceaser_cypher)
first_attempt=True
while first_attempt:
    first_try=0
    messasge = input("Enter text : ").lower()
    shift_no = int(input("Enter shift number to start with : "))
    enc_or_dec = input("What do you want encode or decode  : ").lower()
    ceasercyfer(text=messasge , shift=shift_no ,encode_or_decode= enc_or_dec)
    choice_to_continue=input("Do you want more Encrypt or Decrypt ( yes or  no ) :  ")
    if choice_to_continue=='yes':
        first_attempt=True
    elif choice_to_continue=='no':
        first_attempt=False