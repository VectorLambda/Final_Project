##This is a standalone version of data loading function, we load the data from the given json file directly.
## For the sake of convience, this loading function is also implemented in the main code directly, so that it would not create
## unncecessary caching of the data.

def load_play(tree,json,ans):
    """Travesing through the tree and reaching the answers.
        If new item is noted, update the tree structure to include the new object.
        
    Parameter:
    ---------
    tree: the tree structure currently in play.
    
    Returns:
    -------
    tree: the tree structure corresponding to the content of the file.
    """
    text, left, right = tree
    if isLeaf(tree):
        # add the json object into the list
        text.append((json["Title"],json["Rated"],json["Plot"],json["Poster"]))
        return tree
    else:
        if len(ans)>0:
            prompt = ans[0]
            ans.pop(0)
            if yes(prompt):
                left = load_play(left,json,ans)
            else:
                right = load_play(right,json,ans)
            tree = (text,left,right)
        return tree
    
def loadTree(f):
    '''create a series of prompts to help
      automatically loading every entry into the recommendation system.
    Parameters:
    ----------
    f: the filestream of the JSON file that is loading.
    Returns:
    --------
    tree: the tree structure of the data.
    '''
    #f = open('movies.json')
    movie_list = json.load(f)
    #movie_list = [movie_list[32]]
    for movie in movie_list:
        ans = []
        # first branch
        if movie["Rated"] == "G" or movie["Rated"] == "PG":
            ans.append("yes")
            if re.search("Animation",movie["Genre"]):
                ans.append("yes")
            elif re.search("Family", movie["Genre"]):
                    ans.append("no")
                    ans.append("yes")
            elif re.search("Comedy",movie["Genre"]):
                ans.append("no")
                ans.append("no")
                ans.append("yes")
        else:
            ans.append("no")
            if re.search("Drama",movie["Genre"]):
                ans.append("yes")
            elif re.search("Horror",movie["Genre"]):
                ans.append("no")
                ans.append("yes")
            elif re.search("Action",movie["Genre"]):
                ans.append("no")
                ans.append("no")
                ans.append("yes")
        tree = load_play(movieTree,movie,ans)
    return tree
from tree import printTree
import json
import re
import random
movieTree = \
    ("Is it a G-rated or PG-rated movie?",
        ("Is it an Animation?", ([],None,None), ("Is it a family movie?",([],None,None),("Is it a comedy movie?",([],None,None),([],None,None)))),
        ("Is it a drama movie?", ([],None,None),("Is it a horror movie?",([],None,None), ("Is it an action movie?",([],None,None),([],None,None)))))

def main():
    f = open("movie.json")
    loadTree(f)
    f.close()

#running the main code.
main()