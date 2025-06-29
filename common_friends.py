from pyspark import SparkContext

sc = SparkContext("local", "CommonFriendsApp")

# Charger les données brutes
data = sc.textFile("friends_common.txt")

def parse_line(line):
    parts = line.strip().split()
    user_id = parts[0]
    name = parts[1]
    friends = parts[2].split(",")
    return (user_id, name, friends)

rdd = data.map(parse_line)

# Créer un dict user_id -> nom
user_names = rdd.map(lambda x: (x[0], x[1])).collectAsMap()

# Diffuser ce dict sur les workers
broadcast_names = sc.broadcast(user_names)

# RDD de (user_id, friends)
rdd_friends = rdd.map(lambda x: (x[0], x[2]))

# Générer les paires triées ((min_id, max_id), set_of_friends)
pairs = rdd_friends.flatMap(
    lambda x: [((min(x[0], friend), max(x[0], friend)), set(x[1])) for friend in x[1]]
)

# Réduire par clé pour obtenir l'intersection des sets = amis communs
common = pairs.reduceByKey(lambda a, b: a & b)

# Filtrer la paire (1, 2)
result = common.filter(lambda x: x[0] == ('1', '2')).collect()

for ((u1, u2), friends) in result:
    # Convertir les IDs des amis communs en noms
    names_friends = [broadcast_names.value[f] for f in friends if f in broadcast_names.value]
    print(f"{u1}<{broadcast_names.value[u1]}> {u2}<{broadcast_names.value[u2]}> {names_friends}")

sc.stop()

