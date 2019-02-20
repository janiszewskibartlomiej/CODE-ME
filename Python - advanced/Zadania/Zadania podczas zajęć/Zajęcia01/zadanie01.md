# Zadanie 01-01

W rozgrywkach ligowych zwykle jest kilka kryteriów, które określają kolejność miejsc w tabeli. W angielskiej Premier League najpierw liczą się punkty (za zwycięstwo lub remis) a następnie różnicę pomiędzy golami zdobytymi a straconymi.

Dokończ implementację klasy `Zespol` z szablonu `zadanie01.py`.  

## Etap 1

- Zaimplementuj metodę `__lt__` albo `__gt__`, która umożliwi porównanie ze sobą dwóch zespołów po ilości punktów.
- Zaimplementuj metodę `__repr__`, która zwróci nazwę zespołu.

## Etap 2

- Zmodyfikuj metodę porównującą tak, aby w przypadku zespołów o tej samej liczbie punktów, brana była pod uwagę różnica bramek.
- Zmodyfikuj metodę `__repr__` tak, aby przy nazwie zespołu były widoczne zdobyte punkty i różnica bramek.

## Poprawny wynik:
```
[Manchester City (pts:65,rb:54), Liverpool (pts:65,rb:44), Tottenham Hotspur (pts:60,rb:29), Manchester United (pts:51,rb:17)]
```


