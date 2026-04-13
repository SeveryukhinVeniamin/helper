'''SELECT
    album.Title,
    artist.Name
FROM
    album
INNER JOIN artist
    ON artist.ArtistId = album.ArtistId;'''

import sqlite3

con = sqlite3.connect('data.bd')
cur = con.cursor()
rez = cur.execute("""
SELECT 
    people.name
    age.type
fROM 
    people
LEFT JOIN moods
    ON moods.id = people.mood_id;
LEFT JOIN ages
    ON ages.id = people.age_id;
WHEN 
    moods.id > 5 AND moods.id < 7
ORDER BY moods.type, ages.type
""").fetchall()
print(rez)