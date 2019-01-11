#!/usr/bin/env python3

#######################################
# Auteur   : Alexandre LEVRET         #
# Parcours : ESILV 5A IBO spé FinTech #
# Module   : Python pour la finance   #
#######################################

from random import randint

Cartes = { # dictionnaire afin de ranger les cartes avec en key les cartes, et en value leurs valeurs numériques
		   # cas spécial pour l'As de base il est set à 1 mais l'utilisateur pourra choisir entre 1 et 11
	"As" : 1,
	"2" : 2,
	"3" : 3,
	"4" : 4,
	"5" : 5,
	"6" : 6,
	"7" : 7,
	"8" : 8,
	"9" : 9,
	"10": 10,
	"Valet" : 10,
	"Dame" : 10,
	"Roi" : 10
}

class Joueur(object): #Classe abstraite pour le Player et l'IA
	def __init__(self):
		self.__main = 0 # total des cartes dans la main du joueur
		self.__blackjack = False # le joueur fait "blackjack" lorsque sa main atteint exactement 21 en deux cartes (As + 10/Figure)
		self.__depasse = False # le joueur depasse lorsque sa main > 21

	@property
	def main(self):
		return self.__main
	@main.setter
	def main(self, valeur):
		self.__main = valeur
		return self.__main

	@property
	def blackjack(self):
		return self.__blackjack
	@blackjack.setter
	def blackjack(self, valeur):
		self.__blackjack = valeur
		return self.__blackjack	

	@property
	def depasse(self):
		return self.__depasse
	@depasse.setter
	def depasse(self, valeur):
		self.__depasse = valeur
		return self.__depasse

class Client(Joueur):
	def __init__(self):
		super(Client, self).__init__()
		self.__solde = 0 # argent dont dispose initiallement le client (nous)
		self.__mise = 0 # argent mis en jeu lors d'une manche
		self.__libelle = "Player" # son nom 

	@property
	def libelle(self):
		return self.__libelle
	
	@property
	def solde(self):
		return self.__solde
	@solde.setter
	def solde(self, valeur):
		if not isinstance(valeur, float):
			try:
				valeur = float(valeur)
				self.__solde = valeur
			except:
				raise TypeError("La valeur ne peut être convertible en float")
		else:
			self.__solde = valeur

	@property
	def mise(self):
		return self.__mise
	@mise.setter
	def mise(self, valeur):
		while type(valeur) != float:
			try:
				valeur = float(valeur)
			except:
				valeur = input("Rentrez une mise possible : ")
		self.__mise = valeur
	
	def Bet(self): # mise que le joueur met en jeu lors d'une manche, ne peut dépasser son solde
		print("Solde disponible : {}".format(self.__solde))
		self.mise = float(input("Veuillez rentrer votre mise : "))
		while self.__mise > self.__solde:
			print("La mise dépasse votre solde total")
			self.mise = float(input("Rentrez votre mise : "))
		self.__solde -= self.__mise
		print("\nLa partie est lancée !")
		print("Solde disponible : {}".format(self.__solde))
		print("Mise : {}".format(self.__mise))
		return self.__mise

	def Tirage(self): # le croupier tire une carte du talon et la présente au joueur, la valeur de la carte tirée va s'ajouter à sa main
		print("\n### TIRAGE ###\n")
		carte = randint(0, 12)
		carte = list(Cartes)[carte]
		valeur = Cartes.get(carte)
		if carte == "As":
			print("Vous avez tiré un {} d'une valeur de 1 ou 11.".format(carte))
			choix = int(input("Faites votre choix (1 / 11) : "))
			valeur = choix
		elif carte == "Dame":
			print("Vous avez tiré une {} d'une valeur de {}.".format(carte, valeur))
		elif carte == "Roi" or carte == "Valet":
			print("Vous avez tiré un {} d'une valeur de {}.".format(carte, valeur))
		else:
			print("Vous avez tiré un {}.".format(valeur))
		return valeur

	def __str__(self):
		return "\n---------------------------\nPlayer\nSolde disponible : {}\n---------------------------\n".format(self.__solde)

