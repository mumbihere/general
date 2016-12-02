###
# Author Info:
#     This code is modified from code originally written by Jim Blomo and Derek Kuo
##/



from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from mrjob.step import MRStep

import re

WORD_RE = re.compile(r"[\w']+")

class UniqueReview(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    
    def mapper1_extract_words(self, _, record):
        
        """Take in a record, yield <word, review_id>"""
            ###
            # TODO: for each word in the review, yield the correct key,value
            # pair:
        for word in WORD_RE.findall(record['text']):
            #print(word.lower(), record['review_id'] )
            yield [ word.lower(), record['review_id'] ]

    
            

        
    def reducer1_count_reviews(self, word, review_ids):
        """Count the number of reviews a word has appeared in.  If it is a
        unique word (ie it has only been used in 1 review), output that review
        and 1 (the number of words that were unique)."""

        #unique_reviews = set(review_ids)  # set() uniques an iterator
        ###
        # TODO: yield the correct pair when the desired condition is met:
        #print('reducer 1',list(review_ids))
        Reviews = [x for x in review_ids]

        if len(Reviews)==1:
            yield [Reviews[0] , 1]
        ##/

    def reducer2_count_unique_words(self, review_id, unique_word_counts):
        """Output the number of unique words for a given review_id"""
        ###
        # TODO: summarize unique_word_counts and output the result
        #print('\n',review_id, sum([y for y in unique_word_counts]))

        yield review_id, sum(unique_word_counts)
        ##/

    def mapper3_aggregate_max(self, review_id, unique_word_count):
        """Group reviews/counts together by the MAX statistic."""
        ###
        # TODO: By yielding using the same keyword, all records will appear in
        # the same reducer:
        #print(review_id, unique_word_count)
        value = [unique_word_count, review_id]
        yield ['maximum count',value]
        ##/

    def reducer3_select_max(self, stat, count_review_ids):
        """Given a list of pairs: [count, review_id], select on the pair with
        the maximum count, and output the result."""
        ###
        # TODO: find the review with the highest count, yield the review_id and
        # the count. HINT: the max() function will compare pairs by the first
        # number
        #
        #/

        review_counts = [x for x in count_review_ids]
        yield [stat, max(review_counts)]


    def steps(self):
        return [MRStep(mapper=self.mapper1_extract_words, reducer=self.reducer1_count_reviews),
                MRStep(reducer=self.reducer2_count_unique_words),
                MRStep(mapper=self.mapper3_aggregate_max, reducer=self.reducer3_select_max)]

if __name__ == '__main__':
    UniqueReview.run()
