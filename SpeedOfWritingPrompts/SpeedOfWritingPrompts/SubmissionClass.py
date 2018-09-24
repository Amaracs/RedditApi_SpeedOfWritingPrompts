class SubmissionClass(object):
    """Object that contains all submissions and their average time also ordered by it and first time comment"""
    def __init__(self):
        self.submissionTitle = []
        self.submissionAvgTime = []
        self.submissionFirstCommentTime = []

    def print(self):
        print("Starts Here")
        print(self.submissionTitle)
        print(self.submissionAvgTime)
        print(self.submissionFirstCommentTime)
        print("Ends Here")



    def append(self, title, avgTime, firstTime):
            isInserted = False
            indexToInsert = 0
            for x in range(0, len(self.submissionTitle)):
                
                if(avgTime <= self.submissionAvgTime[x]):
                    indexToInsert = x

                    self.submissionTitle.insert(indexToInsert,title)
                    self.submissionAvgTime.insert(indexToInsert,avgTime)
                    self.submissionFirstCommentTime.insert(indexToInsert,firstTime)
                    isInserted = True
                    break
            
            #Append at the back if it was not inserted beforehand: 1.: Empty List, 2.:Larger than the previous max value
            if(isInserted == False):
                self.submissionTitle.append(title)
                self.submissionAvgTime.append(avgTime)
                self.submissionFirstCommentTime.append(firstTime)
