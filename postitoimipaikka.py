#importtaa tarvittavat työvälineet
import json
import urllib.request

#Tuo postinumerodata netistä
def get_data():
    with urllib.request.urlopen("https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json") as res:
            data = res.read()
        #muunnetaan data kirjastoksi
    return json.loads(data)

def main():
    postinumerot = get_data()
        #kysytään postinumeroa ja printataan vastaava postitmp
    postinumero = input("kirjoita postinumero: ")
    if postinumero in postinumerot:
        print(postinumerot[postinumero])
    else:
        print("Postinumerolla ei löytynyt postitoimipaikkaa :")
    
if __name__ == '__main__':
    main()