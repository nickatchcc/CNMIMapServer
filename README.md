# CNMIMapServer
Small web application to create choropleth maps of the CNMI serverside.

# Installation
1) Git clone to a local directory from cmd.exe (e.g. 'C:\Users\username> git clone https://github.com/nickatchcc/CNMIMapServer.git')
2) cd to the directory (e.g. 'C:\Users\username> cd CNMIMapServer')
3) Install dependencies with pip (e.g. 'C:\Users\username> pip install -r requirements.txt')

# Usage
When the CNMIMapServer.py file is running on the server, http connections will be accepted on port 14515, and JSON encoded excel tables can be used to visualize data by submitting a request from your browser using the following URL format:

http://localhost:14515/api/cnmi_map?json=JSON_STRING_GOES_HERE

# Data preparation
Converting a .csv file to a .json string can be done easily at the following URL:
https://csvjson.com/csv2json

Note: it can also be done locally via the following commands in a python console:
import pandas as pd
df = pd.read_csv(r'\File_Location\input.csv')
df.to_json(r'\Output_File_Location\output.json')

# Demo:
Once the application is running on the local machine, you can follow this URL

http://localhost:5000/api/cnmi_map?json=[%20{%20%22NAMELSAD%22:%20%22Achugao%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Afatung%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Afetnas%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Agatasi%20(Payapai)%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Agingan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Agrihan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Aguijan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Agusan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Alaguan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Alamagan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22American%20Memorial%20Park%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Anatahan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Annex%20F%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Apanon%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Akina%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Akoddo%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Dudo%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Falipe%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Gonna%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Lito%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Mahetog%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Matuis%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Niebes%20(Nieves)%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Palacios%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Perdido%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Rabagau%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Teo%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22As%20Terlaje%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Asuncion%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Banaderu%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Bird%20Island%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Capitol%20Hill%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Carolinas%20Heights%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Carolinas%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Chacha%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Chalan%20Galaide%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Chalan%20Kanoa%20I%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Chalan%20Kanoa%20II%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Chalan%20Kanoa%20III%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Chalan%20Kanoa%20IV%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Chalan%20Kiya%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Chalan%20Laulau%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Chalan%20Piao%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Chalan%20Rueda%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22China%20Town%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Dagu%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Dandan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Duge%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Eastern%20Tinian%20(Marpo%20Valley)%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Fananganan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Fanlagon%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Fanonchuluyan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Farallon%20de%20Medinilla%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Finasisu%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Finata%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Forbidden%20Island%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Gagani%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Gampapa%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Gaonan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Garapan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Gayaugan%20(Kaan)%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Ginalangan%20(Chudan)%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Gualo%20Rai%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Guguan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Hilaihai%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22I%20Akgak%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22I%20Chenchon%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22I%20Denni%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22I%20Fadang%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22I%20Koridot%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22I%20Liyang%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22I%20Maddok%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22I%20Naftan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22I%20Pitot%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Kagman%20I%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Kagman%20II%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Kagman%20III%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Kagman%20IV%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Kagman%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Kalabera%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Kannat%20Tabla%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Koblerville%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Laulau%20Bay%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Lempanai%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Liyu%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Lower%20Base%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Makmak%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Managaha%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Mananana%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Marpi%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Marpo%20Heights%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Matansa%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Matpo%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Maturana%20Hill%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Maug%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Mochong%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Mount%20Sabana%20(Minachage)%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Mount%20Taipingot%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Nanasu%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Navy%20Hill%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Northern%20Tinian%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Opyan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Pagan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Papago%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Pekngasu%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Pidos%20Kahalo%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Puerto%20Rico%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Sabaneta%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Sadog%20Tasi%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Sailigai%20Papa%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22San%20Antonio%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22San%20Jose%20(Oleai)%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22San%20Jose%20(Tinian%20Municipality)%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22San%20Roque%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22San%20Vicente%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Sarigan%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Sayan%20Gigani%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Sinapalo%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Songsong%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Susupe%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Tagolo%20Ogso%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Taimama%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Talafofo%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Talakhaya%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Talo%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Tanapag%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Tangke%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Tapochao%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Tatachok%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Tatgua%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Tenetu%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Tottotville%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Ugis%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Uracus%20(Farallon%20de%20Pajaros)%20village%22,%20%22Value%22:%200.01%20},%20{%20%22NAMELSAD%22:%20%22Western%20Tinian%20village%22,%20%22Value%22:%200.01%20}%20]
