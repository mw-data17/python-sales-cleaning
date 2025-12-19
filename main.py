import pandas as pd


def main():
    # 1. Wczytanie danych
    df = pd.read_csv("data/sales.csv")

    print("Liczba rekordów na wejściu:", len(df))

    # 2. Czyszczenie danych
    # usunięcie zwrotów
    df = df[df["status"] != "refunded"]

    # usunięcie brakujących klientów
    df = df[df["customer"].notna()]

    # usunięcie nadmiarowych spacji w nazwach klientów
    df["customer"] = df["customer"].str.strip()

    # uzupełnienie brakującej prowizji domyślną wartością
    df["commission_rate"] = df["commission_rate"].fillna(0.05)

    # usunięcie kwot <= 0
    df = df[df["amount"] > 0]

    print("Liczba rekordów po czyszczeniu:", len(df))

    # 3. Obliczenia
    df["commission"] = df["amount"] * df["commission_rate"]
    df["amount_net"] = df["amount"] - df["commission"]

    # 4. Zapis danych
    df.to_csv("data/sales_cleaned.csv", index=False)

    # 5. Mini raport
    print("\nSuma sprzedaży:", round(df["amount"].sum(), 2))
    print("Suma prowizji:", round(df["commission"].sum(), 2))

    print("\nTop 3 klienci wg sprzedaży:")
    top_customers = (
        df.groupby("customer")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )
    print(top_customers)


if __name__ == "__main__":
    main()
