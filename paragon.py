pozycje = [
    {"nazwa": "Clean Code, Robert C. Martin", "netto": 100.00, "stawka_vat": 8},
    {"nazwa": "Applying UML and Patterns, C. Larman", "netto": 300.00, "stawka_vat": 8},
    {"nazwa": "Wysyłka", "netto": 50.00, "stawka_vat": 23},
]

wartosci_netto = {}
sumavat = {}

for i in pozycje:
    netto = i["netto"]
    stawka_vat = i["stawka_vat"]
    vat = netto * (stawka_vat / 100.0)
    
    wartosci_netto[stawka_vat] = wartosci_netto.get(stawka_vat, 0) + netto
    sumavat[stawka_vat] = sumavat.get(stawka_vat, 0) + vat

print("| Stawka VAT | Total netto | Kwota VAT |")
print("|------------|-------------|-----------|")

for stawka_vat, netto in sorted(wartosci_netto.items()):
    print(f"| VAT {stawka_vat}%       | {netto:.2f} zł | {sumavat[stawka_vat]:.2f} zł |")
