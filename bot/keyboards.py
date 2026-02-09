from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton('KPI', callback_data='kpi'),
        InlineKeyboardButton('OOS', callback_data='oos')
    )
    kb.add(
        InlineKeyboardButton('Поставщики', callback_data='suppliers'),
        InlineKeyboardButton('По РЦ', callback_data='dc')
    )
    return kb