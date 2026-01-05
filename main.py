import pandas as pd
import os

def main():
    file_path = "data/sales.csv"
    
    # Sprawdzenie czy folder i plik istnieją (dobre praktyki inżynierskie)
    if not os.path.exists(file_path):
        print(f"Błąd: Nie znaleziono pliku {file_path}")
        return

    try:
        # 1. Wczytanie danych
        df = pd.read_csv(file_path)
        print(f"Liczba rekordów na wejściu: {len(df)}")

        # 2. Czyszczenie danych (Data Cleaning)
        df = df[df["status"] != "refunded"]
        df = df[df["customer"].notna()]
        df["customer"] = df["customer"].str.strip()
        df["commission_rate"] = df["commission_rate"].fillna(0.05)
        df = df[df["amount"] > 0]

        print(f"Liczba rekordów po czyszczeniu: {len(df)}")

        # 3. Transformacja i obliczenia (Business Logic)
        df["commission"] = round(df["amount"] * df["commission_rate"], 2)
        df["amount_net"] = df["amount"] - df["commission"]

        # 4. Zapis danych (Load)
        os.makedirs("data", exist_ok=True) # Tworzy folder jeśli nie istnieje
        df.to_csv("data/sales_cleaned.csv", index=False)
        print("Plik wynikowy został zapisany w data/sales_cleaned.csv")

        # 5. Raport analityczny
        print("-" * 30)
        print(f"Suma sprzedaży: {df['amount'].sum():.2f}")
        print(f"Suma prowizji:  {df['commission'].sum():.2f}")
        print("\nTop 3 klienci wg sprzedaży:")
        print(df.groupby("customer")["amount"].sum().nlargest(3))
        print("-" * 30)

    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    main()
