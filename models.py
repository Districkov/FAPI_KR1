from pydantic import BaseModel, Field, field_validator
import re

# Задание 1.4: Модель пользователя
class User(BaseModel):
    name: str [cite: 49]
    id: int [cite: 50]

# Задание 1.5: Модель пользователя для проверки возраста
class UserAge(BaseModel):
    name: str [cite: 58]
    age: int [cite: 59]

# Задания 2.1 и 2.2: Модель отзыва с валидацией
class Feedback(BaseModel):
    # Обязательное поле, от 2 до 50 символов [cite: 102]
    name: str = Field(..., min_length=2, max_length=50) [cite: 102]
    # Обязательное поле, от 10 до 500 символов [cite: 104]
    message: str = Field(..., min_length=10, max_length=500) [cite: 104]

    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, v: str):
        # Запрещенные слова: кринж, рофл, вайб [cite: 106]
        forbidden_words = ['кринж', 'рофл', 'вайб'] [cite: 106]
        for word in forbidden_words:
            # Поиск слова в любом регистре [cite: 106]
            if re.search(word, v, re.IGNORECASE):
                raise ValueError("Использование недопустимых слов") [cite: 106]
        return v