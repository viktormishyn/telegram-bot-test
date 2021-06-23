from datetime import datetime
from random_image import cat


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if 'привет' in user_message:
        return 'Привет! Как дела?'

    elif 'кто' and 'ты' in user_message or 'зовут' in user_message or 'звать' in user_message:
        return "Меня зовут Марк"

    elif 'время' in user_message or 'сколько' and 'врем' in user_message or 'сколько час' in user_message or 'который час' in user_message:
        now = datetime.now()
        date_time = now.strftime('%d/%m/%y, %H:%M:%S')
        return f"Текущее время: {date_time}. Но время не имеет значения..."

    elif 'все ок' in user_message or 'норм' in user_message or 'нормально' in user_message or 'все' and 'хорошо' in user_message:
        return "=)"

    elif (len(''.join(x for x in user_message if x.isalpha())) == 2 and ('ок' in user_message)) \
            or len(''.join(x for x in user_message if x.isalpha())) == 3 and ('оки' in user_message):
        return '👍'

    elif 'погода' in user_message or 'погоду' in user_message or 'погоды' in user_message:
        return f"Пох на погоду"

    return f"Ниче не понял :=(. Лови котятку \n {cat()}"
