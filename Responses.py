from datetime import datetime
from random_image import cat


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('привет', 'hi'):
        return 'Привет! Как дела?'

    if user_message in ('кто ты', 'кто ты?'):
        return "Меня зовут Марк"

    if user_message in ('время', 'время?'):
        now = datetime.now()
        date_time = now.strftime('%d/%m/%y, %H:%M:%S')
        return date_time

    return f"Ниче не понял :=(. Лови котятку \n {cat()}"
