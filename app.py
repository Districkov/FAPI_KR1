from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from models import User, UserAge, Feedback [cite: 51]

app = FastAPI()

# Список для хранения отзывов (Задание 2.1) [cite: 84]
feedbacks_list = []

# Задание 1.1: Корневой URL [cite: 14]
@app.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"} [cite: 14]

# Задание 1.2: Возврат HTML-страницы [cite: 33]
@app.get("/index")
async def get_html():
    return FileResponse("index.html") [cite: 37]

# Задание 1.3*: Сложение чисел [cite: 38, 39]
@app.post("/calculate")
async def calculate(num1: int, num2: int):
    return {"result": num1 + num2} [cite: 41]

# Задание 1.4: Информация о пользователе [cite: 43, 44]
@app.get("/users")
async def get_user():
    # Создание экземпляра с вашим именем [cite: 51, 52]
    user_data = User(name="Ваше Имя и Фамилия", id=1) [cite: 52, 53]
    return user_data [cite: 54]

# Задание 1.5*: Проверка совершеннолетия [cite: 55, 56]
@app.post("/user")
async def check_age(user: UserAge):
    is_adult = user.age >= 18 [cite: 61]
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult [cite: 62]
    }

# Задания 2.1 и 2.2: Отправка отзывов [cite: 75, 94]
@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedbacks_list.append(feedback) [cite: 109]
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."} [cite: 110]