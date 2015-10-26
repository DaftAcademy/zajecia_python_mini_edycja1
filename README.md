# Zajęcia z pythona na wydziale MINI PW

## Praca domowa z pierwszych zajęć:  
Poprawić kod programu napisanego na zajęciach w ten sposób, aby:

- był bardziej optymalny pod względem obliczeniowym jak i pamięciowym
- miał większą liczbę "sprytnych" funkcji, czyli takich, które pozwalają
  zmniejszyć ilość napisanego kodu, a dają ten sam efekt końcowy. Hint:
  dokumentacja BeautifulSoup, dokumentacja Pythona (built-in functions)
- eliminował problem pustych linii, które są generowane przez obecny program
- wpisywał do wyniku rating (ostatnia kolumna ze źródłowej tabeli), który póki
  co jest pusty lub jest znakiem "-". Rzecz jasna w formie tekstowej, nie
  obrazkowej.

## Prezentacja z pierwszych zajęć
Prezentację możesz obejrzeć [tutaj](http://balor.pl/zajecia_python/prez/#/)

## Obraz systemu
Jeśli udało Ci się uruchomić w pełni środowisko pythonowe, wraz z `ipython`em i
bibliotekami `requests`, `unicodecsv` i masz przyzwoity edytor tekstowy, możesz
ominąć ten punkt. Jeśli jednak chciał(a)byś skorzystać z przygotowanego przez
nas obrazu systemu, który już to wszystko ma skonfigurowane i działające:

- Zainstaluj VirtualBoxa w wersji 4.3.30
  [stąd](https://www.virtualbox.org/wiki/Download_Old_Builds_4_3)<br>
  Uwaga: nowsze wersje VirtualBoxa prawdopodobnie nie umożliwią obsługi
  wspólnego schowka, drag&drop pomiędzy hostem i wirtualną maszyną, itp.<br>
  Jeśli jednak się upierasz przy nowszej wersji VirtualBoxa, prawdopodobnie
  będziesz musiał(a) zainstalować pasujący do Twojej wersji
  [Extension Pack](https://www.virtualbox.org/wiki/Downloads).<br>
  (Zorientowałem się, że mam nienajnowszego VB kiedy obraz już zdążył pójść w świat - Antek)
- Ściągnij przygotowany przez nas obraz stąd:
    - [Part 1/2](http://we.tl/7y0PuG7zzs) lub [kopia na innym serwerze](https://copy.com/HQPazfqLcbKKtYGd)
    - [Part 2/2](http://we.tl/KbsQURCZtl) lub [kopia na innym serwerze](https://copy.com/KwGnOMtu6pRwuTTC)
- Rozpakuj pobrane pliki 7zip'em (w razie konieczności wybierz "otwórz plik za
  pomocą 7zip")
- Uruchom VirtualBoxa
- W menu File kliknij `Import Appliance`, po czym wybierz wypakowany plik
- Na następnym ekranie ustaw jakieś przyzwoite wartości, np. >1024MB pamięci,
  po czym kliknij `Import`
- Po lewej stronie powinna pojawić się zaimportowana maszyna. Zanacz ją i
  kliknij `Settings`.
- W dziale `System->Acceleration` zaznacz wszystkie kwadraciki, które są
  możliwe (na słabszych procesorach, takich jak Intel i3 może być część
  niedostępna).
- W dziale `Display` ustaw `Video Memory` na co najmniej 32MB
- W dziale `Network` upewnij się, że masz włączoną co najmniej jedną kartę
  sieciową w trybie `NAT` (lub jeśli będziesz mieć problemy, spróbuj `Bridged
  Adapter`)
- Zamknij okno ustawień przez `OK`
- Uruchom klikając na zieloną strzałkę `Start`
- Sprawdź czy wszystko działa (internet, terminal, python, ipython, sublime)
