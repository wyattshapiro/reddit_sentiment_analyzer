class Comment(object):
    """Object which represents a Reddit comment whose info we are going to scrape."""
    def __init__(self, row):
        """Sets values based on input csv"""

        self.subreddit_name = row[0]
        self.subreddit_id = row[1]
        self.submission_title = row[2]
        self.parent_comment_id = row[3]
        self.comment_link = row[4]
        self.created_utc = row[5]
        self.body = row[6]
        self.author = row[7]
        self.ups = row[9]
        self.downs = row[10]
        self.saved = row[11]
        self.score = row[8]
        self.score_hidden = False
        self.gilded = row[12]
        self.success = True
        self.compound_score = None
        self.compound_score_normalized = None


    def get_success(self):
        """Helper method to get success"""
        return self.success

        # data type
        # self.body = ""
        # self.subreddit_name = ""
        # self.subreddit_id = ""
        # self.comment_link = ""
        # self.parent_id = ""
        # self.created_utc = None
        # self.author = ""
        # self.ups = 0
        # self.downs = 0
        # self.saved = False
        # self.score = 0
        # self.score_hidden = False
        # self.gilded = 0
        # self.success = False
