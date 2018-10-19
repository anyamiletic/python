from bs4 import BeautifulSoup
import requests


def main():
	brojac_firmi = 0

	for i in range(3):

		if(i == 0):
			html = requests.get("https://www.portal-srbija.com/proizvodnja-namestaja")
		else:
			html = requests.get("https://www.portal-srbija.com/proizvodnja-namestaja/" + str(i+1))

		soup = BeautifulSoup(html.content, features="html.parser")

		firme = soup.find_all('div', {"class": "general"})
		for f in firme:
			brojac_firmi += 1

			naziv_firme = f.find(class_="nazivfirme")
			print("naziv firme:")
			print(naziv_firme.get_text())

			grad = f.find(class_="grad")
			print("lokacija:")
			print(grad.get_text().strip())
			ulica = f.find(class_="street")
			print(ulica.get_text())

			telefon = f.find_all('a', {"class": "phone-number-gen"})
			for fon in telefon:
				print("telefon:")
				print(fon.get_text())

			web_site = f.find(class_="web_site")
			print("sajt:")
			if(web_site):
				print(web_site.get_text().strip())

			textfirma = f.find(class_="textfirma")
			print("tekst:")
			if(textfirma):
				print(textfirma.get_text().strip())
			print("_______________________________")

	print("Ukupno firmi: " + str(brojac_firmi))

if __name__ == "__main__":
	main()
