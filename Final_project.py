
# Questions to ask:
# (Is it a G rated movie?)
# Is it released before 2000?
# Is it longer than two hours?
# Is it an Action Genre?
# Is is a Comedy Genre?
# Is it a Drama Genre?


# we put multiple data in a leaf node. Every time it reaches a leaf node, we will pop out a movie series randomly.
# we can't capture the movie data directly. It has to be stored in a cache before we can proceed with the seraching tree.

#load 100 movies:
# helper funcitons:
from tree import printTree
import json
import re
import random
movieTree = \
    ("Is it a G-rated or PG-rated movie?",
        ("Is it an Animation?", ([],None,None), ("Is it a family movie?",([],None,None),("Is it a comedy movie?",([],None,None),([],None,None)))),
        ("Is it a drama movie?", ([],None,None),("Is it a horror movie?",([],None,None), ("Is it an action movie?",([],None,None),([],None,None)))))

def isLeaf(tree):
    '''check if the tree is a leaf node
    Parameter:
    ---------
    tree: the tree structure currently in play.

    Returns:
    -------
    boolean of whether the parameter is a leaf node.
    '''
    text, left, right = tree
    if left is None and right is None:
        return True
    else: 
        return False

def yes(prompt):
    '''check if the answer to the leaf node item is affirmative.
        If not, create a new branch in place of the Leaf node
    Parameter:
    ---------
    prompt: the answer inputted by the user.

    Returns:
    -------
    The boolean of the prompt.
    '''
    affirmative = ['yes','yup','sure','y']
    if prompt in affirmative:
        return True
    else:
        return False

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
        text.append((json))
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
#printTree(movieTree)


def loadTree():
    f = open('movies.json')
    movie_list = json.load(f)
    #movie_list = [movie_list[32]]
    itr = 0
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

def play(tree):
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
        # ask if it is the object you are looking for.
        if len(text)==0:
            print("We don't have any recommended movies for you, please try again.")
        else:
            print("Here is what you might like:")
            #rand_num = random.randint(0,len(text)-1)
            
            if len(text)<=5:
                for i in range(len(text)):
                    print(f'movie {i+1}:')
                    print(text[i]["Title"])
                    print("Rated: ", text[i]["Rated"])
                    print("Poster Link: ", text[i]["Poster"])
                    print(text[i]["Plot"])
                    print("")
            
            else:
                rand_num = random.sample(range(0, len(text)), 5)
                prompt = 'yes'
                while yes(prompt):
                    for j in range(5):
                        print(f'movie {j+1}:')
                        print(text[rand_num[j]]["Title"])
                        print("Rated: ", text[rand_num[j]]["Rated"])
                        print("Poster Link: ", text[rand_num[j]]["Poster"])
                        print(text[rand_num[j]]["Plot"])
                        print("")
                    prompt = input("Would you like to look for another set of recommendation? ")
        return tree
    else:
        prompt = input(text)
        if yes(prompt):
            left = play(left)
        else:
            right = play(right)
        tree = (text,left,right)
        return tree

if __name__ == '__main__':
    movieTree = loadTree()
    prompt = "yes"# default
    while yes(prompt):
        movieTree = play(movieTree)
        prompt = input("Would you like to try again?(type 'yes' to proceed) ")
    print("Thanks for using Movies Recommend! See you again soon!")