import requests
import baza
import data

def new_zakaz(body):
    return requests.post(baza.URL + baza.CREAT_ZAKAZ,  # подставляем полный url
                         json=body,
                         headers=data.headers)
    proverka_cod = new_zakaz()
    assert proverka_cod.status_code == 200
response = new_zakaz(data.zakaz);
track = str(response.json()["track"])
print(response.status_code)
print(response.json())
print(track)


def zakaz_po_nomeru():
    return requests.get(baza.URL + baza.ZAPROS_ZAKAZ + track,
                        headers=data.headers)
response = zakaz_po_nomeru();
print(response.json())
