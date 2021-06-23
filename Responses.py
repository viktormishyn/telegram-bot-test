from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi'):
        return 'Hey! How are u doing?'

    if user_message in ('who are you', 'who are you?'):
        return "I'm Marcus"

    if user_message in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime('%d/%m/%y, %H:%M:%S')
        return date_time

    return "I don't understand you :=("
