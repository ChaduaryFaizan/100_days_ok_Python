from alphabet import alphabets
def ceasercyfer(text,shift,encode_or_decode):


    
    enc_or_dec_mesg=""
    if encode_or_decode == "decode":
        shift  *=-1
    elif encode_or_decode=="encode":
        shift *= 1
    else :
        print("     Please select a valid option    ")
    for letter in text:
       
        index_total=0
        if letter in alphabets:
            index_total=alphabets.index(letter) + shift 
            total_shift = index_total % len(alphabets)
            enc_or_dec_mesg += alphabets[total_shift]
        elif letter not in alphabets:
            enc_or_dec_mesg+=letter
    print(f"The {encode_or_decode}d reasult is : {enc_or_dec_mesg}")      
        