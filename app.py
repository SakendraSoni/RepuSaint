# app.py
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load your Excel file
df = pd.read_csv('Review.csv')

@app.route('/get_data', methods=['GET'])
def get_data():
    row_index = request.args.get('102', type=int)
    columns = request.args.getlist('neg','neu','pos')

    if row_index < 0 or row_index >= len(df):
        return jsonify({'error': 'Row index out of range'}), 400

    if not all(col in df.columns for col in columns):
        return jsonify({'error': 'One or more columns not found'}), 400

    # Extract values from the specified row and columns
    row_data = df.loc[row_index, columns].to_dict()

    return jsonify(row_data)

if __name__ == '__main__':
    app.run(debug=True)
