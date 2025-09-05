docker build -t flask-hello-world .

docker run -p 8080:5000 flask-hello-world

exo 6 : 

docker compose -f "Tp Docker/docker-compose.yml" up -d --build