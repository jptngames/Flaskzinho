from flask import Flask, jsonify
from random import choice
from unidecode import unidecode

app = Flask(__name__)

piadas_lista = [
    "Por que o livro de matemática se suicidou? Porque tinha muitos problemas.",
    "O que o pato disse para a pata? Vem quá!",
    "Qual é o cúmulo da paciência? Esperar o ônibus na internet.",
    "Por que o jacaré tirou o filho da escola? Porque ele réptil de ano.",
    "O que o tomate foi fazer no banco? Tirar extrato.",
    "Como o elétron atende o telefone? Próton!",
    "O que o zero disse para o oito? Que cinto maneiro!",
    "Por que a aranha é o animal mais carente? Porque ela é um aracneedy.",
    "Qual é o peixe mais inteligente? O atum.",
    "Por que o computador foi preso? Porque ele executou um programa.",
    "O que o chão falou para a mesa? Tampo tudo.",
    "Por que o músico foi preso? Porque ele estava em uma nota errada.",
    "O que o tijolo falou para o outro? Há um ciumento entre nós.",
    "Por que o relógio foi para a escola? Para aprender a marcar o tempo.",
    "O que o fotógrafo foi fazer na prisão? Revelar os negativos.",
    "Por que o lápis não pode ir à escola? Porque ele está sem ponta.",
    "O que o papel disse para o lápis? Estou em branco.",
    "Por que a bicicleta não pode ficar em pé sozinha? Porque ela está sem pedal.",
    "O que o elevador disse para a escada? Suba de nível.",
    "Por que o cachorro não gosta de celular? Porque ele prefere latir."
]

@app.route('/')
def piadas():
    data = {"piada": unidecode(choice(piadas_lista)), "copyright": "github.com/RexxLab"}
    return jsonify(data)

if __name__ == "__main__":
    app.run()