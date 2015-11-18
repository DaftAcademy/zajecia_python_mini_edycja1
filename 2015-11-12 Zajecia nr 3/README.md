# Zajęcia 3

## Materiały na drugie zajęcia:

Adres serwisu API z którego korzystamy: http://fixer.io/

Dodatkowo potrzebny będzie pakiet Requests (instalowany na pierwszych zajęciach)
oraz MatPlotLib. Aby go zainstalować, wystarczy wydać w konsoli komendę:

- `sudo pip install matplotlib` (uwaga, może potrwać kilka minut)

Jeśli powyższe nie zadziała (zdarzały się takie przypadki), należy uruchomić
komendę `sudo apt-get install python-matplotlib`.

### OS X

Osoby pracujące na komputerach ze zgniłym jabłkiem mogą napotkać na problem przy
importowaniu `matplotlib`a. Rozwiązanie problemu jest 2-linijkowe, można je
znaleźć [tutaj](https://coderwall.com/p/-k_93g/mac-os-x-valueerror-unknown-locale-utf-8-in-python).

## Praca domowa z trzecich zajęć:

Mamy nadzieję, że podzielenie zadań domowych na kategorie zależne od trudności
ułatwi Wam wybór tych, które zrobicie. Jak zawsze nie jest konieczne zrobienie
wszystkich, wystarczy zrobić jeden podpunkt, żeby wysłać rozwiązanie do
sprawdzenia - warto napisać w komentarzu które podpunkty się zrobiło :)

### Zadania najprostsze

- pozwolić na podanie wartości ustawionych dotychczas jako stałe (waluta
  bazowa, waluty docelowe) jako parametrów do funkcji. Podać domyślne rozsądne
  wartości (na przykład takie jak dotychczas były zapisane jako stałe)
- poprawić zapisywane daty kursów - zamiast takich jakie wynikają z działania
  `rozpatrywana_data + interwał`, takie jakie są zwracane przez usługę
  internetową. Należy przy tym sparsować napis z datą (`strptime`).

### Zadania proste

- zmodyfikować kod tak, aby struktura słownika nie była definiowana w trakcie
  jego uzupełniania, ale przed tym. Możliwa do wykorzystania wskazówka:
  `DefaultDict`. Ma to na celu zwiększenie czytelności kodu i jego łatwiejsze
  utrzymanie (modyfikowanie) w przyszłości.
- zmienić słownik na napisaną przez siebie klasę, która pozwala na proste użycie
  w pyplocie (czyli nie znacząco trudniej niż teraz). Cel: optymalizacja i/lub
  zwiększenie czytelności kodu.

### Zadania umiarkowanie proste

- przybliżyć wykresy funkcjami liniowymi (liniami trendu), narysować je i
  przewidzieć wynik na kilka interwałów do przodu (liczba interwałów podana jako
  parametr). Przykładowo 3 interwały ponad ostatnią znaną wartość.
- to samo co powyżej, ale przybliżenie funkcją wielomianową 3 stopnia (albo
  stopnia ustawialnego przez parametr)

### Zadania proste z gwiazdką

- dodać własną wymyśloną funkcjonalność (na przykład wykorzystanie innych
  funkcji używanego przez nas API) lub poprawki w kodzie wedle własnego uznania.
  To zadanie wymaga koniecznie co najmniej jednego zdania komentarza co się
  zmieniło :)

## Rozwiązania pracy domowej z trzecich zajęć:
Czekamy na nadsyłanie rozwiązań na event@daftcode.com do 22 listopada (niedziela)
włącznie :) Najciekawsze rozwiązania omówimy na zajęciach!