from time import sleep

print('-----' * 8)
print('               AMAZON')
print('-----' * 8)

while True:
    products = input('Type it the name of the product: ').strip().upper()
    while True:
        try:
            int(products)
            print('Please, type it the name of the one product.')
            products = input('Type it the name of the product again: ').strip().upper()
        except ValueError:
            break
        
    while True:
        try:
            price = float(input('Type it the value of the product: R$'))
            break 
        except ValueError:
            print('Please, type it one value to the product.')

    while True:
        question = str(input('\nDo you want continue [Y or N]? ')).strip().upper()
        question_first_letter = question[0]

        if question_first_letter == 'N':
            print('Exiting...')
            sleep(2)
            exit()
        elif question_first_letter == 'Y':
            print('')
            break
        else:
            print('Chose one of them options, YES or NO.')





