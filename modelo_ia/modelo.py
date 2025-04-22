import pandas as pd
from sklearn.naive_bayes import GaussianNB
import joblib

def treinar_modelo(caminho_csv="dados/resultados.csv"):
    df = pd.read_csv(caminho_csv)
    X = []
    y = []
    for i in range(3, len(df)):
        X.append(df['numero'][i-3:i].tolist())
        y.append(df['numero'][i])
    modelo = GaussianNB()
    modelo.fit(X, y)
    joblib.dump(modelo, "modelo_ia/modelo_treinado.pkl")
    print("Modelo treinado e salvo com sucesso.")

def prever_proximo(entrada):
    modelo = joblib.load("modelo_ia/modelo_treinado.pkl")
    return modelo.predict([entrada])[0]

if __name__ == "__main__":
    treinar_modelo()
    previsao = prever_proximo([10, 25, 17])
    print("Próximo número previsto:", previsao)