# Anforderungen
### How to start
- you can start the interface by exécuting
```bash
python userInterface.py
```
or
```bash
python3 userInterface.py
```
depending off your version

- After you can use a user identification in passwords.text to log in

## info
1.__Login__ :
 
- ein IU wo der Nutzer sich einloggen kann
- ein Dialog, wo der Nutzer den Passwort verändern kann
- counter(fuer die Zeit Verwaltung) muss définiert werden, der sich nach jedem abmeldung incrementiert.

2.__Einkaufer_Interface__:
- Logout Button
- Informationen über den Nutzer,der sich angemeldet hast(Name und Budget(aktuel)) 
- soll 5 **Seiten** haben:
    - Warenkorb: 
        - alle ausgewählte Traktoren müssen sich drin finden
        - ein PushButton, um zu bezahlen
        - Budget von einkäufer,denen von Klaus und mängen muss Aktualisiert werden.
    - Home (TraktorenVerkauf):
        - Filter(vereinfach die Suche von Traktoren)
        - list von Traktoren und Infomationnen darüber
        - zoom möglichkeit auf Traktoren Image
        - list von Zubehör
        - Möglichkeit Traktoren und Zubehören auszuwählen und in warenkorb zu schicken
    - Klausnezt: 
        - werden die Leuten von Klaus netwerk hier angezeigt
        - and their Budget
    - Traktoren_voehanden:
        - jeder Nutzer kann sein vorhandenen Traktoren sehen
        - Möglichkeit zu verkaufen
    - Verkauf 
        - die Traktor/en, die der Nutzer verkaufen will, sind/ist hier angezeigt 
        - die Leuten die dafür interessiert sind, sind hier angezeigt mit Angeboten.
        - nach dem Verkauf muss die Daten(budget von dem Kaufer, verkaufer, Klaus und mänge) Aktualisiert werden.

3.__Klaus_Interface__:
- Logout Button
- Informationen über Klaus(Name und Budget(aktuel)) 
- soll 3 **Seiten** haben:
    - Traktoren :
        - werden Traktoren angezeigt (65% von den Verkaufpreis)
        - auswählen und in Warenkorb schicken
    - Zubehör :
        - werden Zubehör angezeigt (65% von den Verkaufpreis)
        - auswählen und in Warenkorb schicken
    - Warenkorb: 
        - alle ausgewählte Traktoren müssen sich drin finden
        - ein PushButton, um zu bezahlen
        - Budget von Klaus und Mägen von Traktoren und/oder Zubehör muss Aktualisiert werden
