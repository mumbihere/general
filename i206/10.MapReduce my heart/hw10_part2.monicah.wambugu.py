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
 

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper1_extract_user_business(self,_,record):
        """Taken a record, yield <user_id, business_id>"""
        #print(record['user_id'], record['business_id'])
        yield [record['user_id'], record['business_id']]

    def reducer1_compile_businesses_under_user(self,user_id,business_ids):
        ###
        # TODO_1: compile businesses as a list of array under given user_id,after remove duplicate business, yield <user_id, [business_ids]>
        ##/
        my_list = list(set([x for x in business_ids]))
        #print(user_id, my_list)
        yield[user_id, my_list]

    def mapper2_collect_businesses_under_user(self, user_id, business_ids):
        ###
        # TODO_2: collect all <user_id, business_ids> pair, map into the same Keyword LIST, yield <'LIST',[user_id, [business_ids]]>
        ##/
        yield ['LIST',[user_id, [business_ids]]]
        
    def reducer2_calculate_similarity(self,stat,user_business_ids):
 
        def Jaccard_similarity(business_list1, business_list2):
            ###
            # TODO_3: Implement Jaccard Similarity here, output score should between 0 to 1
            ##/
            set_intersection = len(set.intersection(*[set(business_list1), set(business_list2)]))
            set_union = len(set.union(*[set(business_list1), set(business_list2)]))
            jaccard = 0
            try:
                jaccard = set_intersection/float(set_union)
            except:
                jaccard = 0
            
            return jaccard

        ###
        # TODO_4: Calculate Jaccard, output the pair users that have similarity over 0.5, yield <[user1,user2], similarity>
        ##/
        
        user_pairs = list(itertools.combinations(user_business_ids, 2))
        for pair in user_pairs:
            jac = Jaccard_similarity(pair[0][1][0],pair[1][1][0])
            if jac>=0.5:
                yield [pair[0][0],pair[1][0]],jac

                
                

    def steps(self):
        return [
            MRStep(mapper=self.mapper1_extract_user_business, reducer=self.reducer1_compile_businesses_under_user),
            MRStep(mapper=self.mapper2_collect_businesses_under_user, reducer= self.reducer2_calculate_similarity)
        ]


if __name__ == '__main__':
    UserSimilarity.run()
