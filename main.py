from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv('API_KEY')
idioma = 'pt-BR'

@app.route('/')
def site():
   
    tendencias_url = f'https://api.themoviedb.org/3/trending/all/week?api_key={API_KEY}&language={idioma}'
    response_tendencias = requests.get(tendencias_url)

    
    genero_acao = 28  # ID de ação
    acao_url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genero_acao}&language={idioma}'
    response_acao = requests.get(acao_url)
    
    genero_desenhos = 16  #ID de desenhos
    desenhos_url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genero_desenhos}&language={idioma}'
    response_desenhos = requests.get(desenhos_url)

    if response_tendencias.status_code == 200 and response_acao.status_code == 200 and response_desenhos.status_code == 200:
        data_tendencias = response_tendencias.json()
        data_acao = response_acao.json()
        data_desenhos = response_desenhos.json()
        return render_template('index.html', tendencias=data_tendencias['results'], filmes_acao=data_acao['results'], filmes_desenhos=data_desenhos['results'])
    else:
        return 'Erro ao obter dados da API TMDb'


if __name__ == '__main__':
    app.run(debug=True)