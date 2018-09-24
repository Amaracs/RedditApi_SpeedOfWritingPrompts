#Import Reddit API
import praw
from praw.models import MoreComments

import SubmissionClass


reddit = praw.Reddit(client_id='IBmMSzy2se2Igg',
                     client_secret='9Wa2VKXHAzxNEo7A3zo0wTz-EuE',
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
    plotly_AvgTimeDictionary[submission.title] = avgTime
    plotly_FirstCommentTimeDictionary[submission.title] = firstValidReponseTime

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
     


