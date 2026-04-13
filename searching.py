from pathlib import Path
import json
import random
import time
import matplotlib.pyplot as plt


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

    seznam_jmen_json = ['unordered_numbers', 'ordered_numbers', 'dna_sequence']
    with open(file_name, "r") as file_path:
        data = json.load(file_path)
        if field in seznam_jmen_json:
            return data[field]
        else:
            return None


def linear_search(seznam_cisel, hledane_cislo):
    slovniok_cisla = {"positions": 0,
                      "count": 0}
    seznam_pozic = []
    count = 0
    for i, char in enumerate(seznam_cisel):
        if char == hledane_cislo:
            seznam_pozic.append(i)
            count += 1
    slovniok_cisla["positions"] = seznam_pozic
    slovniok_cisla["count"] = count
    return seznam_pozic, count


def binary_search(seznam_cisel, hledane_cislo):
    prvni_prvek = 0
    posledni_prvek = len(seznam_cisel) - 1
    serazeny_seznam_cisel = sorted(seznam_cisel)
    while prvni_prvek <= posledni_prvek:
        prostredni_prvek = ((posledni_prvek + prvni_prvek) // 2)
        if serazeny_seznam_cisel[prostredni_prvek] == hledane_cislo:
            return prostredni_prvek
        elif serazeny_seznam_cisel[prostredni_prvek] < hledane_cislo:
            prvni_prvek = prostredni_prvek + 1
        elif serazeny_seznam_cisel[prostredni_prvek] > hledane_cislo:
            posledni_prvek = prostredni_prvek - 1
    return None

pocet_prvku = [100, 500, 1000, 5000, 10000]
linear_casy = []
binar_casy = []
for prvek in pocet_prvku:
    seznam = (random.choices(range(0,100), prvek))
    hledane_cislo = 5

    start1 = time.perf_counter()
    linear_search(seznam, hledane_cislo)
    end1 = time.perf_counter()
    duration1 = end1 - start1
    linear_casy.append(duration1)

    start2 = time.perf_counter()
    binary_search(seznam, hledane_cislo)
    end2 = time.perf_counter()
    duration2 = end2 - start2
    binar_casy.append(duration2)

plt.plot(pocet_prvku, linear_casy)
plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Graf měření - lineární search")
plt.show()

plt.plot(pocet_prvku, binar_casy)
plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Graf měření - binární search")
plt.show()


def main():
    hledane_cislo = 5
    nesarazeny_seznam = read_data("sequential.json", "unordered_numbers")
    print(nesarazeny_seznam )
    slovnik_cisla = linear_search(nesarazeny_seznam, hledane_cislo)
    serazeny_seznam = read_data("sequential.json", "ordered_numbers")
    pozice_cisla = binary_search(serazeny_seznam, hledane_cislo)





# if __name__ == "__main__":
#     main()
