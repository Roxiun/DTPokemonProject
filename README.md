# DT Pokemon Project
[Website](https://dtpokemonproject.herokuapp.com/)

Can also be access through [pokemonproject.ga](https://pokemonproject.ga/)

[Original Project](https://github.com/MrMusovic/PokemonProject)

## What is this?
This is an example rewrite to [this](https://github.com/MrMusovic/PokemonProject) template. This one adds a simple `flask` backend.

It is currently in *extremely* early stages and as such doesn't have very good styling since it was solely meant to be a backend template.

## How to run
### Method 1 - Local Run (Reccommend for Beginners)
1. Install [Python](https://www.python.org/downloads/)
   
   **Note**: Follow [this](https://realpython.com/installing-python/#windows) if you are on windows
2. Clone this repo - `git clone https://github.com/Roxiun/DTProject.git`
3. cd into the directory - `cd DTProject/`
4. Install dependencies - `pip3 install -r requirments.txt`
5. Run the website - `flask run --host=0.0.0.0`

### Method 2 - Docker Run (Reccommened Way)
1. Install [Docker](https://www.docker.com/)
2. Clone this repo - `git clone https://github.com/Roxiun/DTProject.git`
3. cd into the directory - `cd DTProject/`
4. Build the image - `docker build . -t pokemon-project -f Dockerfile`
5. Run the container - `docker run -d -p 5000:5000 --rm pokemon-project:latest`

### Method 3 - Vagrant Run (Untested & Not Reccommened)
1. Instsall [Vagrant](https://www.vagrantup.com/)
2. Clone this repo - `git clone https://github.com/Roxiun/DTProject.git`
3. cd into the directory - `cd DTProject/`
4. `vagrant up`
5. `vagrant ssh`
6. Configure the server in `/vagrant` and then run `flask run --host=0.0.0.0`

## Project Structure
This project structure is based of [this](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars) tutorial. 

It has the following file system:

```bash
├── app
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── explore.html
│   │   ├── pokemon.html
│   │   ├── 404.html
│   │   └── 500.html
│   ├── static
│   │   ├── styles
│   │   │   └── mainpage.css
│   │   ├── favicon.ico
│   │   ├── PokemonLogo.png
│   │   ├── PokemonBall.png
│   │   └── 404.png
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   └── errors.py
├── app.py
├── config.py
├── .flaskenv
├── push.sh
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── Procfile
├── runtime.txt
├── Vagrantfile
├── boot.sh
├── README.md
├── LICENSE
└── .gitignore
```

Futher Information can be found [here](https://github.com/Roxiun/DTPokemonProject/wiki/Application-Structure)

## Contributing
Fork this repo and submit a pull request. If you are already a contributor just push using the push file.

## TODO
* Facelift (~~Bootstrap CSS~~ - Added! & Facelift in general)
* Stats for each pokemon
* ~~Host it for people to see~~ [Completed!](https://dtpokemonproject.herokuapp.com/)
* Favicon.ico - (Added just not currently functioning)

## Resources Used:
* [Flask Quickstart](https://flask.palletsprojects.com/en/0.12.x/quickstart/)
* [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars)
* [Dockerize a Flask App](https://dev.to/riverfount/dockerize-a-flask-app-17ag)

Made by Roxiun 2020
