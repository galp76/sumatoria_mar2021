def greeting():
    import datetime

    dt = datetime.datetime.now()
    hora = dt.hour

    if hora < 12:
        saludo = 'Buenos días Germán.'
    elif 12 <= hora < 19:
        saludo = 'Buenas tardes Germán.'
    else:
        saludo = 'Buenas noches Germán.'

    print('')
    print(saludo)

