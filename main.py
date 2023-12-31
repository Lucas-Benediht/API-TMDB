from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os
import random
import json

load_dotenv()
app = Flask(__name__)

API_KEY = '587ef6e3e3ac5df239394eeca31ef572'
idioma = 'pt-BR'

@app.route('/')
def site():
    #parte de tendências da semana
    tendencias_url = f'https://api.themoviedb.org/3/trending/all/week?api_key={API_KEY}&language={idioma}'
    response_tendencias = requests.get(tendencias_url)

    
    genero_acao = 28  # ID de ação
    acao_url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genero_acao}&language={idioma}'
    response_acao = requests.get(acao_url)
    
    genero_desenhos = 16  #ID de desenhos
    desenhos_url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genero_desenhos}&language={idioma}'
    response_desenhos = requests.get(desenhos_url)
    
    random_page = random.randint(1,10) #Pega uma imagem aleatória na capa
    random_filme_url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&page={random_page}&language={idioma}'
    response_random_filme = requests.get(random_filme_url)

    if (
        response_tendencias.status_code == 200 
        and response_acao.status_code == 200 
        and response_desenhos.status_code == 200 
        and response_random_filme.status_code == 200
        ):
        
        data_tendencias = response_tendencias.json()
        data_acao = response_acao.json()
        data_desenhos = response_desenhos.json()
        data_random_filme = response_random_filme.json()
        
        resultados_random_filme = response_random_filme.json()['results']
        filme_aleatorio = random.choice(resultados_random_filme)
        
        return render_template(
            'index.html', tendencias=data_tendencias['results'],
            filmes_acao=data_acao['results'],
            filmes_desenhos=data_desenhos['results'],
            filme_aleatorio=filme_aleatorio,
        )
    else:
        return 'Erro ao obter dados da API TMDb'
    

@app.route('/filmes')
def filmes():
    return render_template('filmes.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/series')
def series():
    return render_template('series.html')


if __name__ == '__main__':
    app.run(debug=True)
