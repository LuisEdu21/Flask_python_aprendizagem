from flask import Flask, render_template

class jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console
    


app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo_1 =jogo('Tetris', ' Puzzle', 'Atari')
    jogo_2 =jogo('God of war', 'Rack n Slash', 'PS2')
    jogo_3 =jogo('Need For Speed', 'corrida', 'PC')
    lista = [jogo_1,jogo_2,jogo_3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()