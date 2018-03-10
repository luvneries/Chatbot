from synset_similarity import symmetric_sentence_similarity
import re
def sentence_similarity_query(sentence1):
    
    
    
    faq_file = open("coffee_shop_faq.txt").read()    # implememnt with with clause
    faq_split = faq_file.split("?")
    question = ""
    question_answer_list = []
    for faq in faq_split:
        faq_list = faq.split("\n")
        answer = " ".join(faq_list[:-1])
        if(len(question)>10 and len(answer)>10):
            question = " ".join(re.compile('\w+').findall(question))
            answer = " ".join(re.compile('\w+').findall(answer))
            question_answer_list.append([question,answer])
        question = faq_list[-1]+"?"
    sentence1  = " ".join(re.compile('\w+').findall(sentence1))
    score_list = []
    for sets in question_answer_list:
        score_list.append(symmetric_sentence_similarity(sentence1,sets[0]))
    question_query = question_answer_list[score_list.index(max(score_list))][1]
    answer_query = question_answer_list[score_list.index(max(score_list))][1]
    return answer_query


