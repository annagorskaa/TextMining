import re

''''Funkcja służąca do wyodrebniania hasztagów z tekstu'''


def wyodrebnij_hashtagi(tekst: str) -> list:
    wynik = re.findall(r'#[a-z0-9_]+', tekst)
    return wynik
