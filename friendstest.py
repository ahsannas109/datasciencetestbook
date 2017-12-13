from __future__ import division
from collections import Counter, defaultdict


users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }]
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]



for user in users:
    user["friend"]=[]
    # print(user)

for i,j in friendships:
    users[i]["friend"].append(users[j])
    users[j]["friend"].append(users[i])



def number_of_friends(user):
    return len(user["friend"])

total_connection = sum(number_of_friends(use) for use in users)
# print total_connection

# get average connection per user

newusr=len(users)
avgConnection = total_connection / newusr

# create a list of userid,num_of_friemds
no_friend_by_id = [(user["id"], number_of_friends(user)) for user in users]

sorted(no_friend_by_id, key=lambda user_id: user_id[1], reverse=True)


# now vp of friend asks to create a list of friends of a friend
def friend_of_a_friend_bad(user):
    return [foaf["id"] for friend in user["friend"]
            for foaf in friend["friend"]]
# this return friends of friends id
 #this is the bad implmentation as it might return a user that we are already referring to

# print(friend_of_a_friend_bad(users[0]))

#we need a pbetter implementation that usestwo other function to not use redundant values
def not_the_same(user,other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friends, other_user)
               for friends in user["friend"])
#now use these two above function to get the correct implementation of the fOAF function

def friend_of_a_friend_good(user):
    return Counter(foaf["id"] for friend in user["friend"]
    for foaf in friend["friend"]
    if not_the_same(user, foaf) and not_friends(user, foaf))

# print(friend_of_a_friend_good(users[4]))


interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

#based on interest find users
def data_scientist_who_like(target_interest):
    return [user_id for user_id, interest in interests
            if interest == target_interest]

# print(data_scientist_who_like("Hadoop"))

#better way of doing the above implementation
interests_by_user_id = defaultdict(list)
#create a dictionary of iterest with user_id
for user_id, interest in interests:
    interests_by_user_id[interest].append(user_id)
# print(interests_by_user_id["Spark"])
user_id_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_id_by_interest[user_id].append(interest)
# print(user_id_by_interest[0])
def most_common_interests_with(user):
    return Counter(interested_user_id for interest in interests_by_user_id[user["id"]]
    for interested_user_id in user_id_by_interest[interest]
    if interested_user_id != user["id"])


# print(most_common_interests_with(users[2]))
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
# print(salary_by_tenure_bucket)

# keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {tenure_bucket: sum(salaries) / len(salaries)
                            for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
# print(average_salary_by_bucket)

# paid_non_paid = [(0.7, "paid"),
#     (1.9, "unpaid"),
#     (2.5, "paid"),
#     (4.2,"unpaid"),
#     (6,"unpaid"),
#     (6.5,"unpaid"),
#     (7.5,"unpaid"),
#     (8.1,"unpaid"),
#     (8.7, "paid"),
#      (10, "paid")]

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"

words_and_counts = Counter(word for user, interest in interests
                           for word in interest.lower().split())
for word, count in words_and_counts.most_common():
    if count>1:
        print (word,count)