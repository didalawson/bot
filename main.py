from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='############################################')
dp = Dispatcher(bot)

month1=(''' ⬛VIP Monthly ⬛ \n\n  ✅ Free access to the VIP membership platform\n\nPrice: £99.00\nBilling period: 1 month\nBilling mode: recurring ''')
month2=(''' ⬛️ VIP Months ⬛\n⬛️⬛️ JOIN THE PREMIUM FOR MORE 😊  ⬛\n️⬛Your benefits:\n✅ 🚀By joining the Premium Telegram membership,✅ 🚀By joining the Premium Telegram membership, FX PREMIERESI you will have access to:\n

 ✅ 🚀By joining the Premium Telegram membership,
FX PREMIERESI you will have access to:
✅ 3 to 5 Signals Daily.
✅ 85% to 92% Success Rate.
✅ +20000 Pips from the Start.
✅ Weekly pips recount.
✅ Sell Forex Signals.
✅ Buy Forex Signals.
✅ Take Profit & Stop Loss per Signal.
✅ #Free access to the premium membership platform
Price: £250.00
Billing period: 6 months''')

month3 = (''' ⬛️ VIP LIFETIME ⬛️
Your benefits: 
✅ 🚀By joining the Premium Telegram membership, of
FX Premieresi you will have access to:

✅ 3 to 5 Signals Daily.
✅ 85% to 92% Success Rate.
✅ +20000 Pips from the Start.
✅ Weekly pips recount.
✅ Sell Forex Signals.
✅ Buy Forex Signals.
✅ Take Profit & Stop Loss per Signal.
✅Automated PROFIT BASE SYSTEM service (PBS)
✅Telegram Bot Integration
✅Trading Notifications
✅Trailing Functionality
✅Concurrent Stop/Take Profit Orders
✅Customer Support
✅Primary API Slots
✅Automatic Signals Following
Trading View Integration
✅Optimized 

Price: £300.00|£499.00 (Discount offer)
Billing period: Yearly

''')

button1 = KeyboardButton('⬛VIP MONTHLY £100.00/1MONTH⬛')
button2 = KeyboardButton('⬛VIP MONTHLY £249.00/6MONTH⬛')
button3 = KeyboardButton('⬛VIP YEARLY/LIFETIME £300/£499.00⬛')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).add(button3)

button4 = InlineKeyboardButton(text='⚡BTC', callback_data='btc')
button5 = InlineKeyboardButton(text='⚡ETH', callback_data='eth')
button6 = InlineKeyboardButton(text ='⚡TRC20', callback_data='trc')
keyboard2 = InlineKeyboardMarkup().add(button4,button5,button6)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply('''FXSIO 22\n  Welcome to '@xm_signals_bot  payment portal Purchase VIP of our real-time signal channel You will receive following benefits with our subscription package \n Verify screenshots for Instant Access when paid! Need help? Send a message to the bot for our admins to see. We will reply within 8 hours''', reply_markup=keyboard1)



@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text =='⬛VIP MONTHLY £100.00/1MONTH⬛':
        await message.answer(month1, reply_markup=keyboard2)

    elif message.text == '⬛VIP MONTHLY £249.00/6MONTH⬛':
        await message.answer(month2,reply_markup=keyboard2)
    elif message.text == '⬛VIP YEARLY/LIFETIME £300/£499.00⬛':
        await message.answer(month3, reply_markup=keyboard2)
    else:
        await message.answer(f'Invalid input: {message.text} ')

@dp.callback_query_handler(text = ["btc", "eth", "trc"])
async def value(call: types.CallbackQuery):
    if call.data == "btc":
        await call.message.answer('send btc to address bc1q3vmxq296emfvh9w8pfvajz66npn4k3fgm6gxrv')
    if call.data == "eth":
        await call.message.answer('send eth to address 0x597A66f10469Ecbe3b39E5AA60FA4D67C402c7dC')
    if call.data == "trc":
        await call.message.answer('send Trc to address TMyqqDL3WanS7Xgprfio1nXiNsCotow4Zp')
    await call.answer()

executor.start_polling(dp)
        
        
                                                    










