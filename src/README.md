Crear ambiente virtual
```
python3 -m venv venv  
```

Activar ambiente virtual (mac)
```
source venv/bin/activate
```


Para instalar los paquetes que usa la API (solamente si no se ha instalado los paquetes en el ambiente virtual)
```
pip install -r requirements.txt
```


Inicializar la API
```
uvicorn src.main:app --reload
uvicorn src.main:app --reload --port 8000
```

Parar 
control+c



