"""
    克鲁斯卡算法
    算法思路：
    （1）将图中的所有边都去掉。
    （2）将边按权值从小到大的顺序添加到图中，保证添加的过程中不会形成环
    （3）重复上一步直到连接所有顶点，此时就生成了最小生成树。这是一种贪心策略。
"""
def getVE(G):
    V = [v for v in G]
    E = []
    for v in V:
        for e in G[v]:
            u = e[0]
            w = e[1]
            if (u,v,w) not in E and (v,u,w) not in E:
                E.append((u,v,w))
    return V,E

def kruskal(G):
    V,E  = getVE(G)
    forest = [{v} for v in V]
    E.sort(key=lambda e:e[2])
    mst_e, min_weight = [], 0

    for e in E:
        # 判断e的两个端点是否在同一棵树上
        # 如果不在，则联合这两棵树
        for tree in forest:
            if e[0] in tree:
                tree_left = tree
                break
        for tree in forest:
            if e[1] in tree:
                tree_right = tree
                break
        if tree_left != tree_right:
            mst_e.append(e)
            min_weight += e[2]
            forest.remove(tree_right)
            forest.remove(tree_left)
            forest.append(tree_left.union(tree_right))
            if len(forest) == 1:
                break
    return mst_e, min_weight


def test():
    G = {
        'v1': [('v2', 6), ('v3', 1), ('v4', 5)],
        'v2': [('v1', 6), ('v3', 5), ('v5', 3)],
        'v3': [('v1', 1), ('v2', 5), ('v4', 5), ('v5', 6), ('v6', 4)],
        'v4': [('v1', 5), ('v3', 5), ('v6', 2)],
        'v5': [('v2', 3), ('v3', 6), ('v6', 6)],
        'v6': [('v3', 4), ('v4', 2), ('v5', 6)]
    }
    E,min_weight = kruskal(G)
    print(E)
    print(min_weight)

if __name__ == '__main__':
    test()
