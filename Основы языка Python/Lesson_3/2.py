# Коментарий для создания PR


def user_info(name='-', surname='-', born_date='-',
              living_town='-', email='-', phone='-'):
    return name, surname, born_date, living_town, email, phone


new_user = user_info(name='Tom', surname='Krakovsky',
                     born_date='13.06.1973', living_town='New Reno',
                     email='tom@newreno.com', phone='+3(153)-353-53-53')
print(new_user)