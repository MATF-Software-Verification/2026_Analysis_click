# Analiza projekta otvorenog koda Click 

## Uvod
Click (Command Line Interface Creation Kit) je Python biblioteka za kreiranje interfejsa komandne linije.

## Informacije o autoru 
**Ime i prezime** Jelena Lazovic
**Broj indeksa** 1045/2024

# Linkovi do izvornog koda

- **Repository**: https://github.com/pallets/click
- **Analizirana grana**: main
- **Commit hash**: `cdab890e57a30a9f437b88ce9652f7bfce980c1f` 

## Korišćeni alati 

 # | Alat | Kategorija |  | Opis |
|---|------|-----------|--------|
| **1** | **Pytest (unit)** | Testiranje - jedinični | Testiranje pojedinačnih funkcija |
| **2** | **Pylint** | Statička analiza | Code quality, smells, kompleksnost |
| **3** | **MyPy** | Type checking | Provera type hints i type safety |
| **4** | **Bandit** | Security scanning | Skeniranje sigurnosnih ranjivosti |
| **5** | **Radon** | Code complexity | Cyclomatic complexity, maintainability |
| **6** | **Black** | Code formatting | Provera Python code style |

#### 1. Pytest - Unit testovi 
Napisano je 28 novih jediničnih testova koji pokrivaju:
- Edge cases sa Unicode karakterima
- Nested command groups
- Callback validacije
- Type validation boundary cases
- ...

**Pokretanje**
pytest unit_tests/ -v

**Zaključak** 
Click projekat već poseduje **odličnu baseline pokrivenost od 81%**, što je značajno 
iznad industrijskog standarda (60-70%). Ovo ukazuje na visok kvalitet postojeće test 
suite-a i pažljivu praksu testiranja.