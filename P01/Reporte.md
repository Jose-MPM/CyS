# Práctica 1-OSINT

Azpeitia García Karyme Ivette

Pedro Méndez Jose Manuel 

### 2.1 Información personal


| ![](img/foto.png)
|:----------------------:|
| Imagen sobre la que trabajamos utilizando la herramienta: _Exif.tools_.

----

1. ¿Cuál es el nombre real del archivo? Es decir, el nombre que se le dió por el sistema operativo.

 `File name: phpCjd4Yf`

2. ¿Qué marca es la cámara con la que fue tomada la foto?
```
Make:	Sony
Camera Model Name:	H8216
```

De acuerdo a la información anterior la foto fue tomada por un celular `Sony Xperia XZ2(H8216)`

3. ¿De qué color son las carpas del restaurante latino a unas calles?

El restaurante latino ubicado a unas calles de nombre `Las Iguanas - London - Royal Festival Hall`  tiene carpas color azul cielo y rojas.


### 2.2 Información técnica de un sistema

Sitio web: [Personal website ](https://jpyamamoto.com).

Sitio web investigado: [Game's website](https://www.friv.com).

Para conseguir información de la pagina web será necesario conocer la `dirección IP` de esta.

#### Obteniendo la dirección IP del website 

```terminal
~ %  nslookup https://www.friv.com  

Server:		
Address:	

Non-authoritative answer:
Name:	https://www.friv.com
Address: 207.244.69.244
```

Utilizando los siguientes sitios, recabamos la siguiente información:
* [Whois.domaintools](https://whois.domaintools.com/207.244.69.244): La localización de la dirección IP del servidor: United States United States Washington Mass Division Of Employment Training, pero no encontramos mucha información relevante.

* [Geo Data Tool](https://www.geodatatool.com/en/?ip=207.244.69.244)

| ![](img/GeoData.png)
|:----------------------:|
| Información obtenida usando Geo Data Tool.

* [Who.is](https://who.is/whois/friv.com): Aquí pudimos encontrar varias direcciones ip y saber que están trabajando con google. En este caso decidimos investigar más con:

> www.friv.com - A -  498   -  207.244.86.26

##### Información obtenida
```

Hostname: 207.244.69.244
IP Address: 207.244.69.244

Registrant Contact Information:

NameRedacted for Privacy
OrganizationPrivacy service provided by Withheld for Privacy ehf
Country:   United States
Country Code: US ()
Region: North Carolina
City: Fuquay-Varina
Postal Code: 27526
Latitude: 35.584320
Longitude: -78.800010
AddressKalkofnsvegur 2
CityReykjavik
State / ProvinceCapital Region
Postal Code101
CountryIS
Phone+354.4212434




Administrative Contact Information:

NameRedacted for Privacy
OrganizationPrivacy service provided by Withheld for Privacy ehf
AddressKalkofnsvegur 2
CityReykjavik
State / ProvinceCapital Region
Postal Code101
CountryIS
Phone+354.4212434

Technical Contact Information:

NameRedacted for Privacy
OrganizationPrivacy service provided by Withheld for Privacy ehf
AddressKalkofnsvegur 2
CityReykjavik
State / ProvinceCapital Region
Postal Code101
CountryIS
Phone+354.4212434
```
### Información práctica de un sistema