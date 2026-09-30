class ExtendedList(list):
    """Список с дополнительными методами."""

    def sum_values(self) -> int:
        return sum(self)

    def average(self) -> float:
        if not self:
            return 0.0

        return sum(self) / len(self)