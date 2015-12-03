# -*- coding: utf-8 -*-
 
import telebot 
from telebot import types 
import time 
from random import randint
 
TOKEN = '147485890:AAE-TljxM8kdHIeLXsUy2YPDk-mD-f6Vfks' 

#Referencia: https://www.youtube.com/watch?v=qXLVJponfqQ
frasesGil = {
    0:"And say: black, black...all day, is very bad.",
    1:"Fascineroso",
    2:"Caneda hijo de puta y ladrón",
    3:"Aúpa Atleti campeón",
    4:"La madre que le parió, trae aquí el gorro",
    5:"Ahora sí, me cago en la madre que los parió, cabrones!",
    6:"Sois los más grandes, los tíos más cojonudos, estoy a muerte con vosotros",
    7:"¡Los jugadores que tienen más cojones del mundo!",
    8:"Imperioso es lo más noble del mundo, incapaz de hacerte daño....HAHAAA IMPERIOSOOOOO!!! ¿Es una persona o no es una persona?",
    9:"Iba a fichar a un jugador importante y me he enterado que es maricón...Y digo no, a ese no le meto en el vestuario",
    10:"No hay derecho! No hay derecho! Eso es expulsión!",
    11:"Yo es que disfruto cuando pierde el Madrid...es que no lo puedo remediar",
}

frasesCallejeros = {
    0: "Tres escopetas tengo",
    1: "Pim, pam, toma lacasitos",
    2: "¿Qué es eso que tienes en el pelo?",
    3: "Quién es tu padre? Yo seguro que le conozco...",
    4: "Tomate saca la pistola"
}

def getFrases(tipo):
    frases = None
    if tipo == "gil":
        frases = frasesGil
    elif tipo == "callejeros":
        frases = frasesCallejeros
    numero = (randint(0,len(frases) - 1))
    print "Numero " + str(numero)
    return frases[numero]
 
bot = telebot.TeleBot(TOKEN) 

#Listener
def listener(messages):
    for m in messages: 
        cid = m.chat.id # Conversation ID
        print "[" + str(cid) + "]: " + m.text 
 
bot.set_update_listener(listener) 

#######
@bot.message_handler(commands=['gil']) 
def command_gil(m): 
    cid = m.chat.id
    bot.send_message( cid, getFrases('gil') )
 
@bot.message_handler(commands=['callejeros']) 
def command_callejeros(m): 
    cid = m.chat.id 
    bot.send_message( cid, getFrases('callejeros')) 
#######

bot.polling(none_stop=True) # If there're erros, continue working
