person_movies= [{'nume': 'George',
                'filme': ['Shrek', 'Bond', 'Fight Club']
                 },
               {'nume': 'Cristian',
                'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
               {'nume': 'Stefan',
                'filme': ['Fight Club', 'Slumdog Milionare']  }
               ]
fav_movie = {}
most_movies = {}
top_movies = {}
top_user = {}
for i in person_movies:
    for f in i["filme"]:
        if f in fav_movie:
            fav_movie[f] += 1
        else:
            fav_movie.update({f:1})
print(sorted(fav_movie.values()))
