print('Dzień dobry')
jaka_kawa = input('Czy wybierasz kawę z mlekiem? [wpisz "tak" lub "nie"]: ')

if jaka_kawa == 'tak' or jaka_kawa == 't':
        jakie_mleko = input('Czy to ma być mleko sojowe czy krowie? [wpisz "sojowe" lub "krowie"]: ')

        if jakie_mleko == 'sojowe' or jakie_mleko == 's':
            print('\nWybrano kawę z mlekiem sojowym')
        elif jakie_mleko == 'krowie' or jakie_mleko == 'k':
            print('Wybrano kawę z mlekiem krowim')

        else:
            print('Nie rozumiem odpowiedzi')
            exit()

elif jaka_kawa == 'nie' or jaka_kawa == 'n':
     print('\nWybrano kawę czarną.')

else:
    print('Nie rozumiem odpowiedzi')
    exit()

czy_cukier = input('Czy dodać cukier? [wpisz "tak" lub "nie"]: ')
if czy_cukier == 'tak' or czy_cukier == 't':
    print('Wybrano kawę z cukrem')
elif czy_cukier == 'nie' or czy_cukier == 'n':
    print('Wybrano kawę bez cukru')

else:
    print('Nie rozumiem odpowiedzi')
    exit()

print('\nDziękujemy za skorzystanie z naszych usług')