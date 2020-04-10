def main():
    with open("in.txt", "r") as f:
        lines = f.readlines()
    g = []
    flg = True
    for s in lines:
        if flg:
            flg = False
            continue
        line = s.split(" ")
        if len(line) == 2:
            g.append(line[1].split("\t"))

    ans = [[0 for i in range(9)] for j in range(9)]
    for a in range(81):
        i = a // 9
        j = a % 9
        ans[i][j] = int(g[a][1])

    with open("out.txt", "w") as f:
        for i in range(9):
            for j in range(9):
                f.write(str(ans[i][j]) + " ")
            f.write("\n")


main()
