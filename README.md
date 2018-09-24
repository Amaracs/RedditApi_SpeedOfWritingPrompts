# RedditApi_SpeedOfWritingPrompts

Basically the script just iterates over the top 100 submissions of all time in r/WritingPromts and visualizing the average response time for each submissions and the first reply comment next to the average (except the auto moderator's comment of course).


To create this project I used the reddit python api called PRAW, for data visualization I used plotly, also for debugging I inserted the collected data into a PostgreSQL database by using psycopg2 API.