class IA(Joueur):
	def __init__(self):
		super(IA, self).__init__()
		self.__solde = randint(1, 1000) # attribue dès l'entrée au casino un solde random 
		self.__mise = 0
		self.__libelle = "IA"

	@property
	def libelle(self):
		return self.__libelle
	
	@property
	def solde(self):
		return self.__solde
	@solde.setter
	def solde(self, valeur):
		if not isinstance(valeur, float):
			try:
				valeur = float(valeur)
				self.__solde = valeur
			except:
				raise TypeError("La valeur ne peut être convertible en float")
		else:
			self.__solde = valeur

	@property
	def mise(self):
		return self.__mise
	@mise.setter
	def mise(self, valeur):
		if not isinstance(valeur, float):
			try:
				valeur = float(valeur)
				self.__mise = valeur
			except:
				raise TypeError("La valeur ne peut être convertible en float")
		else:
			self.__mise = valeur

	def Bet(self):
		self.__mise = randint(1, self.__solde) #peut miser entre 1 et son solde max
		self.__solde -= self.__mise
		print("\nLa partie est lancée !")
		print("Solde disponible : {}".format(self.__solde))
		print("Mise : {}".format(self.__mise))
		return self.__mise

	def Tirage(self):
		print("\n### TIRAGE ###\n")
		carte = randint(0, 12)
		carte = list(Cartes)[carte]
		valeur = Cartes.get(carte)
		if carte == "As":
			print("IA a tiré un {} d'une valeur de 1 ou 11.".format(carte))
			if (self.main + 11) == 21:
				valeur = 11
			elif (self.main + 11) > 21:
				valeur = 1
			else:
				tmp = randint(0,1)
				if tmp == 0:
					valeur = 1
				else:
					valeur = 11
			print("IA choisi de lui attribuer la valeur {}".format(valeur))
		elif carte == "Dame":
			print("IA a tiré une {} d'une valeur de {}.".format(carte, valeur))
		elif carte == "Roi" or carte == "Valet":
			print("IA a tiré un {} d'une valeur de {}.".format(carte, valeur))
		else:
			print("IA a tiré un {}.".format(valeur))
		return valeur

	def __str__(self):
		return "\n---------------------------\nIA\nSolde disponible : {}\n---------------------------\n".format(self.__solde)

class Croupier(Joueur):
	def __init__(self):
		super(Croupier, self).__init__()

	def Tirage(self):
		carte = randint(0, 12)
		carte = list(Cartes)[carte]
		valeur = Cartes.get(carte)
		if carte == "As":
			if (self.main + 11) <= 21:
				print("Le croupier a tiré un {} d'une valeur de 11.".format(carte))
				valeur = 11
			else:
				print("Le croupier a tiré un {} d'une valeur de {}.".format(carte, valeur))
		elif carte == "Dame":
			print("Le croupier a tiré une {}.".format(carte))
		else:
			print("Le croupier a tiré un {}.".format(carte))
		return valeur

def Check2(Player, Dealer): # check entre les deux mains, celle du client et celle du croupier laquelle gagne sur l'autre
	if Player.depasse == False and Dealer.depasse == True:
		print("{} a gagné d'office car le croupier a depassé 21. {} double sa mise.".format(Player.libelle, Player.libelle))
		Player.solde = Player.solde + (2 * Player.mise)
	elif Player.depasse == False and Dealer.depasse == False:
		if Player.blackjack == True and Dealer.blackjack == True:
			print("Le croupier et {} ont fait Blackjack ! {} récupère sa mise.".format(Player.libelle, Player.libelle))
			Player.solde += Player.mise
		elif Player.blackjack == False and Dealer.blackjack == True:
			print("Le croupier fait Blackjack, {} perd.".format(Player.libelle))
		elif Player.main > Dealer.main:
			print("{} le remporte sur le croupier. Il double sa mise.".format(Player.libelle))
			Player.solde = Player.solde + (2 * Player.mise)
		elif Player.main < Dealer.main:
			print("{} perd par rapport au croupier.".format(Player.libelle))
		elif Player.main == Dealer.main:
			print("{} est à égalité avec le croupier. Il récupére sa mise.".format(Player.libelle))
			Player.solde += Player.mise

def Check3(Player, Ordi, Dealer): # similaire à la fonction 'Check2' mais l'utilise deux fois, une fois entre le client et le croupier, puis entre l'IA et le croupier
	Check2(Player, Dealer)
	Check2(Ordi, Dealer)

