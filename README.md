# sew5-language-service-bbulis
#### Benjamin Bulis
## Beschreibung
Client und Server sollen entwickelt werden, um nur anhand von Wörtern eine Sprache zu erkennen.

### Client
* Schickt eine Anfrage an den Server
* Rückgabe des Servers wird im Ausgabefeld angezeigt

### Server
* Startet einen Server, welcher auf eine Anfrage am Endpoint `/lg` wartet
* Als parameter `id` wird der Text mitgegeben, welcher erkannt werden soll
* Server ist am Port 5000 aufrufbar
* Überprüfung aller Parameter, welche dem Server mitgegeben werden
* Rückgabe eines JSON-Objektes
    * reliable (boolean) - Ist die erkennung zuverlässig
    * language (string) - Erkannte Sprache (voller Name)
    * short (string) - Name der Sprache in kurzer Schreibweise
    * prob (float) - Zuverlässigkeit der Erkenntung in Prozent

#### JSON Rückgabe Beispiel (implementierte Version)(erfolgreiche erkennung)
```json
{
  "success": true,
  "result": {
    "reliable": true,
    "language": "German",
    "short": "de",
    "prob": 100.00
  }
}
```
#### JSON Rückgabe Beispiel (implementierte Version)(error handling)
Kein Parameter angegeben, welcher zu erkennen ist
(Parameter `id` ist nicht vorhanden)
```json
{
  "success": false,
  "error": "no parameter id given"
}
```
Kein Text angegeben, welcher zu erkennen ist
(Parameter `id` ist vorhanden aber kein Text angefügt)
```json
{
  "success": false,
  "error": "no text given"
}
```