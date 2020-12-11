data = [
("username1","phone_number1", "email1"),
("usernameX","phone_number1", "emailX"),
("usernameZ","phone_numberZ", "email1Z"),
("usernameY","phone_numberY", "emailX"),
]

indexer = {}
result = []
for i in range(len(data)) :
        flag = True
        for j in range(len(data[i])):
            if data[i][0].lower() == data[j][0].lower() or data[i][1].lower() == data[j][1].lower() or data[i][2].lower() == data[j][2].lower():
                if j in indexer:
                    indexer.update({i:indexer[j]})
                    result[indexer[j]].append(i)
                else:
                    indexer.update({i:i})
                    result.append([i])
                flag = False
                break
        if flag:
            indexer.update({i:i})
            result.append([i])
print(result)