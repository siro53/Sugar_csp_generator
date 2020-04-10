# 9*9の数独


def main():
    with open("in.txt", "r") as f:
        lines = f.readlines()
    g = []
    for s in lines:
        line = s.split(" ")
        for i in range(len(line)):
            line[i] = int(line[i])
        g.append(line)

    with open("suudoku-9-9.csp", "w") as f:
        # まず盤面の制約を書き込む
        for i in range(9):
            for j in range(9):
                if g[i][j] == 0:
                    f.write('(int x_{0}_{1} 1 9)\n'.format(i, j))
                else:
                    f.write('(int x_{0}_{1} {2} {3})\n'.format(
                        i, j, g[i][j], g[i][j]))
        # タテ列の制約を書き込む
        for i in range(9):
            text = "(alldifferent "
            for j in range(9):
                text += "x_{0}_{1}".format(i, j)
                if j < 8:
                    text += " "
            text += ")\n"
            f.write(text)
        # ヨコ列の制約を書き込む
        for i in range(9):
            text = "(alldifferent "
            for j in range(9):
                text += "x_{0}_{1}".format(j, i)
                if j < 8:
                    text += " "
            text += ")\n"
            f.write(text)
        # 3*3のブロックの制約を書き込む
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                text = "(alldifferent "
                for dy in range(3):
                    for dx in range(3):
                        ni = i + dy
                        nj = j + dx
                        text += "x_{0}_{1}".format(ni, nj)
                        if dx < 2 or dy < 2:
                            text += " "
                text += ")\n"
                f.write(text)


main()
