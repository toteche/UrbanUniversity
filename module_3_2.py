def send_email(message, recipient, *,sender='university.help@gmail.com'):


    valid_domains = (".com", ".ru", ".net")

    if "@" not in sender or not sender.endswith(valid_domains):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return

    if "@" not in recipient or not recipient.endswith(valid_domains):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return

    if sender.lower() == recipient.lower():
        return "Нельзя отправить сообщение самому себе!"

    if sender.lower() == 'university.help@gmail.com':
        return f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
    else:
        return f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}."

    return f"{message}, {recipient}, {sender}"

# message = 'Это сообщение для проверки связи'
# recipient = 'otheruser@example.com'
# sender='urban.info@gmail.com'

message = input('Введите сообщение: ')
recipient = input('Введите адрес получателя: ')

while True:
    sender = input('Введите адрес отправителя (оставьте пустым для значения по умолчанию): ')
    if sender == '':
        sender = 'university.help@gmail.com'
        break
    else:
        break

print(send_email(message, recipient, sender=sender))
