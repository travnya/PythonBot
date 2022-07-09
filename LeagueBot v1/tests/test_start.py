from LeagueBot import start
import pytest

# Тест отправляемых ботом сообщений в функции "start"
@pytest.mark.parametrize("Message",[('Вы уже зарегистрированы!'), (1111222233), ('Перед началом работы необходимо пройти регистрацию\n\nПожалуйста, укажите ваше ФИО\n'), ("Зарегистрируйтесь!"), ("Иванов 1111"),(11.11), ("Иванов Иван Иванович де Санта")])
def test_start(Message):
    assert start(message=Message)

