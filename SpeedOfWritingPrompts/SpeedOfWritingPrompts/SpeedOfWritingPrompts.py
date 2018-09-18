#Import Reddit API
import praw
from praw.models import MoreComments

import operator
from collections import OrderedDict


reddit = praw.Reddit(client_id='kYl1K0MGxqbN2w',
                     client_secret='5dYrrVHVyDV7jp6kfdoz65_9LZM',
                     user_agent='my user agent')



reddit.read_only  
subreddit = reddit.subreddit('writingprompts')


analizedSubmissions = 5
SolutiontimeMin = 0
analizedCommentRange = 300
commentIndex = 0
isFirtComment = True
avgTime = 0

sumReplyComment = 0

firstValidReponseTime = 0

#TODO: Use class instead?
#For data visualization with Plotly:
plotly_AvgTimeDictionary = {}
plotly_FirstCommentTimeDictionary = {}


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
    plotly_AvgTimeDictionary[submission.title] = avgTime
    plotly_FirstCommentTimeDictionary[submission.title] = firstValidReponseTime

    print("Average Time: %s, First Comment Time %s, out of %s first level comments" % (avgTime, firstValidReponseTime, commentIndex))
    print(" ")   
    
    commentIndex = 0
    isFirtComment = True
    sumReplyComment = 0
    avgTime = 0


#Todo: Order by average time:

#Prerequisite for visualization
orderedDict = OrderedDict(sorted(plotly_AvgTimeDictionary.items(), key=lambda x: x[1]))
print(orderedDict)


#Todo: Visualize
     


