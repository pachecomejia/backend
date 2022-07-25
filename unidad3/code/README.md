docker ps -a
docker start b626dd5c8855 -i
docker start 45ee96cfdd19 -i bakend
uvicorn main:app --reload
 python3 -m http.server 8080
 cd autentificacion
 cd code