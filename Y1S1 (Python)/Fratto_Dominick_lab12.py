movie_list = []
movie = open("movies.txt", "w")

while True:
    file_input = input("what are your favorite movies? (type stop to stop adding movies to your list): ")

    if file_input != "stop":
        movie_list.append(file_input)
        movie.write(file_input + "\n")
    else:
        movie.close()
        print("user stopped the list")
        print("the contents of the movies.txt file are:")
        print("")
        break

file_read = open("movies.txt", "r")
file_contents = file_read.read()
print(file_contents)

movie.close()
