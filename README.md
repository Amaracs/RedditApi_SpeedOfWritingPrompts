# RedditApi_SpeedOfWritingPrompts

Basically the script just iterates over the top 100 submissions of all time in r/WritingPromts and visualizing the average response time for each submissions and the first reply comment next to the average (except the auto moderator's comment of course).


To create this project I used the reddit python api called PRAW, for data visualization I used plotly, also for debugging I inserted the collected data into a PostgreSQL database by using psycopg2 API.

User Friendly Data on plot.ly:
https://plot.ly/~amaracs/3/

Raw Data on google drive:
https://docs.google.com/spreadsheets/d/1hZTmlJlQcwNT6FI017k45sM0L1s0QHLokG3QYruE35c/edit?usp=sharing
