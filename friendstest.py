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

for i,j in friendships:
    users[i]["friend"].append(users[j])
    users[j]["friend"].append(users[i])



def number_of_friends(user):
    return len(user["friend"])

total_connection = sum(number_of_friends(use) for use in users)
# print total_connection

no_friend_by_id=[(user["id"], number_of_friends(user)) for user in users]

print sorted(no_friend_by_id, key=lambda (user_id,no_of_fr):no_of_fr, reverse=True)
