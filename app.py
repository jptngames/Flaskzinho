from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
]

@app.route('/', methods=['GET'])
def home():
	data = {"/livros":"retorna todos os livros da api (GET)", "/livros/id":"retorna um livro por id (GET)", "/livros": "Edita um livro (PUT)", "/livros":"Cria um livro (POST)","/livros/id": "Apaga um livro específico pelo id(DELETE)"}
	return jsonify(data)

# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
	return jsonify(livros)

# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
	for livro in livros:
		if livro.get('id') == id:
			return jsonify(livro)
			
# Editar
@app.route('/livros/<int:id>', methods = ['PUT'])
def editar_livro_por_id(id):
	livro_alterado = request.get_json()
	for indice, livro in enumerate(livros):
		if livro.get('id') == id:
			livros[indice].update(livro_alterado)
			return jsonify(livros[indice])
	
# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
	novo_livro = request.get_json()
	livros.append(novo_livro)
	return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
	for indice, livro in enumerate(livros):
		if livro.get('id') == id:
			del livros[indice]
	return jsonify(livros)
	
app.run(host='localhost', port=5000)