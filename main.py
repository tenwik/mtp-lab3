from animal import Dog
from book import Book
from vector import Vector


def main() -> None:
    dog = Dog("Шарик")
    print(dog.speak())

    first_vector = Vector(2, 3)
    second_vector = Vector(4, 5)
    result = first_vector + second_vector
    print("Сумма векторов:", result)

    book = Book("Мастер и Маргарита", "Михаил Булгаков")
    print("Книга:", book.get_info())


if __name__ == "__main__":
    main()