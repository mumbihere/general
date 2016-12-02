###
###
# Author Info:
#     This code is modified from code originally written by Jim Blomo and Derek Kuo
# References
#       http://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/
##/

import itertools
from itertools import repeat,permutations
from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from mrjob.step import MRStep
from math import*
import re

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper1_extract_user_business(self,_,record):
        """Taken a record, yield <user_id, set_of_words>"""
        yield [record['user_id'], re.split('\W+',record['text'])[:-1]]

    def reducer1_compile_businesses_under_user(self,user_id,word_list):
        ###
        # TODO_1: compile words as a list of array under given user_id,after remove duplicate words, yield <user_id, [words]>
        ##/
        yield[user_id, list(set(list(word_list)[0]))]
        

    def mapper2_collect_businesses_under_user(self, user_id, word_sets):
        ###
        # TODO_2: collect all <user_id, words> pair, map into the same Keyword LIST, yield <'LIST',[user_id, [word_sets]]>
        ##/
        yield ['LIST',[user_id, [word_sets]]]
        
    def reducer2_calculate_similarity(self,stat,user_word_sets):
 
        def Jaccard_similarity(word_set_1, word_set_2):
            ###
            # TODO_3: Implement Jaccard Similarity here, output score should between 0 to 1
            ##/
            set_intersection = len(set.intersection(*[set(word_set_1), set(word_set_2)]))
            set_union = len(set.union(*[set(word_set_1), set(word_set_2)]))
            jaccard = 0
            try:
                jaccard = set_intersection/float(set_union)
            except:
                jaccard = 0
            return jaccard

        ###
        # TODO_4: Calculate Jaccard, output the pair users that have similarity over 0.5, yield <[user1,user2], similarity>
        ##/
        
        user_pairs = list(itertools.combinations(user_word_sets, 2))
        for pair in user_pairs:
            jac = Jaccard_similarity(pair[0][1][0],pair[1][1][0])
            if jac>=0.5:
                yield [[pair[0][0],pair[1][0]],jac]
            #else:
                #yield [[pair[0][0],pair[1][0]],jac]

                
                

    def steps(self):
        return [
            MRStep(mapper=self.mapper1_extract_user_business, reducer=self.reducer1_compile_businesses_under_user),
            MRStep(mapper=self.mapper2_collect_businesses_under_user, reducer= self.reducer2_calculate_similarity)
        ]


if __name__ == '__main__':
    UserSimilarity.run()
