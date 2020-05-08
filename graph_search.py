# Graph search algorithm

from collections import deque

def person_is_seller(name):
  return name[-1] == 'm'

graph = {}

graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['ahnung', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['tom', 'jonny']
graph['ahnung'] = []
graph['peggy'] = []
graph['tom'] = []
graph['jonny'] = []

print (graph)
def search_bfs(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            print (person)
            search_queue += graph[person]
            searched.append(person)

def search_dfs(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.pop()
        if person not in searched:
            print (person)
            search_queue += graph[person]
            searched.append(person)

search_bfs('you')
print()
search_dfs('you')

