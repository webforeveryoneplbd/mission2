from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Charger le fichier Excel
    df = pd.read_excel('exemple_agents_badges.xlsx')

    # Identifier les numéros de badge disponibles
    tous_les_badges = set(range(1, 10000))  # Remplace 10000 par le nombre total de badges possibles
    badges_utilises = set(df['Numéro de badge'].unique())
    badges_disponibles = tous_les_badges - badges_utilises

    # Compter le nombre de fois où chaque agent a changé de badge
    changement_badges = df.groupby('Matricule')['Numéro de badge'].nunique()

    return render_template('index.html', badges_disponibles=badges_disponibles, changement_badges=changement_badges)

if __name__ == '__main__':
    app.run(debug=True)
