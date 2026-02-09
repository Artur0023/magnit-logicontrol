from app.services.data_loader import get_data
from app.services.visuals import  get_dashboard_kpi, get_top_oos_sku, get_supplier_sla

from bot.messages import START_TEXT
from bot.keyboards import main_menu
from bot.config import OOS_ALERT_THRESHOLD


def register_handlers(bot):
    '''
    Регистрирует обработчик команд Telegram-бота
    '''

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, START_TEXT, reply_markup=main_menu())
        check_oos_alert(bot, message.chat.id)


    @bot.message_handler(commands=['help'])
    def help_cmd(message):
        bot.send_message(message.chat.id, START_TEXT, reply_markup=main_menu())


    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        df = get_data()
        chat_id = call.message.chat.id

        if call.data == 'kpi':
            kpi = get_dashboard_kpi(df)
            text = (
                "Ключевые KPI:\n\n"
                f"- Средний DOH: {kpi['avg_doh']}\n"
                f"- HIGH OOS: {kpi['high_oos_share']}%\n"
                f"- SLA поставок: {kpi['sla_rate']}%\n"
                f"- Ср. задержка: {kpi['avg_delay']} дн"                
            )
            bot.send_message(chat_id, text)

        elif call.data == 'oos':
            top = get_top_oos_sku(df, top_n=5)
            text = 'SKU с высоким OOS:\n\n'
            for _, r in top.iterrows():
                text += (
                    f"{r['dc_id']} | {r['sku_id']} | "
                    f"DOH {round(r['avg_doh'],1)} | "
                    f"дней HIGH {r['days_high_oos']}\n"                    
                )
                bot.send_message(chat_id, text)

        elif call.data == "suppliers":
            sup = get_supplier_sla(df).sort_values("sla_rate").head(5)
            text = "Поставщики с худшим SLA:\n\n"
            for _, r in sup.iterrows():
                text += (
                    f"{r['supplier']} | "
                    f"SLA {round(r['sla_rate']*100,1)}% | "
                    f"Delay {round(r['avg_delay'],1)} дн\n"
                )
            bot.send_message(chat_id, text)

        elif call.data == "dc":
            dc_oos = (
                df.assign(oos_flag=df['oos_risk'] == 'HIGH')
                  .groupby('dc_id')['oos_flag']
                  .mean()
                  .reset_index()
            )
            text = "Доля OOS по РЦ:\n\n"
            for _, r in dc_oos.iterrows():
                text += f"{r['dc_id']}: {round(r['oos_flag']*100,1)}%\n"
            bot.send_message(chat_id, text)


def check_oos_alert(bot, chat_id):
    df = get_data()
    oos_rate = (df['oos_risk'] == 'HIGH').mean()

    if oos_rate > OOS_ALERT_THRESHOLD:
        bot.send_message(
            chat_id,
            f'ALERT!\nOOS превышает порог: {round(oos_rate*100,1)}%'
        )
