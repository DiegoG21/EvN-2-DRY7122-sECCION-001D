import urllib.parse
import requests 
import datetime 
hora_actual = datetime.datetime.now()
print ("Bienvenido ", hora_actual)
main_api = "https://www.mapquestapi.com/directions/v2/route?"
while True:
    orig = input("Ubicacion Inicial: ")
    if orig == "G" or orig == "g":
        break
    dest = input("Destino: ")
    if dest == "G" or dest == "g":
        break

    key = "Shcp2eEiBiU6s9LDhyjq392xWQmLEV2y"
    url = main_api + urllib.parse.urlencode ({"key" :key, "from" :orig, "to" :dest}) 
    json_data = requests.get (url) .json ()
    json_data = requests.get(url).json()
    json_status = json_data ["info"] ["statuscode"]

    if json_status == 0:
        print ("API Status:” + str (json_status) + “= Una llamada de ruta exitosa.\ n")
        print("=============================================")
        print("Direcion desde " + (orig) + " hasta " + (dest))
        print("Duracion de viaje: " + (json_data["route"]["formattedTime"]))
        #print ("Combustible usado (Gal): "+ str (json_data ["route"] ["FuelUsed"]))# Ya no soporta combustible
        print("Kilometros: " + str((json_data["route"]["distance"])*1.61))
        #print ("Combustible usado (Ltr): + str "((json_data ["route"] ["FuelUsed"])*3.78))#

    print("=============================================")

    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
