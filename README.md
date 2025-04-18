# REST API zawierający regułę decyzyjną

Projekt - aplikacja Flask z czterema endpointami

# Endpointy
- `/` – strona główna
- `/mojastrona` – zwykła podstrona
- `/hello?name=TwojeImie` – przyjmuje parametr `name`
- `/api/v1.0/predict?num1=3&num2=4` – jeśli suma > 5.8, zwraca 1, inaczej 0

## Jak uruchomić:
1. Zainstaluj zależności:
    
pip install -r requirements.txt

2. Uruchom aplikację:
    
python app.py

3. Otwórz przeglądarkę i przetestuj podstrony:

- Strona główna: http://127.0.0.1:5000/
- Moja strona: http://127.0.0.1:5000/mojastrona
- Hello: http://127.0.0.1:5000/hello?name=TwojeImie
- Predykcja: http://127.0.0.1:5000/api/v1.0/predict?num1=3&num2=4
