# Definiowanie pozycji z ich wartością netto i stawką VAT
pozycje = [
    {"nazwa": "Clean Code, Robert C. Martin", "netto": 100.00, "stawka_vat": 8},
    {"nazwa": "Applying UML and Patterns, C. Larman", "netto": 300.00, "stawka_vat": 8},
    {"nazwa": "Wysyłka", "netto": 50.00, "stawka_vat": 23},
]

# Obliczanie wartości netto i VAT dla każdej stawki
wartosci_netto = {}
suma_vat = {}

for pozycja in pozycje:
    netto = pozycja["netto"]
    stawka_vat = pozycja["stawka_vat"]
    vat = netto * (stawka_vat / 100.0)
    
    if stawka_vat in wartosci_netto:
        wartosci_netto[stawka_vat] += netto
    else:
        wartosci_netto[stawka_vat] = netto
    
    if stawka_vat in suma_vat:
        suma_vat[stawka_vat] += vat
    else:
        suma_vat[stawka_vat] = vat

# Drukowanie podsumowania w formacie Markdown
print("| Stawka VAT | Razem netto | Kwota VAT |")
print("|------------|-------------|-----------|")

for stawka_vat in sorted(wartosci_netto.keys()):
    print(f"| VAT {stawka_vat}%       | {wartosci_netto[stawka_vat]:.2f} zł | {suma_vat[stawka_vat]:.2f} zł |")
