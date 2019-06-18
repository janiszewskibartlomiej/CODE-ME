# Zadanie 03

Zmodyfikuj aplikację tak, aby spełniała następujące wymagania:
- Dodaj do aplikacji specjalnego użytkownika, który ma podgląd wszystkich danych w bazie. Aby to zrobić:
    - Dodaj nowe pole `is_admin` (typu BOOLEAN) w bazie danych `users`.
    - Zmodyfikuj pozostałych użytkowników, aby nie mieli dostępu administracyjnego.
    - Dodaj nowego użytkownika `admin`, który będzie miał pełen dostęp.
- Zmodyfikuj funkcję logowania tak, aby w ciasteczku sesji była również przechowywana informacja o tym, czy zalogowany użytkownik ma prawa administratora.
- Zmodyfikuj endpoint `index()` tak, aby dla użytkownika, który jest administratorem zwracała wszystkie wpisy w bazie danych (przedmioty wszystkich użytkowników).

## Dla chętnych:

W widoku administratora tabela powinna również wskazywać id użytkownika, do którego należy dany przedmiot (dla "jeszcze bardziej chętnych": należy wypisać nazwę zamiast id).
