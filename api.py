from ejtraderMT import Metatrader

api = Metatrader(host="node-1")

df = api.history("EURUSD","M1",50)

print(df)


