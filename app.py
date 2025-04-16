from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    response = requests.get(url)

    if response.status_code != 200:
        return "<p>Error al obtener el archivo desde la URL.</p>"

    lines = response.text.strip().split("\n")
    people = []

    for line in lines[1:]:  # Saltar encabezado
        parts = line.strip().split(";")  # <-- CORREGIDO

        if len(parts) < 5 or not parts[0]:
            continue

        if parts[0][0] in ['3', '4', '5', '7']:
            people.append({
                "ID": parts[0],
                "Nombre": parts[1],
                "Apellido": parts[2],
                "Género": parts[3],
                "Edad": parts[4]
            })

    html = '''
    <h1>Personas con ID que comienza en 3, 4, 5 o 7</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Género</th>
            <th>Edad</th>
        </tr>
        {% for person in people %}
        <tr>
            <td>{{ person.ID }}</td>
            <td>{{ person.Nombre }}</td>
            <td>{{ person.Apellido }}</td>
            <td>{{ person.Género }}</td>
            <td>{{ person.Edad }}</td>
        </tr>
        {% endfor %}
    </table>
    '''
    return render_template_string(html, people=people)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
