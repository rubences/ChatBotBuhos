import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "4d498320-036e-11e9-b3bd-230993bd7b325388d668-8f62-4acb-bc8e-38a9592e0d61"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


def answer_question():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]
    if answerclass == "Alimentacion":
        print ("Depende de la especie de buho. Algunos buhos comen arañas y otros invertebrados. Otros incluso pequeños mamíferos como ratones")
    elif answerclass == "Distribucion":
         print ("Algunos buhos viven en desiertos, otros en bosques. También habitan zonas Articas")
    elif answerclass == "Esperanza_de_vida":
         print ("Un búho salvaje puede vivir hasta un máximo de 20 años, pero un búho en cautividad puede superar sin problemas los 50 años de edad. ")
    elif answerclass == "Especies":
         print ("Búho es el nombre común de aves de la familia Strigidae, del orden de los estrigiformes o aves rapaces nocturnas. Habitualmente designa especies que, a diferencia de las lechuzas, tienen plumas alzadas que parecen orejas y presentan una coloración amarilla o naranja en el iris.")
    elif answerclass == "Dimensiones":
         print ("El tamaño varía según la especie, el más pequeño es el mochuelo que mide 13,5 cm")
            
print ("¿Qué te gustaría saber de los búhos?")
    
while True:
    answer_question()   