from fastapi  import FastAPI
import httpx
import json

# Crear una instancia de FastAPI
app = FastAPI()

# Definir una ruta básica
def login(api_url, username, password):
    # Crear los datos del formulario
    data = {"email": username, "password": password}
    json_data = json.dumps(data)
    # Hacer la solicitud POST a la API
    with httpx.Client() as client:
        response = client.post(f"{api_url}/login", data=json_data)

    # Verificar el estado de la respuesta
    if response.status_code == 201:
        # La solicitud fue exitosa, el token debe estar en el cuerpo de la respuesta
        token = response.json().get("token")
        print(f"Login exitoso. Token: {token}")
        return token
    else:
        # La solicitud falló, imprimir el código de estado y el contenido de la respuesta
        print(f"Error en la solicitud. Código de estado: {response.status_code}")
        print(f"Contenido de la respuesta: {response.text}")
# Ejemplo de uso


def peticion_materials():
    api_url = "http://127.0.0.1:8000"  # Reemplaza esto con la URL real de tu API
    username = "tier2@gmail.co"
    password = "pzs12345"
    token = login(api_url, username, password)
    print(token)
    data = {
    "client": username,
    "products": [
        {
        "id_pro": "655455bef786b6ad709433e",
        "quantity": 230
        }
        ],
        "date_delivery_expected": "11-11-2023"
    }
    json_data = json.dumps(data)
    with httpx.Client() as client:
            headers = {"Authorization": f"Bearer {token}"}
            response = client.post(f"{api_url}/client/request/api", headers=headers,data=json_data)

        # Verificar el estado de la respuesta
    if response.status_code == 200:
            # La solicitud fue exitosa, imprimir el contenido de la respuesta
            print(f"Solicitud protegida exitosa. Contenido: {response.text}")
    else:
            # La solicitud falló, imprimir el código de estado y el contenido de la respuesta
            print(f"Error en la solicitud protegida. Código de estado: {response.status_code}")
            print(f"Contenido de la respuesta: {response.text}")
    

peticion_materials()

# Si ejecutas este script directamente, FastAPI lanzará el servidor en el puerto 8001
if __name__ == "__main__":
    import uvicorn

    # Iniciar el servidor utilizando uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)