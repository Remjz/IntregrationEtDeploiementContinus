fichiers d'origine : 
 time docker build -t test .
temps build :  
real    0m47.936s
user    0m0.335s
sys     0m0.180s

docker images 
taille : 
test                latest    48cd6fd66363   2 minutes ago   1.2GB

optimisations : 

- on n'expose que le port 3000 et pas les 2 autres.
- on change le from pour le passer en "alpine", qui est optimisez, ce qui permet de résuire la taille.
- on change la ligne : RUN apt-get update && apt-get install -y build-essential ca-certificates locales && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

Car après le changement en alpine elle provoque une erreur.

nouvelle ligne : RUN apk update && apk add --no-cache build-base ca-certificates libc6-compat

- on récupère que les dépendenses avant le npm install et après on copie tout.
- on sépare le runner et le builder pour gagner du temps et de la place (en récupérant que les fichiers utiles pour le runner).
- Pour plus de sécurité on utilise un user et pas root.
-création d'un dockerignore

fichiers d'origine : 
 docker build --no-cache -t test2 .
temps build :  
Building 4.5s (15/15) FINISHED 

taille : 
test2               latest    2b8ac9317f6d   6 seconds ago   179MB

Conclusion : 

images | temps | taille

test      48s      1.2GB
test2     4.5s     179MB