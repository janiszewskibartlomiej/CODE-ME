wiersz = ('Wieprza znów skarciła Raba: Oby cię wypiła żaba!” Na to się odezwie Nida: Tobie samej też się przyda!” Biebrza na to rzecze grzecznie: Mówisz, rzeko, niedorzecznie”. Jak nie skoczy San na Biebrzę: Sama wciąż u Narwi żebrze, A dla innych - niełaskawa!” San, a głupi!” - rzekła Skawa. I tak trwały kłótnie długie Sanu z Sołą, Wieprza z Bugiem, Ledwie coś tam powie która, A już Nysa, a już Bzura, A już Odra czy Barycza Wszystkie wady jej wylicza. To się tak sprzykrzyło Wiśle, Że im rzekła po namyśle: Drogie rzeki, biorąc ściśle, Waszych słów naprawdę szkoda, Przecież to jest wszystko woda. Jednakowy los nas czeka, W morze wpadnie każda rzeka”. Gdy tak rzekła mądra Wisła, Cała zwada zaraz prysła."')

wiersz_z_malej_litery = wiersz.lower()

print(wiersz_z_malej_litery)

lista_wyrazów_malej_litery = wiersz_z_malej_litery.split()

print(lista_wyrazów_malej_litery)

print('Ilość wyrazów w tekście to: ', len(lista_wyrazów_malej_litery))

lista_wyr = list(lista_wyrazów_malej_litery)

lista_wyr.sort()

print(lista_wyr)

#lista_wyrazow = str(lista_wyr)

print(lista_wyr[:3], lista_wyr[-3:])