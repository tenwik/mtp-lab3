class Book:
    """Книга с названием и автором."""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def get_info(self) -> str:
        return f"«{self.title}», автор: {self.author}"
