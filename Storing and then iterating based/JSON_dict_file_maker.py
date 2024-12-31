from OOP_Model import Game
import json

def main():
    file_handler=open("ALL_Games.json", "w")

    game=Game([" ", " ", " ", " ", " ", " ", " ", " ", " "],"x")

    tree={}

    make_tree(tree, game)
    
    json.dump(tree, file_handler)

def make_tree(node, obj):

    node["chance"]=obj.chance
    node["state"]=obj.state
    node["status"]=obj.status
    node["value"]=obj.value
    node["min"]=obj.min
    node["max"]=obj.max
    node["children"]=[[],[],[]]

    # print(node)
    for i in range(3):
        for j in obj.children[i]:
            node["children"][i].append(dict())
            make_tree(node["children"][i][-1], j)
            



if __name__=="__main__":
    main()