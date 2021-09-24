import vk_api
import os 
import shutil
from pyfiglet import Figlet
import time

os.system('clear') 
f = Figlet(font='ascii___')

def DrawText(text,center=True):
    if center:
      print(*[x.center(shutil.get_terminal_size().columns) for x in f.renderText(text).split("\n")],sep="\n")  
    else:
      print(f.renderText(text))

DrawText('666',center=True)
print("\033[35m{}\033[0m".format("\nДанный скрипт написал darknesss666🦋."))
TOKEN = input("\033[33m{}\033[0m".format("🔐Введи токен kate_mobile: "))
print('\033[33m{}\033[0m'.format('💠 Начинаю удаление сообщений...'))
token = vk_api.VkApi(token = TOKEN) 
vk = token.get_api()
#удаление всех сообщений
def del_msgs():
    while True:
        try:
            msg = vk.messages.getConversations(count=200, offset=0)['items']
            if not msg:
                print('💠 Удаление сообщений завершено.')
                break
            for i in msg:
                vk.messages.deleteConversation(user_id=i['conversation']['peer']['id'])
                print('\033[36m🔆 Диалог с vk.com/' + str(i['conversation']['peer']['id']) + ' был успешно удалён!')
                time.sleep(0.1)
        except Exception as er:
            print(er)
del_msgs()