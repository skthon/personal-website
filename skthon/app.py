from app import app

"""If this script is an entrypoint, then run the app server """
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)
