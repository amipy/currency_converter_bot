import telepot ,requests
token = '1318983381:AAGa8FUffct0lHjs12YiodJfCi9c_55CsjY'
telegram_bot = telepot.Bot(token)
current_id=0
update = telegram_bot.getUpdates()
print('Reached main loop.')
while True:
    try:
        if len(update)>0:
            current_id = update[0]['update_id']
            message = update[0]['message']['text']
            div_message = message.split(' ')
            chat_id = update[0]['message']['chat']['id']
            print()
            print(f'id :{current_id}')
            print(f'message :{message}')
            print(f'list :{div_message}')
            print(f'chat id :{chat_id}')
            if (len(div_message) == 3) and (div_message[0].isdigit()):
                telegram_bot.sendMessage(chat_id, 'Proccesing request.')
                base = div_message[1].upper()
                symbol = div_message[2].upper()
                conversion_rate = requests.get(url=f'https://api.exchangeratesapi.io/latest?base={base}&symbols={symbol}').json()
                if 'error' in conversion_rate.keys():
                    telegram_bot.sendMessage(chat_id, conversion_rate['error'])
                    resp=conversion_rate['error']
                    print(f'response :{resp}')
                else:
                    rate = conversion_rate['rates'][symbol]
                    converted = round(int(div_message[0])*rate,2)
                    telegram_bot.sendMessage(chat_id, f'{div_message[0]} {base} is equal to {converted} {symbol}, at {rate} {symbol} per {base}.')
                    print('response :{div_message[0]} {base} is equal to {converted} {symbol}, at {exchange_rate} {symbol} per {base}.')
            else:
                if message == '/start':
                    telegram_bot.sendMessage(chat_id, 'Hello! I am an auto currency conversion bot.\nTo use me, type the amount of currency you want to convert, followed by the name of the currency you are converting from and to.\nIE: 100 USD CAD converts 100 US dollars to Canadian dollars.')
                else:
                    telegram_bot.sendMessage(chat_id, 'I did not understand your inquiry.')
                    print('response :I did not understand your inquiry.')
        update = telegram_bot.getUpdates(current_id+1)
    except Exception as problem:
        print(problem)
        telegram_bot.sendMessage(chat_id, 'This bot has chrashed and has restarted.')
