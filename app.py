import telebot
from datetime import datetime

TOKEN = "8613774076:AAHPL5ao4mLdr9oYOrxZON3Pe5SxUkQqTDs"
bot = telebot.TeleBot(TOKEN)

# Comando /hola
@bot.message_handler(commands=['hola'])
def comando_hola(message):
    bot.reply_to(message, "¡Hola! Bienvenido al bot de la Tarea 5.")

# Comando /hora
@bot.message_handler(commands=['hora'])
def comando_hora(message):
    hora_actual = datetime.now().strftime("%H:%M:%S")
    bot.reply_to(message, f"La hora actual del servidor es: {hora_actual}")

# Comando /contacto
@bot.message_handler(commands=['contacto'])
def comando_contacto(message):
    bot.reply_to(message, "Puedes contactarnos al correo: 363473327001@ingenieria.usac.edu.gt")

# Comando /proyecto
@bot.message_handler(commands=['proyecto'])
def comando_proyecto(message):
    bot.reply_to(message, "Nuestro proyecto (HandTalk AI) consiste en un sistema de reconocimiento de lenguaje de señas en tiempo real usando Computer Vision y Machine Learning.")

print("Bot de la Tarea 5 escuchando comandos...")
# Esto mantiene al bot corriendo infinitamente esperando mensajes
bot.infinity_polling()