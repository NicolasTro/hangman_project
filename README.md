Python - Ahorcado

```text
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
         =========
```

Juego del ahorcado basado en consola. 
El jugador adivinará letras de una palabra oculta
(como un título de película) dentro de un número 
limitado de intentos incorrectos. 

Las palabras se cargarán aleatoriamente desde un archivo de texto simple.

## Estructura del proyecto

```text
hangman_project/
│
├── main.py             # Bucle del juego
├── game.py             # Clase HangmanGame (lógica del juego)
├── player.py           # Clase Player (datos y validación del jugador)
├── ranking.py          # Clase Ranking (gestión del top de jugadores)
├── utils.py            # Funciones auxiliares 
├── wordlist.txt        # Lista de frases (una por línea)
├── ranking.txt         # Archivo de texto para guardar el ranking
└── README.md           # Instrucciones y descripción del juego
```

## Cómo ejecutar

Desde la terminal, situarse en el directorio del proyecto y ejecutar:

```bash
python main.py
```
