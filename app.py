from app import create_app

app = create_app(template_folder='../templates')

if __name__ == '__main__':
    app.run(host="192.168.56.1",debug=True)
