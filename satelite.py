from datetime import datetime

def calculer_distance_satellite(heure_depart, heure_arrivee):
    depart = datetime.strptime(heure_depart, "%H:%M:%S.%f")
    arrivee = datetime.strptime(heure_arrivee, "%H:%M:%S.%f")

    difference_temps = (arrivee - depart).total_seconds()

    vitesse_lumiere = 299792458

    distance = vitesse_lumiere * difference_temps

    return round(distance, 2)

print(calculer_distance_satellite("9:58:37.289", "9:59:28.210"))