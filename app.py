from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from models import User, UserAge, Feedback

app = FastAPI()

# Список для хранения отзывов (Задание 2.1)
feedbacks_list = []

# Задание 1.1: Корневой URL
@app.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

# Задание 1.2: Возврат HTML-страницы
@app.get("/index")
async def get_html():
    return FileResponse("index.html")

# Задание 1.3*: Сложение чисел
@app.post("/calculate")
async def calculate(num1: int, num2: int):
    return {"result": num1 + num2}

# Задание 1.4: Информация о пользователе
@app.get("/users")
async def get_user():
    # Создание экземпляра с вашим именем
    user_data = User(name="Ваше Имя и Фамилия", id=1)
    return user_data

# Задание 1.5*: Проверка совершеннолетия
@app.post("/user")
async def check_age(user: UserAge):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

# Задания 2.1 и 2.2: Отправка отзывов
@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedbacks_list.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}