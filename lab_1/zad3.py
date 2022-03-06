import re

''''Funkcja służąca do wyodrebniania emotikonów z tekstu'''


def wyodrebnij_emotikony(tekst: str) -> list:
    wynik = re.findall(r'[:|;][-]?[)|(|<|>]', tekst)
    return wynik
