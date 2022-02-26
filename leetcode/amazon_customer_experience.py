numCompetitors=6
topNCompetitors = 2
competitors = ['newshop', 'shopnow', 'afashion', 'fashionbeats', 'mymarket', 'tcellular']
numReviews = 6
reviews = [
"newshop is providing good services in the city; everyone should use newshop",
"best services by newshop",
"fashionbeats has great services in the city",
"I am proud to have fashionbeats",
"mymarket has awesome services",
"Thanks Newshop for the quick delivery"]

competitors = set(competitors)

reviews_list = []
for review in reviews:
    reviews_list.extend(review.replace(';','').replace('.','').split())

answer = {}
for i in reviews_list:
    if i in competitors:
        if answer.get(i):
            answer[i] +=1
        else:
            answer[i] = 1
answersorted = sorted(list(answer.items()),key=lambda x:x[1],reverse=True)
first_two = [i[0] for i in answersorted[:topNCompetitors]]