from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)


model = joblib.load('../models/trained-models.pkl')


btc_df = pd.read_csv('../data/raw/coin_Bitcoin.csv')
eos_df = pd.read_csv('../data/raw/coin_EOS.csv')
sol_df = pd.read_csv('../data/raw/coin_Solana.csv')

@app.route('/predict', methods=['GET'])
def predict():
    crypto = request.args.get('crypto')

    if crypto == 'BTC':
        last_row = btc_df.iloc[-1]
        features = [[last_row['Open'], last_row['High'], last_row['Low'], last_row['Volume'], last_row['Marketcap']]]
    
    elif crypto == 'EOS':
        last_row = eos_df.iloc[-1]
        features = [[last_row['High'], last_row['Low'], last_row['Open'], last_row['Volume'], last_row['Marketcap']]]
    
    elif crypto == 'SOL':
        last_row = sol_df.iloc[-1]
        features = [[last_row['High'], last_row['Low'], last_row['Open'], last_row['Volume'], last_row['Marketcap']]]
    else:
        return jsonify({"error": "Criptomoeda não suportada"}), 400


    prediction = model.predict(features)
    

    return jsonify({"forecast": prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
