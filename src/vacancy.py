class Vacancy:
    """Класс для описания вакансий"""

    name: str  # Название вакансии
    area: str  # Населенный пункт
    url: str  # Ссылка на вакансию
    description: str  # Описание
    salary_from: float | str  # Зарплата от,,,
    salary_to: float | str  # Зарплата до ,,,

    __slots__ = ("name", "area", "url", "salary_from", "salary_to", "description")

    def __init__(self, name: str, area: str, url: str, salary_from: str, salary_to: str, description: str) -> None:
        self.name: str = name
        self.area: str = area
        self.url: str = url
        self.salary_from: str = salary_from if salary_from else "0"
        self.salary_to: str = salary_to if salary_to else "0"

        self.description: str = description

    def __str__(self) -> str:
        return f"{self.name}, {self.area}, Зарплата: от {self.salary_from} до {self.salary_to}, Ссылка: {self.url}"

    def __lt__(self, other: "Vacancy") -> bool:
        return int(self.salary_to) < int(other.salary_to)

    def validate(self) -> None:
        if not self.name or not self.url:
            raise ValueError("Название и ссылка на вакансию обязательны.")
