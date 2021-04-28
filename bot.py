import amino
import os
 

from multiprocessing.pool import ThreadPool
from rich.console import Console

console = Console()

console.print("[yellow]╔╦═╦══╦╦════╦═╦╗╔╦══╦╦═╦╦═══╦╦╦╦═════╗")
console.print("[yellow]║║║╠══╬╬═╦═╗║╔╣╚╝╠═╦╣╠╗║╠═╦╦╬╬╣╠╦═╦═╗║")
console.print("[yellow]║║╩║║║║║║║║║║╚╣╔╗╠╝╠╗╔╣║║║║║║╠╗╔╣╩╣╠╝║")
console.print("[yellow]║╚╩╩╩╩╩╩╩╩═╝╚═╩╝╚╩═╝╚═╝╚╩╩╩═╩╝╚═╩═╩╝ ║")
console.print("[yellow]╚════════════════════════════════════╝\n")

console.print("[cyan]╔╦═╦═══╦═╦══╦╦══════════╗")
console.print("[cyan]║║░╩╦╦╗║╚╬═╦╣╠╦═╦═╦══╦╦╗║")
console.print("[cyan]║║░░║║║╠╗║║╠╗╔╣╩╬╝╠╗╚╣║║║")
console.print("[cyan]║╚══╬╗║╚═╩═╝╚═╩═╩═╩══╬╗║║")
console.print("[cyan]╚═══╩═╩══════════════╩═╩╝\n")

def curlist(data):
    curusers=[]
    for userId in data.profile.userId:
       curusers.append(userId)
    return curusers

def leadlist(data):
    leadusers=[]
    for userId in data.profile.userId:
       leadusers.append(userId)
    return leadusers

def userlist(data):
    listusers=[]
    for userId in data.profile.userId:
       if lvlchoice.lower() == '1':
          if sub_client.get_user_info(userId = userId).level<=x:           
             listusers.remove(userId)           
          else:
             listusers.append(userId)
             pass
       else:
           listusers.append(userId)
           pass  
    return listusers

def comlist():
        sub_clients = client.sub_clients(start=0, size=100)
        console.print("\n[cyan]Select the community: ")
        for x, name in enumerate(sub_clients.name, 1):
            console.print(f"[green]{x}. {name}")
        while True:
            choice_sub_client = console.input("[cyan]Enter community number: ")
            try:
                return sub_clients.comId[int(choice_sub_client) - 1]
            except (IndexError, TypeError):
                console.print("[red]Invalid community number! ")

def chatlist():
        get_chats = sub_client.get_chat_threads(start=0, size=100)
        chat_list = []
        x = 0
        console.print("\n[cyan]Select the chat: ")
        for name, thread_type, chatid in zip(get_chats.title, get_chats.type, get_chats.chatId):
            if thread_type != 0:
                x += 1
                console.print(f"[green]{x}. {name}")
                chat_list.append(chatid)
        while True:
            choice_chat = console.input("[cyan]Enter chat number: ")
            try:
                return chat_list[int(choice_chat) - 1]
            except IndexError:
                console.print("\n[red]Invalid chat number!")

client=amino.Client()
logger = True
while logger == True:
    email=console.input("[yellow]Email: ")
    password = console.input("[yellow]Password: ")
    try:
        client.login(email=email, password = password)
        console.print (f"\n[green]You successfully logged as {email}! ")
        logger = False
    except amino.exceptions.InvalidEmail:
        console.print ("[red]Wrong Email! Try again!")
    except amino.exceptions.InvalidPassword:
        console.print ("[red]Wrong Password! Try again!")
    except amino.exceptions.InvalidAccountOrPassword:
        console.print ("[red]Wrong Email or Password! Try again!")
    except amino.exceptions.AccountDoesntExist:
        console.print ("[red]Account doesn't exist! Try again!")
    except amino.exceptions.ActionNotAllowed:
         console.print ('[red]Your device id has been banned. Change it in device.json file and try again!')
         os._exit(1)
    except Exception as e:
          console.print (f'[red]{e}')
         
comId=comlist()  
sub_client=amino.SubClient(comId=comId, profile=client.profile)

choicer = False

while not choicer:
    console.print ('\n[cyan]Choose chat from the link, or from the list? ')
    console.print('[yellow]1 - from the link')
    chat_choice = console.input('[yellow]2 - from the list: ')
    switcher = False  
    while not switcher:
        if chat_choice.lower() == "1":
           link = console.input("\n[cyan]Link of the chat: ")                 
           try:
                object_id = client.get_from_code(str(link.split('/')[-1])).objectId
                switcher = True
                choicer = True
           except:
                console.print('[red]Wrong link!')
                console.print ('\n[cyan]Choose chat from the link, or from the list? ')
                console.print('[yellow]1 - from the link')
                chat_choice = console.input('[yellow]2 - from the list: ')
           pass
       
        elif chat_choice.lower() == "2":
            object_id = chatlist()
            choicer = True
            switcher = True
        else:
            console.print ('[red]Wrong number! ')
            console.print ('\n[cyan]Choose chat from the link, or from the list? ')
            console.print('[yellow]1 - from the link')
            chat_choice = console.input('[yellow]2 - from the list: ')


Your_decisions_determine_your_destiny = False

while not Your_decisions_determine_your_destiny:
    max = int(console.input("\n[yellow]Max members to invite: "))
    scrapper = False
    while not scrapper:
        pool_count = int(console.input("\n[yellow]Number of invitations per turn? (1-500): ")) 
        if pool_count >=1 and pool_count <= 500:
           scrapper = True       
        else:
            console.print("\n[red]Wrong number! ") 

    console.print("\n[cyan]We have option to invite only if lvl of a user is higher then you set. Do you need this option? ")
    console.print('[yellow]1 - yes (takes more time)')     
    switcher = False
    while not switcher:
        lvlchoice = console.input('[yellow]2 - no: ')
        if lvlchoice.lower() == '1':

            lvlassist = False
            while not lvlassist:
                x = int(console.input("\n[yellow]Invite from what lvl? "))
                if x > 2 and x<20:
                    lvlassist = True
                else:
                     console.print("\n[red]Wrong level!")

            switcher = True
        elif lvlchoice.lower() == '2':
            switcher = True            
        else:
             console.print('[red]Wrong number!')
             console.print('[yellow]1 - yes (takes more time)')              

    pool = ThreadPool(pool_count)
    limit = 0
    sub_client.join_chat(object_id)    
    console.print ("\n[cyan]Collecting data...")

    while max>limit and len(sub_client.get_online_users(start = 0, size = 50).profile.userId)!=0:
            online_users = sub_client.get_online_users(start = 0, size = 50)
            usersCur = sub_client.get_all_users(type = "curators", start=0, size=50)
            usersLead = sub_client.get_all_users(type = "leaders", start=0, size=50)            
            for userId in (userlist(online_users)):            
                if userId not in (curlist(usersCur) and leadlist(usersLead)):
                    try:
                        pool.apply_async(sub_client.invite_to_chat, [userId, object_id])                
                    except:               
                        pass
                else:
                    pass
            limit += pool_count
            if limit < max:
                console.print(f"\n[green]{limit} users are invited...")
            else: 
                console.print(f"\n[green]{max} users are invited...")

    choice = console.input((f"\n[green]{max} members were invited. Wanna repeat? (y/n) "))
    if choice.lower() == "n":
        Your_decisions_determine_your_destiny = True
        console.print("\n[yellow]Ty for using the script. See ya!")
        os._exit(1)
