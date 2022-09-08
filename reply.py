def greating(language):
    match language:
        case 'es':
            return 'Bienvenido a Wiki-Hotel:\nSoy WikiBot , ¿Qué puedo hacer por ti?\n- Hacer una reservacion\n- Precios de las Habitaciones\n- Ubicacion'
        case 'en':
            return 'None'
        case _:
            return 'None'
def booking():
    return 'Tenemos '

            
def replier(res:dict):
    match res:
        case 'greatings':
            return greating('es')
        case _:
            return 'No entender'