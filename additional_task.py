import socket
import threading
import time


def server_thread():
    """Функция сервера в отдельном потоке"""
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5000


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    print("Сервер запущен, ожидание данных...")


    actors_by_genre = {
        'comedy': set(),
        'drama': set(),
        'action': set(),
        'horror': set()
    }


    genres = ['comedy', 'drama', 'action', 'horror']
    for message_number in range(4):
        data, addr = sock.recvfrom(1024)
        actors_list = data.decode('utf-8').strip().split()
        actors_by_genre[genres[message_number]] = set(actors_list)
        print(f"Получены данные для жанра {genres[message_number]}: {actors_list}")


    only_comedy_actors = actors_by_genre['comedy'].copy()

    only_comedy_actors.difference_update(
    actors_by_genre['drama'],
        actors_by_genre['action'],
        actors_by_genre['horror']
    )

    print(f"\nАктеры, снимавшиеся только в комедиях: {only_comedy_actors}")
    print(f"Количество: {len(only_comedy_actors)}")

    sock.close()


def client_thread():
    """Функция клиента в отдельном потоке"""

    time.sleep(1)

    UDP_IP = "127.0.0.1"
    UDP_PORT = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    messages = [
        "Иванов Петров Смирнов",
        "Петров Соколова",
        "Васильева",
        "Смирнов Михайлов"
    ]

    print("\nКлиент отправляет данные...")
    for msg_index, msg_text in enumerate(messages):
        sock.sendto(msg_text.encode(), (UDP_IP, UDP_PORT))
        print(f"Отправлено сообщение {msg_index + 1}: {msg_text}")
        time.sleep(0.5)

    sock.close()



if __name__ == "__main__":

    server = threading.Thread(target=server_thread)
    server.start()


    client = threading.Thread(target=client_thread)
    client.start()


    client.join()
    server.join()
