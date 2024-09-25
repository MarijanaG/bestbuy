import csv


num_movies_tv_ma = 0
num_tv_show_tv_ma = 0

with open ("netflix_titles.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["rating"] == "TV-MA":
            if row["type"] == "TV Show":
                num_tv_show_tv_ma += 1
            elif row["type"] == "Movie":
                num_movies_tv_ma += 1

print(f"{num_movies_tv_ma} movies in Netflix")
print(f"{num_tv_show_tv_ma} tv shows in Netflix")