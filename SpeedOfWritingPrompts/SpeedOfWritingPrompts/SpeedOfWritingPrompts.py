#Import Reddit API
import praw
from praw.models import MoreComments

#Import Plotly API
import plotly
import plotly.graph_objs as go

#Import Module for Ordered Complex Class
import SubmissionClass


reddit = praw.Reddit(client_id='-',
                     client_secret='-',
                     user_agent='my user agent')






reddit.read_only  
subreddit = reddit.subreddit('writingprompts')


analizedSubmissions = 5000
SolutiontimeMin = 0
analizedCommentRange = 300
commentIndex = 0
isFirtComment = True
avgTime = 0

sumReplyComment = 0

firstValidReponseTime = 0

submissionObjects = SubmissionClass.SubmissionClass()

for submission in subreddit.top(limit=analizedSubmissions):
    submission.comments.replace_more(limit=0)
    print(submission.title)
    for top_level_comment in submission.comments:
        if(isFirtComment):
            #Skip autoMod comment
            isFirtComment = False
            continue
        else:
            #Create an upper limit and do not analize all top level comments
            if(commentIndex == analizedCommentRange):
                break
            else:
                #print(commentIndex)
                SolutiontimeMin = ((top_level_comment.created_utc - submission.created_utc) / 60)
                #print(round(SolutiontimeMin,2))  
                commentIndex += 1
                sumReplyComment += SolutiontimeMin
                if(commentIndex == 1):
                    firstValidReponseTime = SolutiontimeMin

    avgTime = round(sumReplyComment / commentIndex,1)


    submissionObjects.append(submission.title,avgTime,round(firstValidReponseTime,1))

    print("Average Time: %s, First Comment Time %s, out of %s first level comments" % (avgTime, firstValidReponseTime, commentIndex))
    print(" ")   
    
    commentIndex = 0
    isFirtComment = True
    sumReplyComment = 0
    avgTime = 0

#Print ordered object by average time:
submissionObjects.print()


#Todo: Visualize

#Visualization with Plotly
plotly.offline.plot({
    "data": [go.Bar(y = submissionObjects.submissionAvgTime,
                    x = submissionObjects.submissionTitle,
                    name ='Average Time'),
             
             go.Bar(y = submissionObjects.submissionFirstCommentTime,
                    x = submissionObjects.submissionTitle,
                    name = 'Top Comment Time')],
        
    "layout": go.Layout(title = "How fast are top level comments in r/WritingPrompts compared to average response time",
                        xaxis = dict(title = 'Submissions',
                                        titlefont=dict(family='Courier New, monospace',
                                        size=18,
                                        color='#7f7f7f')),
                        yaxis = dict(title = 'Time (min)',
                                        titlefont=dict(family='Courier New, monospace',
                                        size=18,
                                        color='#7f7f7f')))
}, auto_open=True)


