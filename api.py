from ejtraderMT import Metatrader

api = Metatrader(host="node-1")

api.history("EURUSD","M1",300)



