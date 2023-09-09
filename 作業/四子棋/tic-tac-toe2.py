import random

# Define constants
EMPTY = '-'
X = 'X'
O = 'O'
TIE = 'TIE'

def alpha_beta(board, player, alpha, beta, depth, recent_i, recent_j):
    # 檢查終止條件
    score = evaluate(board, player)
    if depth == 0 or score == float("inf") or score == float("-inf"):
        return (score*-1, recent_i, recent_j) if player == 'O' else (score, recent_i, recent_j)
    # 定義初始值
    best_score = float("-inf") if player == 'X' else float("inf")
    # 每個可用的位置都嘗試
    best_i, best_j = 0, 0
    for i in range(6):
        for j in range(6):
            if board[i][j] == '-':
                board[i][j] = player
                # 遞迴呼叫alpha-beta函數以搜索下一個狀態
                if player == 'X':
                    maxv, resp_i, resp_j = alpha_beta(board, 'O', alpha, beta, depth-1, i, j)
                    if best_score >  maxv:
                        best_i, best_j = i, j
                    best_score = max(best_score, maxv)
                    alpha = max(alpha, best_score)
                else:
                    minv, resp_i, resp_j = alpha_beta(board, 'X', alpha, beta, depth-1, i, j)
                    if best_score <  minv:
                        best_i, best_j = i, j
                    best_score = min(best_score, minv)
                    beta = min(beta, best_score)
                # 恢復原始狀態
                board[i][j] = '-'
                # alpha-beta剪枝
                if alpha >= beta:
                    return (best_score, best_i, best_j)
    return (best_score, best_i, best_j)
    
def evaluate(board, player):
    # 定義各種情況的權重
    row_weight = 1
    col_weight = 1
    diag_weight = 1
    diag_weight = 1
    # 檢查row中是否有4個連續標記
    score = 0
    for i in range(6):
        for j in range(3):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                score += row_weight
    # 檢查colume中是否有4個連續標記
    for i in range(3):
        for j in range(6):
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
                score += col_weight
    # 檢查對角線中是否有4個連續標記
    for i in range(3):
        for j in range(3, 6):
            if board[i][j] == player and board[i+1][j-1] == player and board[i+2][j-2] == player and board[i+3][j-3] == player:
                score += diag_weight
    # 檢查對角線2中是否有4個連續標記
    for i in range(3):
        for j in range(3):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                score += diag_weight
    return score

def get_next_move(board, real_player, computer_player):
    # 定義初始值
    best_score = float("-inf") if real_player == 'X' else float("inf")
    best_move = None
    loss = []
    step = []
    check = False
    # 每個可用的位置都計算得分，如果較佳就記錄該位置
    for i in range(6):
        for j in range(6):
            if board[i][j] == '-':
                board[i][j] = computer_player
                score, next_step_i, next_step_j = alpha_beta(board, real_player, float("-inf"), float("inf"), 4, 0, 0)
                loss.append(score)
                step.append([i, j])
                print([i, j])
                print(score, next_step_i, next_step_j)
                if real_player == 'X' and score > best_score:
                    best_score = score
                    check = True
                elif real_player == 'O' and score < best_score:
                    best_score = score
                    check = True
                board[i][j] = '-'
    if check:
        if real_player == "X":
            best_move = step[loss.index(min(loss))][0], step[loss.index(min(loss))][1]
        else:
            best_move = step[loss.index(max(loss))][0], step[loss.index(max(loss))][1]
    else:
        score, next_step_i, next_step_j = alpha_beta(board, real_player, float("-inf"), float("inf"), 4, 0, 0)
        best_move = next_step_i, next_step_j
    return best_move

# 初始化棋盤
def init_board():
    board = [[EMPTY for i in range(6)] for j in range(6)]
    return board

# 印出當前棋盤狀態
def print_board(board):
    for i in range(6):
        print(' '.join(board[i]))

# 檢查是否存在空位置
def has_empty(board):
    for row in board:
        if EMPTY in row:
            return True
    return False

# 檢查是否有4個連續標記
def check_win(board, player):
    # 檢查row
    for i in range(6):
        for j in range(3):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True
    # 檢查colume
    for i in range(3):
        for j in range(6):
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
                return True
    # 檢查對角線
    for i in range(3):
        for j in range(3):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True
    # 檢查對角線2
    for i in range(3):
        for j in range(3, 6):
            if board[i][j] == player and board[i+1][j-1] == player and board[i+2][j-2] == player and board[i+3][j-3] == player:
                return True
    return False

# 遊戲流程
def main():
    board = init_board()
    lots = random.randint(1,2)
    computer_player = ""
    real_player = ""
    if lots == 1:
        print(f"遊戲開始，玩家先手。")
        computer_player = X
        real_player = O
    elif lots == 2:
        print(f"遊戲開始，電腦先手。")
        computer_player = O
        real_player = X
    turn = O
    while has_empty(board) and not check_win(board, computer_player) and not check_win(board, real_player):
        print_board(board)
        if turn == real_player:
            row = int(input("玩家請在0-5之間輸入要落子的列："))
            col = int(input("玩家請在0-5之間輸入要落子的欄："))
            if board[row][col] == EMPTY:
                board[row][col] = turn
                turn = computer_player
            else:
                print("該位置已有棋子，請重新輸入。")
        else:
            print("電腦的回合。")
            # 呼叫alpha-beta函數進行搜索
            i, j = get_next_move(board, real_player, computer_player)
            board[i][j] = computer_player
            turn = real_player
    if check_win(board, computer_player):
        print("電腦獲勝！")
        print_board(board)
    elif check_win(board, real_player):
        print("恭喜玩家獲勝！")
        print_board(board)
    else:
        print("平局！")
        print_board(board)

if __name__ == "__main__":
    main()
