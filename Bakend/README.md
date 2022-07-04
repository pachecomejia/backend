# unidad2
pip install fastapi
pip install uvicorn
uvicorn main:app --reload
sqlite3 clientes.sqlite < clientes.sql
git push -u origin main

 git push -u origin main
 rm -rf .git
 ###########################
#hacere una imagen
 docker build -t bakend:v1 . 
 docker run -it -v /workspace/backend/Bakend/code:/home/code --net=host --name reymon -h pacheco  bakend:v1