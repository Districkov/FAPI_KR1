from pydantic import BaseModel, Field, field_validator
import re

# Задание 1.4: Модель пользователя
class User(BaseModel):
    name: str
    id: int

# Задание 1.5: Модель пользователя для проверки возраста
class UserAge(BaseModel):
    name: str
    age: int

# Задания 2.1 и 2.2: Модель отзыва с валидацией
class Feedback(BaseModel):
    # Обязательное поле, от 2 до 50 символов
    name: str = Field(..., min_length=2, max_length=50)
    # Обязательное поле, от 10 до 500 символов
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, v: str):
        # Запрещенные слова: кринж, рофл, вайб
        forbidden_words = ['кринж', 'рофл', 'вайб']
        for word in forbidden_words:
            # Поиск слова в любом регистре
            if re.search(word, v, re.IGNORECASE):
                raise ValueError("Использование недопустимых слов")
        return v