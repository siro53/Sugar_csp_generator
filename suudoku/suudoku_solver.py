import sys
import copy
sys.setrecursionlimit(1000000)


def solve(board, ans):
    # 空きマスの探索
    now_i, now_j = -1, -1
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                now_i, now_j = i, j
                break
    if now_i == -1 or now_j == -1:
        ans.append(copy.deepcopy(board))
        return

    # num[i] := 数字iを(now_i, now_j)に置いてもいいかどうか
    num = [True for _ in range(10)]
    for i in range(9):
        # 列
        if board[now_i][i] != 0:
            num[board[now_i][i]] = False
        # 行
        if board[i][now_j] != 0:
            num[board[i][now_j]] = False
        # ブロック
        center_i, center_j = (now_i // 3) * 3 + 1, (now_j // 3) * 3 + 1
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if board[center_i + di][center_j + dj] != 0:
                    num[board[center_i + di][center_j + dj]] = False

    for i in range(1, 10):
        if num[i] == True:
            board[now_i][now_j] = i
            solve(board, ans)
    board[now_i][now_j] = 0


def main():
    with open("in.txt", "r") as f:
        lines = f.readlines()

    board, ans = [], []
    for s in lines:
        line = s.split(" ")
        for i in range(len(line)):
            line[i] = int(line[i])
        board.append(line)

    solve(board, ans)

    with open("out.txt", "w") as f:
        if len(ans) == 0:
            f.write("No Answer.")
        else:
            for i in range(9):
                for j in range(9):
                    f.write(str(ans[0][i][j]) + " ")
                f.write("\n")


main()
