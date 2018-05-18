import sys
import csv

# Set encoding to utf-8 rather than ascii, as is default for python 2.
# This avoids ascii errors on csv write.
reload(sys)
sys.setdefaultencoding('utf-8')


def read_csv(input_path):
    """Reads a csv file into a list of lists
    path: String representing the path to the csv file

    return: List of Lists representing the file
    """
    with open(input_path, 'rb') as f:
        reader = csv.reader(f)
        read_list = list(reader)
        return read_list[1:]


def write_row(output_path, comment=None, header=None):
    """Writes a Comment object to a csv file.

    comment: comment object to write out
    header: header row
    """
    try:
        with open(output_path, "ab") as output:
            writer = csv.writer(output)
            if comment:
                row = [comment.subreddit_name,
                        comment.submission_title,
                        comment.created_utc,
                        comment.body,
                        comment.author,
                        comment.ups,
                        comment.downs,
                        comment.compound_score_normalized]
            elif header:
                row = header
            else:
                row = []
            writer.writerow(row)

    except Exception, e:
        print(e)
        print("Write row failed")
