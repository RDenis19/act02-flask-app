from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    data = requests.get(url).text.strip().split("\n")[1:]  # Omitir cabecera

    people = [
        {"ID": p[0], "Nombre": p[1], "Apellido": p[2], "País": p[3], "Dirección": p[4]}
        for line in data if (p := line.strip().split("|")) and p[0][:1] in "3457"
    ]

    html = '''
    <table border="1" cellpadding="5">
        <tr><th>ID</th><th>Nombre</th><th>Apellido</th><th>País</th><th>Dirección</th></tr>
        {% for person in people %}
        <tr>
            <td>{{ person.ID }}</td>
            <td>{{ person.Nombre }}</td>
            <td>{{ person.Apellido }}</td>
            <td>{{ person.País }}</td>
            <td>{{ person.Dirección }}</td>
        </tr>
        {% endfor %}
    </table>
    '''
    return render_template_string(html, people=people)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
