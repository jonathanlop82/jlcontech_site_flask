from flask import Flask, render_template, request, flash
from sendmail import send_mail
from sendtelegram import send_telegram_message

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/form', methods=("POST","GET"))
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        company = request.form.get("company")
        message = request.form.get("message")

        #Action
        print(name,email,subject,company,message)
        flash('Gracias por contactarnos, su mensaje ha sido enviado exitosamente, pronto le responderemos!!!')
        send_mail("Nuevo Prospecto desde Formulario Web", "ventas@jlcontech.com", "ventas@jlcontech.com", name, email, subject, company, message)
        mensaje_telegram = f'Nuevo Prospecto: Nombre: {name}, Email: {email}, Asunto: {subject}, Empresa: {company}, Mensaje: {message}'
        send_telegram_message(mensaje_telegram)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


