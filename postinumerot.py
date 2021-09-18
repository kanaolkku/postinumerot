#importtaa työvälineet
import json
import urllib.request

#Haetaan postinumerodata netistä
def get_data():
        with urllib.request.urlopen("https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json") as res:
            data = res.read()
        #muunnetaan data kirjastoksi
        return json.loads(data)
postinumerot = get_data()
    #Järjestetään data uuteen muotoon
    #Uusi data voidaan tallentaa myös muualle, josta voidaan hakea data ajamatta funktiota
def rearrangeData(data):
        #luodaan uusi tyhjä kirjasto
        newData = {}
        #käydään läpi jokainen avain-arvo pari
        for postinumero, postitmp in postinumerot.items():
            #asetetaan postitoimipaikka avaimeksi ja postinumerot asetetaan listassa oleviksi arvoiksi
            if postitmp in newData:
                #jos avain on olemassa, lisätään arvolistaan postinumero
                newData[postitmp] += [postinumero]
            else: 
                #jos avain ei ole olemassa, lisätään postitmp avaimiin ja postinumero sen arvolistan ensimmäiseksi
                newData[postitmp] = [postinumero]
        #palautetaan uusi kirjasto
        return newData
    
    #asetetaan uusi kirjasto muuttujaan

def main():
    postitoimipaikat = rearrangeData(postinumerot)
    
    #kysytään postitoimipaikkaa
    postitoimipaikka = input("Kirjoita postitoimipaikka: ").upper().strip()
    #tarkistetaan, että inputti on olemassa ehtolauseella
    if postitoimipaikka in postitoimipaikat:
    #mikäli inputti on olemassa, palauta lajiteltu
        lista = postitoimipaikat[postitoimipaikka]
        lista.sort()
        print(f"Postinumerot {lista}")
    else:
    #mikäli inputti ei ole olemassa, palauta virheviesti
        print("Postitoimipaikkaa ei löytynyt :(")
if __name__ == '__main__':
    main()