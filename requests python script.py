#gebruik de requests-module om gegevens op te halen van de "JSONPlaceholder" API (https://jsonplaceholder.typicode.com/) 
# #instructies:







# import requests

# # 1: haal gegevens op van de API-endpoint /todos/1
# response= requests.get("https://jsonplaceholder.typicode.com/todos/1")
# # 2: Decodeer de JSON-reactie
# data = response.json()
# # 3: Toon de titel van de taak in de console (haal value van key 'title' in dictionary data)
# titel = data['title']
# print(titel)


# #uitbreiding, task "completed" check
# status = data["completed"]
# print(status)
# if status == False:
#     print('Er moet nog werk worden gedaan')

# else:
#     print("Goed gedaan!")    




#CAT API oefening: ophalen foto, openen in browser en opslaan lokaal
    
# import webbrowser
# import requests

# request = requests.get("https://dog.ceo/api/breeds/image/random")
# data = request.json()
# url = data['message']

# webbrowser.open(url)
# afbeelding = requests.get(url)
# with open(r"C:\Users\mathi\Desktop\test/hond.jpg","wb") as hond:
#     hond.write(afbeelding.content)



#oefening api moppen: 
import requests

input = int(input("Wat is je leeftijd? "))
            
if input < 18:
    counter = 0
    while counter < 1:

        response = requests.get("https://moppenbot.nl/api/random/")
        data = response.json()
        adult = data['joke']["nsfw"]
        mop = data['joke']['joke']
        print(adult)
        if adult == False:
            print(mop)
            counter +=1 
        if adult == True:
            
            continue
        
        

else:
    response = requests.get("https://moppenbot.nl/api/random/")
    data = response.json()
    mop = data['joke']['joke']
    print(mop)
      