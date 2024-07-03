import requests
import random
import os
from datetime import datetime
import pickle
import json

def newOffers(list1, list2):
   diffs = [i for i in list1 + list2 if i not in list1]
   # diffs = [i for i in list1 + list2 if i not in list1 or i not in list2]
   return diffs
   
def oldOffers(list1, list2):
   diffs = [i for i in list1 + list2 if i not in list2]
   return diffs
   
def log(message):
	with open('enjoythefansale.log', 'a',encoding='utf-8') as f:
		f.write(f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')} - {message} \n")
		

def sendTelegram(message):
    apiToken = '<telegram_api_token>'
    chatID = '<telegram_chat_id>'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        # print(response.text)
    except Exception as e:
        print(e)

# https://www.ticketone.it/event/depeche-mode-stadio-san-siro-15946090/
# Il numero e' l'ID dell'evento.
#event = 'https://www.fansale.it/fansale/tickets/pop-amp-rock/depeche-mode/459359/15946090'
event = 'https://www.fansale.it/fansale/tickets/pop-amp-rock/depeche-mode/459359/15946075'
event_id = event.split("/")[-1]

if not os.path.exists('enjoythefansale.log'):
	with open('enjoythefansale.log', 'w') as f:
		pass
		

user_agents = [
	'Mozilla/5.0 (X11; CrOS x86_64 15359.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.134 Safari/537.36',
	'Mozilla/5.0 (X11; CrOS armv7l 15359.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.134 Safari/537.36',
	'Mozilla/5.0 (X11; CrOS aarch64 15359.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.134 Safari/537.36',
	'Mozilla/5.0 (X11; CrOS x86_64 15359.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.134 Safari/537.36',
	'Mozilla/5.0 (X11; CrOS armv7l 15359.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.134 Safari/537.36',
	'Mozilla/5.0 (X11; CrOS aarch64 15359.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.134 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13.3; rv:112.0) Gecko/20100101 Firefox/112.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Vivaldi/6.0.2979.15',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
	'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1',
	'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/112.0.5615.70 Mobile/15E148 Safari/604.1',
	'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/112.0 Mobile/15E148 Safari/605.1.15',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
	'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0',
	'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Vivaldi/6.0.2979.15',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Vivaldi/6.0.2979.15',
	'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 13; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 13; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 13; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 13; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 13; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 13; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36',
	'Mozilla/5.0 (Android 13; Mobile; rv:68.0) Gecko/68.0 Firefox/112.0',
	'Mozilla/5.0 (Android 13; Mobile; LG-M255; rv:112.0) Gecko/112.0 Firefox/112.0'
]

user_agent = random.choice(user_agents)

log(f"Oggi mi sento proprio un browser tipo {user_agent}")

headers = {
	'User-Agent': user_agent,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	'Accept-Language': 'it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate, br',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'none',
	'Sec-Fetch-User': '?1'
}

response = requests.get(event, headers=headers)

if (response.status_code  != 200):
	log(f"Errore nella prima chiamata verso Fansale: response.status_code != 200 {response.status_code}")
	raise Exception(f"Errore nella prima chiamata verso Fansale: response.status_code != 200 {response.status_code}")
	exit()

cookies = response.cookies

access_fansale = cookies["access.FANSALE"]

params = {
	'groupEventId': event_id,
	'maxResults': '2500',
	'dataMode': 'evdetails',
	'addPrerenderedList': 'false',
	'_': access_fansale
}

log(f"Il cookie access.FANSALE vale {access_fansale}")

response = requests.get('https://www.fansale.it/fansale/json/offer', headers=headers, params=params, cookies=cookies)
json_data = response.json()

if (response.status_code  != 200):
	log(f"Errore nella seconda chiamata verso Fansale: response.status_code != 200 {response.status_code}")
	raise Exception(f"Errore nella seconda chiamata verso Fansale: response.status_code != 200 {response.status_code}")
	exit()

log(f"Quante offerte al mondo vuoi analizzare? {len(json_data['offers'])}")

if not os.path.exists('offers.dump'):
	with open('offers.dump', 'wb') as f:
		pickle.dump(json_data['offers'], f)
else:
	with open('offers.dump', 'rb') as f:
		offers = pickle.load(f)
	new_offers = newOffers(offers, json_data['offers'])
	old_offers = oldOffers(offers, json_data['offers'])
	for new_offer in new_offers:
		print(f"Nuova offerta per {new_offer['evdetailsSeatDescriptionHtml']} a EUR {new_offer['minPurchasablePriceWithBuyerCommission']}: https://www.fansale.it{new_offer['initialOfferUrl']}")
		log(f"Nuova offerta per {new_offer['evdetailsSeatDescriptionHtml']} a EUR {new_offer['minPurchasablePriceWithBuyerCommission']}: https://www.fansale.it{new_offer['initialOfferUrl']}")
		sendTelegram(f"\u26A0\uFE0F Nuova offerta per i Depeche Mode! \u26A0\uFE0F {new_offer['evdetailsSeatDescriptionHtml']} a EUR {new_offer['minPurchasablePriceWithBuyerCommission']}: https://www.fansale.it{new_offer['initialOfferUrl']}")
	for old_offer in old_offers:
		print(f"Offerta non più disponibile per {old_offer['evdetailsSeatDescriptionHtml']} a EUR {old_offer['minPurchasablePriceWithBuyerCommission']}: https://www.fansale.it{old_offer['initialOfferUrl']}")
		log(f"Offerta non più disponibile per {old_offer['evdetailsSeatDescriptionHtml']} a EUR {old_offer['minPurchasablePriceWithBuyerCommission']}: https://www.fansale.it{old_offer['initialOfferUrl']}")
		sendTelegram(f"\u26D4\uFE0F Offerta non più disponibile per i Depeche Mode! \u26D4\uFE0F {old_offer['evdetailsSeatDescriptionHtml']} a EUR {old_offer['minPurchasablePriceWithBuyerCommission']}: https://www.fansale.it{old_offer['initialOfferUrl']}")
	with open('offers.dump', 'wb') as f:
		pickle.dump(json_data['offers'], f)	

exit()
