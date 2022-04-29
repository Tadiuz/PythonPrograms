class Trie:
  def __init__(self):
    self.root = {"*":"*"}

  def add_word(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node:
        curr_node[letter] = {}
      curr_node = curr_node[letter]
    curr_node["*"] = "*"
  
  def does_word_exist(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node:
        return False
      curr_node = curr_node[letter]
    return "*" in curr_node

  def find_maxim(self, number):
    binary = f"{number:032b}"
    complement = binary.replace("0","2").replace("1","0").replace("2","1")
    curr_node = self.root
    lista = ""
    for i in complement:
      if i == "0" and "0" in curr_node or i== "1" and "1" not in curr_node:
        lista += "0"
        curr_node = curr_node["0"]
      else:
        lista += "1"
        curr_node = curr_node["1"]
    return int(lista,2)
      


trie = Trie()
numbers = [3,7,5,10,2]
queries = [6,4]
#for number in numbers:
  #trie.add_word(f"{number:032b}")
trie.add_word(f"HOLA")
trie.add_word(f"aMIGO")
trie.add_word(f"HOLO")

# lista = []
# for query in queries:
#   lista.append(trie.find_maxim(queries[0])^query)

# print(lista)