# Импорты различных библиотек
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.emoji import emojize

# Кнопка отмены вызова тех. специалиста
cancel = KeyboardButton('Отмена')

# Кнопки главного меню
buttonTechHelp = KeyboardButton('Написать в тех. поддержку')
buttonFAQ = KeyboardButton('FAQ')
easterButton = KeyboardButton('Пасхалки')
links = KeyboardButton('Быстрый доступ к основным ссылкам Лиги')

# Кнопки пасхалок
easter1 = KeyboardButton('Создатели')
easter2 = KeyboardButton('Пасхалка')

# Кнопки меню FAQ
section_1 = KeyboardButton('Работа с запущенной сессией проф. развития')
section_2 = KeyboardButton('Создание сессии проф. развития')
section_3 = KeyboardButton('Работа с группой после запуска сессии')
section_4 = KeyboardButton('Работа с группой во время сессии')
section_5 = KeyboardButton('Работа при формировании группы')
section_6 = KeyboardButton('Работа с группой в работе')
section_7 = KeyboardButton('Конфигурирование практики')
section_8 = KeyboardButton('Гайдбуки')
back = KeyboardButton(emojize(':leftwards_arrow_with_hook:Вернуться в меню:leftwards_arrow_with_hook:'))

phoneButton = KeyboardButton(text='Отправить номер телефона', request_contact=True)

# Маркапы для кнопок
cancelMarkup = ReplyKeyboardMarkup(resize_keyboard=True).add(cancel)
phoneRequest = ReplyKeyboardMarkup(resize_keyboard=True).add(phoneButton)
easters = ReplyKeyboardMarkup(resize_keyboard=True).add(easter1).add(easter2).add(back)
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonFAQ).add(buttonTechHelp).add(easterButton).add(links)
FAQmenu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(section_1, section_2, section_3, section_4, section_5, section_6, section_7, section_8, back)


