############################################################
# CMPSC442: Homework 4
############################################################

student_name = "Joseph Sepich"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import email
import collections
import math
import os

############################################################
# Section 1: Spam Filter
############################################################

def load_tokens(email_path):
    """Loads all text tokens from email at file path
    into a list.
    
    Arguments:
        email_path {string} -- path to email file on disk
    
    Returns:
        list[string] -- list of text tokens
    """
    email_file = open(email_path, 'r')
    # read message from file
    message = email.message_from_file(email_file)
    # create list of tokens
    tokens = []
    for line in email.iterators.body_line_iterator(message):
        [tokens.append(token) for token in line.strip().split(' ') if token is not '']
    email_file.close()
    return tokens

def log_probs(email_paths, smoothing):
    """Determines the log probability of a each word/token appearing
    in the given set of emails.
    
    Arguments:
        email_paths {list[string]} -- list of paths to email files
        smoothing {float} -- smoothing factor alpha = 1 / m
    
    Returns:
        [type] -- [description]
    """
    # load all tokens
    tokens = []
    for path in email_paths:
        [tokens.append(token) for token in load_tokens(path)]
    # create dictionary
    word_count = collections.defaultdict(int)
    total_count = len(tokens)
    for token in tokens:
        word_count[token] += 1
    unique_count = len(word_count.keys())
    probs = {}
    for key in word_count.keys():
        probs[key] = math.log((word_count[key] + smoothing) / (total_count + smoothing * (unique_count + 1)))
    probs['<UNK>'] = math.log((smoothing) / (total_count + smoothing * (unique_count + 1)))
    return probs

class SpamFilter(object):

    def __init__(self, spam_dir, ham_dir, smoothing):
        spam_files = os.listdir(spam_dir)
        ham_files = os.listdir(ham_dir)
        spam_files = [spam_dir + '/' + f for f in spam_files]
        ham_files = [ham_dir + '/' +  f for f in ham_files]
        self.cond_spam = log_probs(spam_files, smoothing)
        self.cond_ham = log_probs(ham_files, smoothing)
        self.p_spam = math.log(len(spam_files) / (len(spam_files) + len(ham_files)))
        self.p_ham = math.log(len(ham_files) / (len(spam_files) + len(ham_files)))
    
    def is_spam(self, email_path):
        email_tokens = load_tokens(email_path)
        # compute spam value
        spam_val = self.p_spam
        for token in email_tokens:
            if token not in self.cond_spam.keys():
                spam_val += self.cond_spam['<UNK>']
            else:
                spam_val += self.cond_spam[token]
        # compute ham value
        ham_val = self.p_ham
        for token in email_tokens:
            if token not in self.cond_ham.keys():
                ham_val += self.cond_ham['<UNK>']
            else:
                ham_val += self.cond_ham[token]
        if spam_val > ham_val:
            return True
        return False

    def most_indicative_spam(self, n):
        indications = {}
        for key in self.cond_spam.keys():
            if key in self.cond_ham.keys():
                indications[key] = self.cond_spam[key] - math.log(math.exp(self.cond_spam[key]) + math.exp(self.cond_ham[key]))
        top = []
        for key, value in sorted(indications.items(), key=lambda kv: kv[1], reverse=True):
            top.append(key)
            if len(top) == n:
                return top
        return top

    def most_indicative_ham(self, n):
        indications = {}
        for key in self.cond_ham.keys():
            if key in self.cond_spam.keys():
                indications[key] = self.cond_ham[key] - math.log(math.exp(self.cond_spam[key]) + math.exp(self.cond_ham[key]))
        top = []
        for key, value in sorted(indications.items(), key=lambda kv: kv[1], reverse=True):
            top.append(key)
            if len(top) == n:
                return top
        return top

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
I spent approximately 4 hours on this assignment.
"""

feedback_question_2 = """
I found the log probability part the most challenging.
At first I did not know the proper equation, because the image of the
formula is not visible on the Canvas description. I also was able to only get half of the
test cases working, not including my own.
"""

feedback_question_3 = """
I really liked the last question. Although it gave us the formula
to determine what was most indicative, it did not help us breakdown how to
use the formula. I liked having to write out the math on paper to figure this out.
"""
