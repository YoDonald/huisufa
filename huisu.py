#回溯法，根据货物体积约束&价值，求初始方案，若亦满足托盘重量限制，则输出。

def bag(n, c, w, v):
    res = [[-1 for j in range(c + 1)] for i in range(n + 1)]
    for j in range(c + 1):
        res[0][j] = 0
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            res[i][j] = res[i - 1][j]
            if j >= w[i - 1] and res[i][j] < res[i - 1][j - w[i - 1]] + v[i - 1]:
                res[i][j] = res[i - 1][j - w[i - 1]] + v[i - 1]
    return res


def show(n, c, w, res):
    print('最大价值为:', res[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(1, n + 1):
        if res[i][j] > res[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('选择的物品为:')
    for i in range(n):
        if x[i]:
            print('第', i, '个,', end='')
    print('')


if __name__ == '__main__':
    n = 32 #n为物品的数量
    c = 50000 #背包重量约束
    w = [2582,2182,1650,580,2971,2922,2443,2096,1347,2132,2893,1650,580,620,
2971,2922,2909,1622,2595,1270,2036,1500,2100,1761,2443,2096,620,2286,2036,1500,2100,812,2582,2182,2922,2971,2443,2182,2286]#货物重量
    v = [1,2,2,2,1,2,1,2,1,1,2,2,1,2,1,1,2,2,1,1,21,2,1,2,1,1,2,1,1,1,2,1,12,2,1,1,2,2]#货物体积
    #问题是，如何确立货物的价值？
    res = bag(n, c, w, v)
    show(n, c, w, res)

#去除掉已经取出来的货物，无放回的再筛选一波。