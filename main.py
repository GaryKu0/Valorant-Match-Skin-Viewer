import valclient
import json
import requests

run=False
try:
    client = Client(region='ap')
    client.activate()
    run=True
except Exception as e:
    print("Error: " + str(e))
    

search=False
lan='en-US'
Final = {}
def GetMatchPlayerSkin():
    print('Getting match player Data...')
    match = client.coregame_fetch_match_loadouts()
    print(type(match))
    match = match['Loadouts']
    character = []
    skin = []
    for i in match:
        if (uuid_character[i['CharacterID']] in character):
            tmp=uuid_character[i['CharacterID']]+'-enemy'
            character.append(tmp)
        else:
            character.append(uuid_character[i['CharacterID']])
        skin.append(i['Loadout']['Items'])
    print('Getting each character data...')
    print(character)
    weapon = []
    WeaponSkin = []
    print('Getting Skin data...')
    for s in skin:
        for i in s:
            WeaponSkin.append(s[i]['Sockets']["bcef87d6-209b-46c6-8b19-fbe40bd95abc"]["Item"]['ID'])
            weapon.append(uuid_weapon[i])
        weapon.append('NEXT')
        WeaponSkin.append('NEXT')
    weapon.pop()
    # ALL SKIN DATA
    url = "https://valorant-api.com/v1/weapons/skins?language="+lan
    response = requests.get(url)
    response = response.json()
    response = response['data']
    Name = []
    count = 0
    for i in WeaponSkin:
        if i != 'NEXT':
            for r in response:
                if r['uuid'] == i:
                    Name.append(r['displayName'])
        else:
            Final[character[count]] = Name
            Name=[]
            count += 1


uuid_character = {'dade69b4-4f5a-8528-247b-219e5a1facd6': 'Fade', 'f94c3b30-42be-e959-889c-5aa313dba261': 'Raze', '569fdd95-4d10-43ab-ca70-79becc718b46': 'Sage', '5f8d3a7f-467b-97f3-062c-13acf203c006': 'Breach', '22697a3d-45bf-8dd7-4fec-84a9e28c69d7': 'Chamber', '601dbbe7-43ce-be57-2a40-4abd24953621': 'KAY/O', '6f2a04ca-43e0-be17-7f36-b3908627744d': 'Skye', '117ed9e3-49f3-6512-3ccf-0cada7e3823b': 'Cypher', '320b2a48-4d9b-a075-30f1-1f93a9b638fa': 'Sova',
                  '1e58de9c-4950-5125-93e9-a0aee9f98746': 'Killjoy', '707eab51-4836-f488-046a-cda6bf494859': 'Viper', 'eb93336a-449b-9c1b-0a54-a891f7921d69': 'Phoneix', '41fb69c1-4189-7b37-f117-bcaf1e96f1bf': 'Astra', '9f0d8ba9-4140-b941-57d3-a7ad57c6b417': 'Brimstone', 'bb2a4828-46eb-8cd1-e765-15848195d751': 'Neon', '7f94d92c-4234-0a36-9646-3a87eb8b5c89': 'Yoru', 'a3bfb853-43b2-7238-a4f1-ad90e9e46bcc': 'Reyna', '8e253930-4c05-31dd-1b6c-968525494517': 'Omen', 'add6443a-41bd-e414-f6ad-e58d267f4e95': 'Jett'}
uuid_weapon = {'63e6c2b6-4a8e-869c-3d4c-e38355226584': 'Odin', '55d8a0f4-4274-ca67-fe2c-06ab45efdf58': 'Ares', '9c82e19d-4575-0200-1a81-3eacf00cf872': "Vandal", 'ae3de142-4d85-2547-dd26-4e90bed35cf7': 'Bulldog', "ee8e8d15-496b-07ac-e5f6-8fae5d4c7b1a": "Phantom", "ec845bf4-4f79-ddda-a3da-0db3774b2794": "Judge", "910be174-449b-c412-ab22-d0873436b21b": "Bucky", "44d4e95c-4157-0037-81b2-17841bf2e8e3": "Frenzy", "29a0cfab-485b-f5d5-779a-b59f85e204a8": "Classic",
               "1baa85b4-4c70-1284-64bb-6481dfc3bb4e": "Ghost", "e336c6b8-418d-9340-d77f-7a9e4cfe0702": "Sheriff", "42da8ccc-40d5-affc-beec-15aa47b42eda": "Shorty", 'a03b24d3-4319-996d-0f8c-94bbfba1dfc7': "Operator", "4ade7faa-4cf1-8376-95ef-39884480959b": "Guardian", "c4883e50-4494-202c-3ec3-6b8a9284f00b": "Marshal", "462080d1-4035-2937-7c09-27aa2a5c27a7": "Spectre", "f7e1b454-4ad4-1063-ec0a-159e56b58941": "Stinger", "2f59173c-4bed-b6c3-2191-dea9b58be9c7": "Melee"}

    
while run==True:
    inp=input("Enter a command: ")
    inp = inp.lower()
    if inp=="exit":
        run=False
    elif inp=="help":
        print("""
              |------------ Valorant Match Skin Check  -------------|
              |START - Start the program(Make sure you are in match)|
              |Language - Change the language(en-US,zh-TW,etc)      |
              |EXIT  - Exit the program                             |
              |---------------Thanks For Using----------------------|
              """)
    elif inp=="language":
        print("What language do you want Change to?(en-US,zh-TW,etc)")
        lan=input("Language: ")
    elif inp=="start":
        try:
            GetMatchPlayerSkin()
            run=False
            search=True
        except Exception as e:
            print("Error: " + str(e))
 
           
while search==True:
    inp=input("Which character Skin You Wanna See? (Agent Name) ")
    inp=inp.capitalize()
    print(inp)
    if inp=="Exit":
        search=False
        run=True
    elif inp in Final:
        w=1
        if (inp+"-enemy" in Final):
            w=input("Our team or Enemy Team(ours(1)/enemy(2))")
        if w==1:
            print(Final[inp])  
        else:
            print(Final[inp+"-enemy"])
    
    

