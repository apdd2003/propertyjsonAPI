from flask import Flask, jsonify
import pandas as pd
import openpyxl
import os
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello</h1>"


@app.route("/project/<string:project_id>", methods=['GET'])
def project(project_id):
    if os.path.isfile('gandhi.xlsx'):
        df = pd.read_excel('gandhi.xlsx', sheet_name='Sheet 1', header=0)
    else:
        return "Could not find gandhi.xlsx file to read, please make sure it exists in the same directory"
    result = df.loc[df['projectRegId'] == int(project_id)]

    print(result.iloc[0].to_dict())
    return jsonify(result.iloc[0].to_dict())


if __name__ == '__main__':
    app.run(debug=True)
