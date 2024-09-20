person_movies= [{'nume': 'George',
                'filme': ['Shrek', 'Bond', 'Fight Club']
                 },
               {'nume': 'Cristian',
                'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
               {'nume': 'Stefan',
                'filme': ['Fight Club', 'Slumdog Milionare']  }
               ]
fav_movie = {}
top_user = {}

nr_filme = 0
nume=""
for i in person_movies:
    if len(i["filme"]) > nr_filme:
        nr_filme = len(i["filme"])
        nume = i["nume"]
    top_user.update({i["nume"]:len(i["filme"])})
    for f in i["filme"]:
        if f in fav_movie:
            fav_movie[f] += 1
        else:
            fav_movie.update({f:1})
film = list(dict(sorted(fav_movie.items(), key=lambda item: item[1], reverse=True)).keys())[0]
top_movies= ",".join(list((dict(sorted(fav_movie.items(), key=lambda item: item[1], reverse=True)).keys())))
top_users=",".join(list((dict(sorted(top_user.items(), key=lambda item: item[1], reverse=True)).keys())))

print(f"Cel mai vizionat film este {film}")
print(f"Utilizatorul cu cele mai multe filme vizionate este: {nume} si a vizualizat un numar de {nr_filme}")
print(top_movies)
print(top_users)

