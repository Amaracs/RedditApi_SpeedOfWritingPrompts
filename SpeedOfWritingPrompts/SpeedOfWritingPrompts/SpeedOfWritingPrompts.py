#Import Reddit API
import praw
from praw.models import MoreComments

reddit = praw.Reddit(client_id='-',
                     client_secret='-',
                     user_agent='my user agent')



reddit.read_only  
subreddit = reddit.subreddit('writingprompts')


analizedSubmissions = 50
SolutiontimeMin = 0
analizedCommentRange = 300
commentIndex = 0
isFirtComment = True

sumReplyComment = 0

firstValidReponseTime = 0

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
    
    print("Average Time: %s, First Comment Time %s, out of %s first level comments" % (sumReplyComment / commentIndex, firstValidReponseTime, commentIndex))
    print(" ")   
    
    commentIndex = 0
    isFirtComment = True
    sumReplyComment = 0


#Todo: Order by average time:

#Prerequisite for visualization
#orderedDict = OrderedDict(sorted(plotly_SolvedDictionary.items(), key=lambda x: x[1]))
#
#
#generatedList = []
#nameAvgForTrace = "Average Time: "
#if(howManySubmissionsAreSolvedByAuthor is not 0):
#    averageSolutionTime = sumSolutionTime / howManySubmissionsAreSolvedByAuthor
#    for x in range(0, len(orderedDict.keys())):
#        generatedList.append(averageSolutionTime)
#
#    nameAvgForTrace = "Average Time: " + str(round(averageSolutionTime,1))

#Todo: Visualize
     


