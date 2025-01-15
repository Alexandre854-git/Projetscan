import socket
from datetime import datetime


def obtenir_cible():
    hostname = input("Entrez le nom d'hôte ou l'adresse IP de la cible : ")
    cible = socket.gethostbyname(hostname)
    print(f'Cible du scan  > {cible}')
    return cible


def obtenir_liste_ports():
    print(f'Plage des ports  > [1 – 255]')
    return range(1, 1024)


def scanner_port(cible, port):
    # Créer un objet socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Tester la connexion
        test = s.connect_ex((cible, port))
        if test == 0:
            print(f'Le port {port} est [ouvert]')


def scanner_ports():
    try:
        cible = obtenir_cible()
        liste_ports = obtenir_liste_ports()
        temps_debut = datetime.now()
        for port in liste_ports:
            scanner_port(cible, port)
    except Exception as e:
        print(f"Une erreur s'est produite ! Erreur : {e}")
    else:
        temps_fin = datetime.now()
        print("Scan terminé en", temps_fin - temps_debut)


if __name__ == '__main__':
    scanner_ports()
