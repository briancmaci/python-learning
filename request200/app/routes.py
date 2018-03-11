from app import app


@app.route('/trixie_hello', methods=['GET'])
def trixie_hello():
    return "Oh honnnneeyyyyyy YOU GOT SOME SHIT!"