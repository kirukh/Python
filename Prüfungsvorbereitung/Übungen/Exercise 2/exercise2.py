import json

with open("Übungen/Exercise 2/books.json", 'r', encoding='utf-8') as file:
    books = json.load(file)

while True:
    try:
        print(
            f"1 zum laden der Library, 2 um ein Buch hinzuzufügen, 3 um Bücher zu löschen, 4 zum Speichern der Änderungen und 5 zum Beenden")
        entry = input("Was wollen sie ausführen?")

        if entry == "1":
            for book in books:
                print(
                    f"{book['titel']} von {book['autor']} ({book['erscheinungsjahr']})")

        elif entry == "2":
            titel = input("Titel des Buches: ")
            autor = input("Autor des Buches: ")
            erscheinungsjahr = input("Erscheinungsjahr des Buches: ")

            new_book = {
                "titel": titel,
                "autor": autor,
                "erscheinungsjahr": int(erscheinungsjahr)
            }

            books.append(new_book)

        elif entry == "3":
            titel = input("Titel des zu löschenden Buches: ")
            for book in books:
                if book['titel'] == titel:
                    books.remove(book)
                    break
            print(f"Buch '{titel}' wurde gelöscht.")

        elif entry == "4":
            new_libraray = input("Neue Bibliothek: ")
            with open(f"Übungen/Exercise 2/{new_libraray}.json", 'w', encoding='utf-8') as file:
                json.dump(books, file, ensure_ascii=False, indent=4)
            break

        elif entry == "5":
            print("Programm wird beendet.")
            break
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        continue
