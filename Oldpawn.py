# import SPAWN
# import Open

# import turtle
# import time
# legal_moves=[]


# wpa=(1,2)
# wpb=(2,2)
# wpc=(3,2)
# wpd=(4,2)
# wpe=(5,2)
# wpf=(6,2)
# wpg=(7,2)
# wph=(8,2)

# bpa=(1,3)
# bpb=(2,7)
# bpc=(3,7)
# bpd=(4,7)
# bpe=(5,7)
# bpf=(6,7)
# bpg=(7,7)
# bph=(8,7)




# #Returns if there is a white pawn at this block
# def blackp(x):
#   if bpa==x or bpb==x or bpc==x or bpd==x or bpe==x or bpf==x or bpg==x or bph==x:
#     return (True)
#   else:
#     return (False)

# #Returns if there is a white pawn at this block
# def whitep(x):
#   if wpa==x or wpb==x or wpc==x or wpd==x or wpe==x or wpf==x or wpg==x or wph==x:
#     return (True)
#   else:
#     return (False)

# #Returns if there is a pawn at this block
# def block(x):
#   if bpa==x or bpb==x or bpc==x or bpd==x or bpe==x or bpf==x or bpg==x or bph==x or wpa==x or wpb==x or wpc==x or wpd==x or wpe==x or wpf==x or wpg==x or wph==x:
#     return (True)
#   else:
#     return (False)

# def wp(cordinates):
#   if block([cordinates[0],cordinates[1]+1])==False:
#       legal_moves.append([cordinates,[cordinates[0],cordinates[1]+1]])
#   if cordinates[1]==2:
#     if block([cordinates[0],cordinates[1]+1])==False and block([cordinates[0],cordinates[1]+2])==False:
#       legal_moves.append([cordinates,[cordinates[0],cordinates[1]+2]])
#   if blackp([cordinates[0]+1,cordinates[1]+1])==True:
#     legal_moves.append([cordinates,[cordinates[0]+1,cordinates[1]+1]])
#   if blackp([cordinates[0]-1,cordinates[1]+1])==True:
#     legal_moves.append([cordinates,[cordinates[0]-1,cordinates[1]+1]])


# def bp(cordinates):
#   if block([cordinates[0],cordinates[1]-1])==False:
#       legal_moves.append([cordinates,[cordinates[0],cordinates[1]-1]])
#   if cordinates[1]==7:
#     if block([cordinates[0],cordinates[1]-1])==False and block([cordinates[0],t[1]-2])==False:
#       legal_moves.append([cordinates,[cordinates[0],cordinates[1]-2]])
#   if whitep([cordinates[0]+1,cordinates[1]-1])==True:
#     legal_moves.append([cordinates,[cordinates[0]+1,cordinates[1]-1]])
#   if whitep([cordinates[0]-1,cordinates[1]-1])==True:
#     legal_moves.append([cordinates,[cordinates[0]-1,cordinates[1]-1]])
# def bm():
#   bp(bpa)
#   bp(bpb)
#   bp(bpc)
#   bp(bpd)
#   bp(bpe)
#   bp(bpf)
#   bp(bpg)
#   bp(bph)
# def wm():
#   wp(wpa)
#   wp(wpb)
#   wp(wpc)
#   wp(wpd)
#   wp(wpe)
#   wp(wpf)
#   wp(wpg)
#   wp(wph)

# #Set Pawn Positions



# #CORDINATE GRID
# #________________________________
# #|1,8|2,8|3,8|4,8|5,8|6,8|7,8|8,8|
# #--------------------------------|
# #|1,7|2,7|3,7|4,7|5,7|6,7|7,7|8,7|
# #--------------------------------|
# #|1,6|2,6|3,6|4,6|5,6|6,6|7,6|8,6|
# #--------------------------------|
# #|1,5|2,5|3,5|4,5|5,5|6,5|7,5|8,5|
# #--------------------------------|
# #|1,4|2,4|3,4|4,4|5,4|6,4|7,4|8,4|
# #--------------------------------|
# #|1,3|2,3|3,3|4,3|5,3|6,3|7,3|8,3|
# #--------------------------------|
# #|1,2|2,2|3,2|4,2|5,2|6,2|7,2|8,2|
# #--------------------------------|
# #|1,1|2,1|3,1|4,1|5,1|6,1|7,1|8,1|
# #--------------------------------|





