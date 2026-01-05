Python Sales Data Cleaning (ETL Pipeline)

📌 Cel projektu
Projekt automatyzuje proces czyszczenia i transformacji danych (Preprocessing) pochodzących z surowych zrzutów systemów e-commerce/ERP. Skrypt rozwiązuje typowe problemy z jakością danych, przygotowując je do dalszej analizy lub importu do bazy danych SQL.

🛠 Technologie
Język: Python 3.x

Biblioteka: pandas (kluczowe narzędzie do manipulacji danymi)

🔍 Zakres operacji (Data Cleaning)

Skrypt realizuje kompletny mini-proces ETL:

E (Extract): Automatyczne wczytywanie danych z plików CSV.

T (Transform): * Czyszczenie danych: usuwanie zbędnych spacji, obsługa brakujących wartości (NaN).

Walidacja: odfiltrowanie rekordów zwróconych lub błędnych.

Logika biznesowa: obliczanie prowizji oraz wyliczanie kwot netto na podstawie zdefiniowanych reguł.

L (Load): Zapis w pełni oczyszczonego zbioru do nowego pliku CSV, gotowego do zasilenia bazy danych.

📊 Wynik działania
Po uruchomieniu skryptu użytkownik otrzymuje:

Plik cleaned_sales_data.csv z poprawnymi typami danych i przeliczonymi wartościami.

Krótki raport w konsoli z podsumowaniem przetworzonych rekordów (Data Quality Check).
