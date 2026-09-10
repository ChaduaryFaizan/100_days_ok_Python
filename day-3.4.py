print('''             __   ____
           /   '~'   ) \
          / _(__  (__   \_
         / /(/  )) ) (\ \ \
        ( / (   (     )\ ) )
        )//"-_  )_.-"\ (    \
        )|-._     _.-- )( \ (
       (/){c)\| /"c)"7 )|\  )
        )|"""'| `"""" ( |  /_)
       ( |    --       ,/ / -_)
         \    __      / ." \ -_)
          \  /--\    //(   ( -_)
           \ `--'   //     ( -_)
            \____.-" |     ( -_)
              |      |    ( -_)
              |      |   ( -_)
              |      |  ( -_)
   _________-"\     / "-(_-_)___
  /                              \
 /                                \
 \                              __ \
  \     /             /        /   |
  /    /      /      /        /   /
 /     \____ /_____.'         \__/
|                             /
|                        |   /
|          __            |  /
\           __           /_"
 \          _           /
  '._______/ \________.'
             
          
''')
print("Welcome   ONE % persent    ")
print("You're   a prisoner who is willing to Escape")
print(" Your Choices can make to Escape :  have a go and TRY ")
choice1=input("Do You wana to Escape  : Yes  or  No  : ").lower()
if choice1=='yes'   :
    choice2=input(''' You have two Options for Escape
                  1- By Main gate  "Main"
                  2-By Climbing over Wall "Climb"  :  ''').lower()
    if choice2=='climb'  :
        choice3=input(" You are spoted by Guards \"Run\" or \" Surrender\"  :   ").lower()
        if choice3=='run'  :
            print(" Wohooooo.... You have succesfuly Escaped from prison ")
    
        elif choice3=='surrender' :
            print(" Cauhgt by Guards.")
            print(" Game Over")
        else:
            print("Enter Valid Choice from given Options")
    
        
    elif   choice2 == 'main':
        print("Game over                ")
        print(" Arested by Guards") 


    ## game starts from here


elif choice1=='no':
    print(" You does nit wab=nt to Escape right?         ")
    print(" Game Over ")
else:
    print(" Please Select Valid Options")