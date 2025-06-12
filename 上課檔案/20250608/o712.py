# #wall & bound

# M,N,k,r,c = map(int, input().split)
# game_map = [list(map(int, input().split())) for _ in range(M)]
# d = [
#     [0,1],#right
#     [1,0],#down
#     [0,-1],#left
#     [-1,0]#up
# ]
# d_index = 0
# rob_y, rob_x = r, c

# score = 0

# def move(rob_y, rob_x, d_index):
#     #out
#     if (rob_y + d[d_index][0] >= M) or (rob_x + d[d_index][1] >= N):
#         #turn right
#         move(rob_y, rob_x, d_index)
#     #wall
#     elif (game_map[rob_y + d[d_index][0]][rob_x + d[d_index][1]]) == -1:
#         #turn right
#         move(move(rob_y, rob_x, d_index))
#     else:
#         return rob_y, rob_x, d_index
    
# while True:
#     #rule 1
#     if game_map[rob_y][rob_x] == 0:
#         break
#     #rule 2
#     score += game_map[rob_y][rob_x]
#     game_map[rob_y][rob_x] -= 1
#     #rule 3
#     if (score % k) == 0:
#         #turn right
#     #rule 4
#     rob_y, rob_x, d_index = move(rob_y, rob_x, d_index)
    