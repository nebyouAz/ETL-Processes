# Create Tables

songplay_table_create = ("""
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'songplays')
BEGIN
    CREATE TABLE songplays (
        songplay_id INT PRIMARY KEY,
        start_time DATETIME,
        user_id INT,
        level VARCHAR(10),
        song_id VARCHAR(20),
        artist_id VARCHAR(20),
        session_id INT,
        location VARCHAR(50),
        user_agent VARCHAR(150)
    );
END;
""")

user_table_create = ("""
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'users')
BEGIN
    CREATE TABLE users (
        user_id INT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        gender CHAR(1),
        level VARCHAR(10)
    );
END;
""")

song_table_create = ("""
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'songs')
BEGIN
    CREATE TABLE songs (
        song_id VARCHAR(20) PRIMARY KEY,
        title VARCHAR(100),
        artist_id VARCHAR(20) NOT NULL,
        year INTEGER,
        duration FLOAT
    );
END;
""")

artist_table_create = ("""
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'artists')
BEGIN
CREATE TABLE artists (
    artist_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100),
    lattitude FLOAT,
    longitude FLOAT
);
END;
""")

time_table_create = ("""
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'time')
BEGIN
CREATE TABLE time (
    start_time DATETIME2 PRIMARY KEY,
    hour INTEGER,
    day INTEGER,
    week INTEGER,
    month INTEGER,
    year INTEGER,
    weekday INTEGER
);
END;
""")

# INSERT RECORDS

songplay_table_insert = ("""
MERGE INTO songplays AS target
USING (VALUES (?,?,?,?,?,?,?,?,?)) AS source (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
ON target.songplay_id = source.songplay_id
WHEN NOT MATCHED THEN
    INSERT (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (source.songplay_id, source.start_time, source.user_id, source.level, source.song_id, source.artist_id, source.session_id, source.location, source.user_agent);
""")



user_table_insert = ("""
MERGE INTO users AS target
USING (VALUES (?, ?, ?, ?, ?)) AS source (user_id, first_name, last_name, gender, [level])
ON target.user_id = source.user_id
WHEN MATCHED THEN
    UPDATE SET [level] = source.[level]
WHEN NOT MATCHED THEN
    INSERT (user_id, first_name, last_name, gender, [level])
    VALUES (source.user_id, source.first_name, source.last_name, source.gender, source.[level]);
""")

song_table_insert = ("""
MERGE INTO songs AS target
USING (VALUES (?,?,?,?,?)) AS source (song_id, title, artist_id, year, duration)
ON target.song_id = source.song_id
WHEN NOT MATCHED THEN
    INSERT (song_id, title, artist_id, year, duration)
    VALUES (source.song_id, source.title, source.artist_id, source.year, source.duration);
""")


artist_table_insert = ("""
MERGE INTO artists AS target
USING (VALUES (?,?,?,?,?)) AS source (artist_id, name, location, lattitude, longitude)
ON target.artist_id = source.artist_id
WHEN NOT MATCHED THEN
    INSERT (artist_id, name, location, lattitude, longitude)
    VALUES (source.artist_id, source.name, source.location, source.lattitude, source.longitude);
""")


time_table_insert = ("""
MERGE INTO time AS target
USING (VALUES (?,?,?,?,?,?,?)) AS source (start_time, hour, day, week, month, year, weekday)
ON target.start_time = source.start_time
WHEN NOT MATCHED THEN
    INSERT (start_time, hour, day, week, month, year, weekday)
    VALUES (source.start_time, source.hour, source.day, source.week, source.month, source.year, source.weekday);
""")

# FIND SONGS

song_select = ("""
SELECT ss.song_id, ss.artist_id FROM songs ss 
JOIN artists ars on ss.artist_id = ars.artist_id
WHERE ss.title = ?
AND ars.name = ?
AND ss.duration = ?
;
""")


# Drop Tables

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]







