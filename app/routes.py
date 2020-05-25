import os
import random
import pypokedex

from flask import render_template, redirect, request, url_for, send_from_directory
from app import app
from app.forms import PokemonSearch


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/search', methods = ['POST'])
def searchs():
    edata = request.form['edata']
    if edata.isnumeric():
        return redirect(url_for(f'pokemon', dex_number=edata))
    else:
        pdata = pypokedex.get(name=str(edata))
        return redirect(url_for(f'pokemon', dex_number=pdata.dex))

@app.route('/explore')
def explore():
    pd = {}
    for i in range(5):
        pokemon = pypokedex.get(dex=int(random.randint(1, 807)))
        name = pokemon.name.title()
        types = pokemon.types

        leng = len(str(pokemon.dex))
        pd[name] = {"Name":name, "Types":types, "Leng":leng, "Dex":pokemon.dex}
    print(pd)
    return render_template('explore.html', random_pokemon_dict=pd)

@app.route('/pokemon/<dex_number>')
def pokemon(dex_number):
    try:
        pokemon = pypokedex.get(dex=int(dex_number))
    except pypokedex.exceptions.PyPokedexHTTPError:
        return 'No Pokemon Found :('

    name = pokemon.name.title()
    types = pokemon.types

    leng = len(str(dex_number))

    return render_template('pokemon.html', title=name, dex_number=dex_number, name=name, types=types, leng=leng)
