import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

import config as config
from models.models import Comment
import util.csv_util as csv_util
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
# nltk.download('vader_lexicon')  # one time install
sia = SIA()

HEADER = ["subreddit_name",
            "submission_title",
            "created_utc",
            "body",
            "author",
            "ups",
            "downs",
            "compound_score_normalized"]


def calculate_sentiment(comment):
    res = sia.polarity_scores(comment.body)
    comment.compound_score = res['compound']

    # create sentiment score out of range 0 to 1 instead of -1 to 1
    compound_score_normalized = (comment.compound_score + 1)/2
    comment.compound_score_normalized = compound_score_normalized

    return comment


def calculate_word_distributions(pos_list, neg_list):
    with open(config.INPUT_PATH_POS, "w") as f_pos:
        for comment in pos_list:
            f_pos.write(comment + "\n")

    with open(config.INPUT_PATH_NEG, "w") as f_neg:
        for comment in neg_list:
            f_neg.write(comment + "\n")

    tokenizer = RegexpTokenizer(r'\w+')
    # print(tokenizer.tokenize(example))

    stop_words = set(stopwords.words('english'))
    # print(stop_words)

    all_words_pos = []
    with open(config.INPUT_PATH_POS, "r") as f_pos:
        for line in f_pos.readlines():
            words = tokenizer.tokenize(line)
            for w in words:
                if w.lower() not in stop_words:
                    all_words_pos.append(w.lower())

    pos_res = nltk.FreqDist(all_words_pos)
    print("Most common positive words %s" % pos_res.most_common(8))
    print
    all_words_neg = []
    with open(config.INPUT_PATH_NEG, "r") as f_neg:
        for line in f_neg.readlines():
            words = tokenizer.tokenize(line)
            for w in words:
                if w.lower() not in stop_words:
                    all_words_neg.append(w.lower())

    neg_res = nltk.FreqDist(all_words_neg)
    print("Most common negative words %s" % neg_res.most_common(8))
    print
    return (pos_res, all_words_pos, neg_res, all_words_neg)


def run():
    """Analyse reddit comments from a subreddit."""
    print
    input_path = config.INPUT_PATH
    comment_row_list = csv_util.read_csv(input_path)
    comment_list = []
    pos_list = []
    neg_list = []

    # calculate sentiment for each comment
    for comment_row in comment_row_list:
        comment = Comment(comment_row)
        comment = calculate_sentiment(comment)
        comment_list.append(comment)

        if comment.compound_score > 0.2:
            pos_list.append(comment.body)
        elif comment.compound_score < -0.2:
            neg_list.append(comment.body)

    # write out CSV with sentiment score for each comment
    output_path = config.OUTPUT_PATH
    csv_util.write_row(output_path, comment=None, header=HEADER)
    for comment in comment_list:
        csv_util.write_row(output_path, comment=comment)

    # distribution analysis
    (pos_res, all_words_pos, neg_res, all_words_neg) = calculate_word_distributions(pos_list, neg_list)


if __name__ == "__main__":
    run()
