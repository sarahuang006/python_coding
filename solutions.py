
"""
Question 1:

"""
import collections
def question1(s, t):
    if len(s) != len(t):
        return False 
    count = collections.defaultdict(int)
    for c in s:
        count[c] += 1
    for c in t:
        count[c] -= 1
        if count[c] < 0:
            return False
    return True
        


"""
Question 2

"""

def question2(s):
    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res
 
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]


"""
Question 3

"""
def find( parent,i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, root1, root2):
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else :
        parent[root2] = root1
        rank[root1] += 1


# constructing minimal spanning tree MST using Kruskal's algorithm
def MST(graph, order, vertex_dict_rev):
    
    parent = []
    rank = []

    #store result in [u,v,w ] formate
    result = []

    # sort the edges
    graph =  sorted(graph,key=lambda item: item[2])

    parent = []
    rank = []

    # make sets of a single element
    for node in range(order):
        parent.append(node)
        rank.append(0)
        
    i = 0 # index for graph
    e = 0 # index for result      

    while e < order -1 :
        u,v,w =  graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent,v)

        if x != y:
            e += 1
            result.append([u,v,w])
            union(parent, rank, x, y)

    # make the mst in the adjacent list format
    v_w_list = []
    final_result = {}
    for u,v,w in result:
        v_w_list = [(vertex_dict_rev[v],w)]
        if vertex_dict_rev[u] not in final_result:
            final_result[vertex_dict_rev[u]] = v_w_list
        else:
            final_result[vertex_dict_rev[u]] = final_result[vertex_dict_rev[u]].append(v_w_list)

    return final_result

def question3(G):
    vertex_dict = {}
    vertex_dict_rev = {}
    
    # use number to represent vertex
    order = 0
    u,v,w = None, None, None
    graph = []
    for i in G:
        vertex_dict[i] = order
        vertex_dict_rev[order] = i
        order += 1

    for i in G:
        for j in G[i]:
            u,v,w = vertex_dict[i], vertex_dict[j[0]], j[1]
            graph.append([u,v,w])

    return MST(graph, order,vertex_dict_rev)


"""
Question 4

"""

def getParent(T, n):
    num_rows = len(T)
    for x in range(num_rows):
        if T[x][n] == 1:
            return x
def question4(T, r, n1, n2):
    ancestor = []
    while n1 != r:
        n1 = getParent(T, n1)
        ancestor.append(n1)
    if len(ancestor) == 0:
        return -1
    while n2 != r:
        n2 = getParent(T, n2)
        if n2 in ancestor:
            return n2
    return -1

"""
Question 5

"""

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(ll, m):
    #use two points fast and slow nodes , fast node advance m nodes first.
    fast = slow = ll
    for val in range(m):
        fast = fast.next
    if not fast:
        return None 
    # when fast is null, slow is the ith node from the end
    while fast.next:
        fast = fast.next
        slow = slow.next
    return slow.data

def main():
    #Test for question1
    print "TestCases for question 1"
    print question1("aba", "")
    print question1("udacity", "uda")
    print question1("", "")

    # Test for question2
    print "TestCases for quesion 2"
    print question2("ababcbabaadc")
    print question2("")
    print question2("a")


    # Test for question3
    graph1 = {'A':[('B',2)],'B':[('A',2),('C',5)],'C':[('B',5)]}
    graph2 = {}
    graph3 =  {'A':[('B', 1)], 'B': [('A', 1)]}
    print "TestCases for question 3"
    print question3(graph1)
    print question3(graph2)
    print question3(graph3)

    # Test for question 4
    print "TestCases for question 4"
    print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)
    print question4([[0,0,0],[1,0,1],[0,0,0]],1,0,2)
    print question4([[0,0,0],[1,0,0],[0,0,0]],1,0,0)

    #Test for question 5
    # make linkedlist 1->2->3->4
    ll = Node(1)
    ll.next= Node(2)
    ll.next.next = Node(3)
    ll.next.next.next = Node(4)
    print "TestCases for question 5"
    print question5(ll, 3)

    # make a LinkedList with only one node
    ll_2 = Node(30)
    print question5(ll_2, 1)

    # make an empty LinkedList
    ll_3 = Node(None)
    print question5(ll_3, 0)

if __name__ == '__main__':
    main()
