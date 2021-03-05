import time
from pprint import pprint
import flask


messages = [
    {
        'name': 'Kate',
        'text': 'Hello, Im Kate!',
        'message_time': 1614922894.363384
    },
    {
        'name': 'Mike',
        'text': 'Hello, Im Mike!',
        'message_time': 1614925874.363384
    },
]



def send_message (name, text): #формирует сообщение в виде словаря
    message_time=time.time()   #и кладет в список 'messages'
    message = {
        'name': name,
        'text': text,
        'message_time': message_time
    }
    messages.append(message)
    print ('message sent')


last_after=0

def get_messages (after):
    responce = []    #создаем пустой список, стобы собрать туда сообщения для вывода
 #       {
 #           'name': 'test',  #тестовый элемент для проверок
 #           'text': 'test',
 #           'message_time': 0
 #       }]
    for message in messages:
        if message['message_time']>after: #при выполнении условия кладем сообщение в 'responce'
            responce.append(message)
    if len(responce) == 1:            #а если ничего не нашли, то сообщаем об этом
        print('No new messages')       #почему-то не работает
    for message in responce[50:]:         #выводит на экран последние 50 сообщений из 'responce'
        print ('***' + message['name'] + '***',
                message['text'],
                'Sent: ', message['message_time'])
    last_after= responce[-1]['message_time']
    responce.clear()
    print(last_after, 'test1')







print()
print()
print()
print('***send_message (Jake, hi, im Jake)')
send_message ('Jake', 'hi, im Jake')
print()
pprint('***get_messages (0)')
get_messages (0)
print()

print('***pprint(messages)')
pprint(messages)
print()

print('***send_message(Marta, Im Marta)')
send_message('Marta', 'Im Marta')

print('***pprint(messages)')
pprint(messages)

()
print('***get_messages(last_after)')
get_messages(last_after)

#pprint(messages)
print()
print()
print('***get_messages(last_after)')
get_messages(last_after)
