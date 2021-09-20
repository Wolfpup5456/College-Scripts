add_movies = ["Shawshank Redemption", "Second Hand Lions", "Back to the Future"]

def movies(filename, list):
    movie = open(filename, "a")

    while True:
        file_input = list
        last = min(file_input, default=0)

        if file_input != "":
            movie.write("\n" + last)
            file_input.remove(last)
            if file_input == []:
                break

    movie.close()

    print("the contents of the movies.txt file are:")
    print("")

    file_read = open("movies.txt", "r")
    file_contents = file_read.read()
    print(file_contents)

    movie.close()

movies(filename="movies.txt", list=add_movies)
