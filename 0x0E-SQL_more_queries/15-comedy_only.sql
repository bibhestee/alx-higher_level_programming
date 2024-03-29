-- Import the database dump from hbtn_0d_tvshows to MySQL server
-- lists all Comedy shows in the database
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- Only one SELECT statement is allowed
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title FROM tv_show_genres
    INNER JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
        INNER JOIN tv_shows
        ON tv_shows.id = tv_show_genres.show_id
        WHERE tv_genres.name = 'Comedy'
        ORDER BY tv_shows.title ASC;
