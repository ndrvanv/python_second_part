color = input('Your favorite color: ')
match color:
    case 'red' | 'orange':
        print("You like red or orange!")
    case 'green':
        print("You aren't hunter!")
    case 'blue' | 'purple':
        print("Yeah, it's classic!")
    case _:
        print("I don't understand")