def wait(): # Sert à segmanter les tours de chacun pour la lisibilité 
	print("\nAppuyer sur une touche pour continuer\n")
	input()

def Game(): # Lancement d'une table de Blackjack (et donc du programme)
	Player = Client()
	Dealer = Croupier()
	print("Bienvue au BlackJack")
	choix = input("Voulez-vous ajouter une intelligence artificielle ? (y/n) : ")
	if choix == "y" or choix == "Y":
		Ordi = IA()
		print("IA ajouté !")
	else:
		Ordi = None
		print("Vous jouerez tout seul face au croupier")

	Player.solde = float(input("Veuillez rentrer votre solde : "))

	continuerPartie = True
	while continuerPartie is True or Player.solde <= 0:
		stopTire = False
		Player.Bet()
		Player.main = 0
		Player.depasse = False
		Player.blackjack = False
		Dealer.main = 0
		Dealer.depasse = False
		Dealer.blackjack = False
		compteurPlayer = 2
		compteurDealer = 2
		premierTour = True
		while stopTire is False or Player.main >= 21:
			if premierTour == True: #Premier tirage, le croupier nous tire deux cartes
				Player.main += Player.Tirage()
				Player.main += Player.Tirage()
				premierTour = False
			else:
				Player.main += Player.Tirage()
			print("Vous êtes à {}".format(Player.main))
			if Player.main == 21 and compteurPlayer == 2:
				print("BlackJack !")
				Player.blackjack = True
				break
			elif Player.main == 21 and compteurPlayer > 2:
				print("Bravo vous êtes à 21 !")
				break
			elif Player.main > 21:
				print("Vous avez dépassé 21, vous avez perdu.")
				Player.depasse = True
				break
			choix = input("Tirer encore une carte (y/n) : ")
			if choix == "n":
				print("Vous vous arrêtez à {}.".format(Player.main))
				stopTire = True
				break
			compteurPlayer += 1

		if Ordi != None:
			wait()
			if Ordi.solde <= 0:
				print("IA ne peut plus jouer, il n'a pas les fonds nécessaires")
				Ordi == None
			else:
				print("\n----------------------------------------------------------\n")
				print("### Au tour de l'IA ###")
				print("\n---------------------------\nIA\nSolde disponible : {}\n---------------------------\n".format(Ordi.solde))
				Ordi.Bet()
				Ordi.main = 0
				Ordi.depasse = False
				Ordi.blackjack = False
				IAstopTire = False
				premierTour = True
				compteurIA = 2
				while IAstopTire == False:
					if premierTour == True:
						Ordi.main += Ordi.Tirage()
						Ordi.main += Ordi.Tirage()
						premierTour = False
					else:
						Ordi.main += Ordi.Tirage()
					print("IA est à {}".format(Ordi.main))
					if Ordi.main == 21 and compteurIA == 2:
						print("IA fait Blackjack !")
						Ordi.blackjack == True
						break
					elif Ordi.main == 21 and compteurIA > 2:
						break
					elif Ordi.main > 21:
						print("IA a dépassé 21, il perd.")
						Ordi.depasse = True
						break
					if Ordi.main > 16:
						IAstopTire = True
						break
					compteurIA += 1

		wait()

		print("\n----------------------------------------------------------\n")
		print("### Au croupier désormais ! ###\n")
		while Dealer.main < 17:
			Dealer.main += Dealer.Tirage()
			print("Le croupier en est à {}".format(Dealer.main))
			if Dealer.main == 21 and compteurDealer == 2:
				print("Blackjack !")
				Dealer.blackjack = True
			elif Dealer.main > 21:
				print("Le croupier a dépassé 21, il a perdu.")
				Dealer.depasse = True
			compteurDealer += 1

		if Ordi == None:
			Check2(Player, Dealer)
		else:
			Check3(Player, Ordi, Dealer)

		print(Player) #Etat en fin de manche
		if Ordi != None: # Lorsqu'il n'y a pas d'IA
			print(Ordi)
		if Player.solde <= 0:
			print("Vous n'avez plus d'argent. Vous ne pouvez plus jouer, aurevoir.")
			break

		nouvellePartie = input("Voulez-vous continuer de jouer (y/n) : ")
		if nouvellePartie == "n":
			continuerPartie = False
			print("Revenez vite nous voir ! ")

Game()
