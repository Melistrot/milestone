movies = []

def menu():
    user_input = input("Введите 'a' для того что бы добавить фильм, 'l' посмотреть фильм, 'f' найти фильм и 'q' для того что бы выйти: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print('Неправильная команда, попробуйте снова.')

        user_input = input("Введите 'a' для того что бы добавить фильм, 'l' посмотреть фильм, 'f' найти фильм и 'q' для того что бы выйти: ")

def add_movie():
    name = input('Введите название фильма: ')
    director = input('Введите имя режисера: ')
    year = input('Введите год фильмы: ')

    movies.append({
        'Название': name,
        'Режисер': director,
        'Год': year
    })

def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)

def show_movie_details(movie):
        print(f"Название: {movie['Название']}")
        print(f"Режисер: {movie['Режисер']}")
        print(f"Год: {movie['Год']}")


def find_movie():
    find_by = input("По какому параметру вы хотите выполнить поиск? ")
    looking_for = input("Что вы ищите? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)
 

def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)
    
    return found

menu()

