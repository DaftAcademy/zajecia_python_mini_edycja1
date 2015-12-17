# Zajęcia 5 - Aplikacja WWW

# UWAGA, zajęcia 6 odbędą się 14 stycznia 2016!

Zajęcia miały na celu przybliżenie Wam pisania prostych aplikacji webowych.
Aplikację będziemy rozwijać na następnych zajęciach.

## Materiały na piąte zajęcia:

Potrzebny jest pakiet Flask
Aby go zainstalować, wystarczy wydać w konsoli komendę:

- `sudo pip install Flask`

## Praca domowa z piątych zajęć:

Tym razem proponujemy dwie wersje:

### Zadania dla wszystkich

- Dodać w aplikacji widok, który zamiast strony internetowej, wygeneruje plik csv
  (który się ściąga w formie pliku na dysk), zawierający informacje jakie są aktualnie
  prezentowane na stronie
- Dodać w widoku strony internetowej link do pobrania danych w formie csv (korzystający z widoku
  z poprzedniego punktu)
- Po kliknięciu na nazwę procesu pojawiają się (w dowolnej formie, może być popup) dodatkowe informacje
  o tym procesie, które można uzyskać za pomocą biblioteki `psutil`

### Zadania dla wszystkich, którzy po powyższych zadaniach mają wciąż niespożyte zasoby kreatywności

- Rozwinięcie ostatniego zadania "dla wszystkich": przy szczegółowych informacjach o procesie
  jest możliwość wysłania do procesu sygnału SIGKILL lub dowolnie wybranego przez użytkownika
- Dodatkowo przy szczegółach procesu wyświetla się opis tego procesu (opis z komendy `man` lub
  np. jakiś wygoogle'any wynik)
- Dodatkowa funkcjonalność, wymyślona przez robiącego zadanie

Na rozwiązania prac domowych czekamy do 10 stycznia 2016 :)
