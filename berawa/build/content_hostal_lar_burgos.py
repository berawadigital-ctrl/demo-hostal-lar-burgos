# Contenido de la demo Hostal Lar (Burgos) (es/en/fr/de). Hechos de hostallar.es leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones de clientes.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Individual y triple','Dobles'],'en':['Single and triple','Doubles'],'fr':['Individuelle et triple','Doubles'],'de':['Einzel- und Dreibettzimmer','Doppelzimmer']}
RD={
'es':['Individual de 9 m² con 1 cama y triple de 9 m² con 3 camas individuales. Baño privado con ducha, TV, calefacción y artículos de aseo.','Doble con 2 camas (13 m², vistas a la ciudad) y doble con cama doble (10 m², accesible en silla de ruedas). Baño privado, TV y secador.'],
'en':['Single of 9 m² with 1 bed and triple of 9 m² with 3 single beds. Private bathroom with shower, TV, heating and toiletries.','Double with 2 beds (13 m², city views) and double with a double bed (10 m², wheelchair accessible). Private bathroom, TV and hairdryer.'],
'fr':['Individuelle de 9 m² avec 1 lit et triple de 9 m² avec 3 lits simples. Salle de bain privée avec douche, TV, chauffage et articles de toilette.','Double avec 2 lits (13 m², vue sur la ville) et double avec lit double (10 m², accessible en fauteuil roulant). Salle de bain privée, TV et sèche-cheveux.'],
'de':['Einzelzimmer mit 9 m² und 1 Bett, Dreibettzimmer mit 9 m² und 3 Einzelbetten. Eigenes Bad mit Dusche, TV, Heizung und Pflegeartikeln.','Doppelzimmer mit 2 Betten (13 m², Stadtblick) und Doppelzimmer mit Doppelbett (10 m², rollstuhlgerecht). Eigenes Bad, TV und Föhn.']}
ART={
'hero':('skyline',9701,['#1c2f4a','#d99a5b','#efc48f','#5a2f3c','#47242f','#2b151c']),
'intro':('arches',9702,['#eeece6','#e2b07a','#7a3b2c','#1c2f4a','#0f1a2a']),
'r1':('columns',9711,['#efebe3','#f7f3ec','#8a4a2f','#5a2f1c','#331a10']),
'r2':('hills',9712,['#e9ede6','#efe5cf','#e0ab6c','#9fb09a','#6d8670','#475e4c']),
'g1':('waves',9721,['#1c2f4a','#e7b47c','#f4d9b0','#36506f','#25395a','#15233a']),
'g2':('skyline',9722,['#26324a','#e0a064','#f2cf9c','#6e3a45','#5a2f39','#3a1d24']),
'g3':('arches',9723,['#ecdfca','#dcab76','#7a3b2c','#1c2f4a','#0f1a2a']),
'g4':('columns',9724,['#edeae2','#f7f4ee','#8a4a2f','#5a2f1c','#331a10'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hostal Lar · Hostal en el centro histórico de Burgos',see_rooms='Ver las habitaciones',hero_k='Burgos · Centro histórico',hero_t='En Burgos, como en tu propia casa',hero_s='Un hostal acogedor en pleno centro histórico, a escasos metros del Camino de Santiago.',
 intro_t='Tu lugar para disfrutar de Burgos',intro_p1='Junto a la Iglesia de San Lesmes, en una zona llena de lugares de ocio, cultura y esparcimiento. En unos minutos andando llegas a la Catedral y al Museo de la Evolución Humana.',
 intro_p2='Habitaciones con baño privado, WiFi gratuito y vistas a la ciudad. Mostrador de información turística y consigna de equipaje gratuita.',
 stats=['4 tipos de habitación','Baño privado','WiFi gratuito','Ascensor'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Individual, doble con 2 camas, doble con cama doble y triple.',
 svcs=['WiFi gratuito','Ascensor','Calefacción','Habitación accesible','Información turística','Consigna de equipaje gratuita'],
 around_s='A 800 m de la Catedral, a 300 m del Museo de la Evolución Humana y a 20 m del Camino de Santiago.',
 loc_p='Cardenal Benlloch 1 · 09004 Burgos, en pleno centro histórico. Recepción de 09:00 a 23:30.',
 chips=['¿Qué habitaciones tenéis?','¿Cuánto cuesta una noche?','¿Dónde está el hostal?','¿Cómo reservo?']),
'en':dict(title='Hostal Lar · Hostel in the historic centre of Burgos',see_rooms='See the rooms',hero_k='Burgos · Historic centre',hero_t='In Burgos, as in your own home',hero_s='A cosy hostel in the historic centre, just a few metres from the Camino de Santiago.',
 intro_t='Your place to enjoy Burgos',intro_p1='Next to the Church of San Lesmes, in an area full of leisure and culture. A few minutes on foot take you to the Cathedral and the Museum of Human Evolution.',
 intro_p2='Rooms with private bathroom, free WiFi and city views. Tourist information desk and free luggage storage.',
 stats=['4 room types','Private bathroom','Free WiFi','Lift'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Single, double with 2 beds, double with a double bed and triple.',
 svcs=['Free WiFi','Lift','Heating','Accessible room','Tourist information','Free luggage storage'],
 around_s='800 m from the Cathedral, 300 m from the Museum of Human Evolution and 20 m from the Camino de Santiago.',
 loc_p='Cardenal Benlloch 1 · 09004 Burgos, in the historic centre. Reception from 09:00 to 23:30.',
 chips=['Which rooms do you have?','How much is a night?','Where is the hostel?','How do I book?']),
'fr':dict(title='Hostal Lar · Hostal dans le centre historique de Burgos',see_rooms='Voir les chambres',hero_k='Burgos · Centre historique',hero_t='À Burgos, comme chez vous',hero_s='Un hostal accueillant en plein centre historique, à quelques mètres du Chemin de Saint-Jacques.',
 intro_t='Votre point de départ pour Burgos',intro_p1="À côté de l'église San Lesmes, dans un quartier plein de loisirs et de culture. À quelques minutes à pied de la cathédrale et du Musée de l'Évolution humaine.",
 intro_p2="Chambres avec salle de bain privée, WiFi gratuit et vue sur la ville. Comptoir d'information touristique et consigne à bagages gratuite.",
 stats=['4 types de chambre','Salle de bain privée','WiFi gratuit','Ascenseur'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Individuelle, double à 2 lits, double avec lit double et triple.',
 svcs=['WiFi gratuit','Ascenseur','Chauffage','Chambre accessible','Information touristique','Consigne à bagages gratuite'],
 around_s="À 800 m de la cathédrale, à 300 m du Musée de l'Évolution humaine et à 20 m du Chemin de Saint-Jacques.",
 loc_p='Cardenal Benlloch 1 · 09004 Burgos, en plein centre historique. Réception de 09:00 à 23:30.',
 chips=['Quelles chambres avez-vous ?','Combien coûte une nuit ?',"Où se trouve l'hostal ?",'Comment réserver ?']),
'de':dict(title='Hostal Lar · Hostal in der Altstadt von Burgos',see_rooms='Zimmer ansehen',hero_k='Burgos · Altstadt',hero_t='In Burgos wie zu Hause',hero_s='Ein gemütliches Hostal mitten in der Altstadt, nur wenige Meter vom Jakobsweg.',
 intro_t='Ihr Ort, um Burgos zu genießen',intro_p1='Neben der Kirche San Lesmes, in einem Viertel voller Freizeit und Kultur. In wenigen Gehminuten erreichen Sie die Kathedrale und das Museum der menschlichen Evolution.',
 intro_p2='Zimmer mit eigenem Bad, kostenlosem WLAN und Stadtblick. Touristeninformation und kostenlose Gepäckaufbewahrung.',
 stats=['4 Zimmertypen','Eigenes Bad','Kostenloses WLAN','Aufzug'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Einzelzimmer, Doppelzimmer mit 2 Betten, Doppelzimmer mit Doppelbett und Dreibettzimmer.',
 svcs=['Kostenloses WLAN','Aufzug','Heizung','Barrierefreies Zimmer','Touristeninformation','Kostenlose Gepäckaufbewahrung'],
 around_s='800 m von der Kathedrale, 300 m vom Museum der menschlichen Evolution und 20 m vom Jakobsweg.',
 loc_p='Cardenal Benlloch 1 · 09004 Burgos, mitten in der Altstadt. Rezeption von 09:00 bis 23:30 Uhr.',
 chips=['Welche Zimmer gibt es?','Was kostet eine Übernachtung?','Wo liegt das Hostal?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://booking.avirato.com/?code=44423949'
BOOK=dict(mode='engine',url={l:RB+'&lang='+l for l in ('es','en','fr','de')})
D=dict(name='Hostal Lar',ac='#1c2f4a',ac2='#8a4a2f',ac2_a11y='#7a3b2c',book=BOOK,around=['Catedral de Burgos','Museo de la Evolución Humana'],foot=FOOT,
 address='Cardenal Benlloch 1 · 09004 Burgos',phones=['947 209 655'],emails=['reservas@hostallar.es'],maps='Hostal Lar, Cardenal Benlloch 1, 09004 Burgos',t=T)
META=dict(repo='demo-hostal-lar-burgos',name='Hostal Lar',legal_name='Hostal Lar (titular persona física, autónomo, según el aviso legal de su web)',registry_ids=['NIF de persona física publicado en el aviso legal de su web (no se copia en la demo)'],
 url='https://www.hostallar.es/',domain='hostallar.es',municipality='Burgos',province='Burgos',sector='hostal familiar con cuatro tipos de habitación en el centro histórico de Burgos',
 read_at='2026-10-30T07:33:40+01:00',created_at='2026-10-30T07:33:00+01:00',built_at='2026-10-30T07:45:00+01:00',audit_date='2026-10-30T06:52:00+01:00',
 rating=dict(value=4.4,coincide=['telefono','web'],date='2026-10-29T12:45:00+01:00',url='https://www.google.com/maps/place/Hostal+Lar/@42.3422134,-3.6963633,17z/data=!4m9!3m8!1s0xd45fcd0e6e55ca1:0x777013137f358780!5m2!4m1!1i2!8m2!3d42.3422134!4d-3.6963633!16s%2Fg%2F1tg_ydf0'),
 book=dict(mode='engine',url=RB,note='motor de reservas real de su web (Avirato, webcode 44423949 del calendario de hostallar.es), HTTP 200 comprobado el 30/10/2026 en es/en/fr/de.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Cuánto cuesta una noche?','K02'),('¿A qué hora abre la recepción?','K03'),('¿Hay wifi?','K04'),('¿Es accesible en silla de ruedas?','K05'),('¿Puedo dejar las maletas?','K06'),('¿Estáis en el Camino de Santiago?','K07'),('¿Dónde está el hostal?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Hay restaurante?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('How much is a night?','K02'),('What are the reception hours?','K03'),('Is there wifi?','K04'),('Is it wheelchair accessible?','K05'),('Can I leave my luggage?','K06'),('Are you on the Camino de Santiago?','K07'),('Where is the hostel?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('Is there a restaurant?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Combien coûte une nuit ?','K02'),('Quels sont les horaires de la réception ?','K03'),('Y a-t-il le wifi ?','K04'),('Est-ce accessible en fauteuil roulant ?','K05'),('Puis-je laisser mes bagages ?','K06'),('Êtes-vous sur le Chemin de Saint-Jacques ?','K07'),("Où se trouve l'hostal ?",'K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Y a-t-il un restaurant ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was kostet eine Übernachtung?','K02'),('Wann ist die Rezeption geöffnet?','K03'),('Gibt es WLAN?','K04'),('Ist es rollstuhlgerecht?','K05'),('Kann ich mein Gepäck abgeben?','K06'),('Liegen Sie am Jakobsweg?','K07'),('Wo liegt das Hostal?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Gibt es ein Restaurant?',None),('Haben Sie ein Schwimmbad?',None)]}
