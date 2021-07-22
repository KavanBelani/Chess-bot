import Open
import SPAWN
import cordinates
import turtle
import cordinates
pen=turtle.Turtle()
#creates turtle called pen
turtle.tracer(0,0)
#allows turtle to draw faster
turtle.width(2)
index=0
possiblemoves=[]
cords = cordinates.getValues()
wpa=cords[0]
wpb=cords[1]
wpc=cords[2]
wpd=cords[3]
wpe=cords[4]
wpf=cords[5]
wpg=cords[6]
wph=cords[7]
wra=cords[16]
wnb=cords[26]
wbc=cords[28]
wq=cords[20]
wk=cords[22]
wbf=cords[29]
wng=cords[27]
wrh=cords[17]

bpa=cords[8]
bpb=cords[9]
bpc=cords[10]
bpd=cords[11]
bpe=cords[12]
bpf=cords[13]
bpg=cords[14]
bph=cords[15]
bra=cords[18]
bnb=cords[25]
bbc=cords[30]
bq=cords[21]
bk=cords[23]
bbf=cords[31]
bng=cords[24]
brh=cords[19]

#finds legal moves for both colored pawns with input of which index in list of pieces
def pawns(piece):
	cords = cordinates.getValues()
	wpa=cords[0]
	wpb=cords[1]
	wpc=cords[2]
	wpd=cords[3]
	wpe=cords[4]
	wpf=cords[5]
	wpg=cords[6]
	wph=cords[7]
	wra=cords[16]
	wnb=cords[26]
	wbc=cords[28]
	wq=cords[20]
	wk=cords[22]
	wbf=cords[29]
	wng=cords[27]
	wrh=cords[17]
	bpa=cords[8]
	bpb=cords[9]
	bpc=cords[10]
	bpd=cords[11]
	bpe=cords[12]
	bpf=cords[13]
	bpg=cords[14]
	bph=cords[15]
	bra=cords[18]
	bnb=cords[25]
	bbc=cords[30]
	bq=cords[21]
	bk=cords[23]
	bbf=cords[31]
	bng=cords[24]
	brh=cords[19]
	
	possiblemoves=[]
	piecespos=[wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph, wra,wnb,wbc,wq,wk,wbf,wng,wrh,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh]
	
	piecesname=["wpa","wpb","wpc","wpd","wpe","wpf","wpg","wph", "wra","wnb","wbc","wq","wk","wbf","wng","wrh","bpa","bpb","bpc","bpd","bpe","bpf","bpg","bph","bra","bnb", "bbc","bq","bk","bbf","bng","brh"]
	for k in range(1):
		currentpiecetype=piecesname[piece]
		currentpiecepos=piecespos[piece]
		if currentpiecetype[1]=="p":
			pawn=True
		else:
		  pawn=False
		if currentpiecetype[0]=="b":
			black=True
			white=False
		else:
			white=True
			black=False
		#checks if forward 1 and 2, left and right diagonal occupied by black or white piece. Seperate for black and white because diagonals depend on color for pawns.
		if white == True and pawn == True:
			
			blockedfrontw=Open.isblockedw(currentpiecepos[0],currentpiecepos[1]+1,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)
			blockedfrontb=Open.isblockedb(currentpiecepos[0],currentpiecepos[1]+1
			,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)
			blockeddiagonalrw=Open.isblockedw(currentpiecepos[0]+1,currentpiecepos[1]+1,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)
			blockeddiagonalrb=Open.isblockedb(currentpiecepos[0]+1,currentpiecepos[1]+1,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)
			blockeddiagonallw=Open.isblockedw(currentpiecepos[0]-1,currentpiecepos[1]+1,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)
			blockeddiagonallb=Open.isblockedb(currentpiecepos[0]-1,currentpiecepos[1]+1,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)
			blockedfrontw2=Open.isblockedw(currentpiecepos[0],currentpiecepos[1]+2,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)
			blockedfrontb2=Open.isblockedb(currentpiecepos[0],currentpiecepos[1]+2,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)
		if black == True and pawn== True:  
			blockedfrontw2=Open.isblockedw(currentpiecepos[0],currentpiecepos[1]-2,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)
			blockedfrontb2=Open.isblockedb(currentpiecepos[0],currentpiecepos[1]-2,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)
			blockeddiagonalrw=Open.isblockedw(currentpiecepos[0]+1,currentpiecepos[1]-1,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)
			blockeddiagonalrb=Open.isblockedb(currentpiecepos[0]+1,currentpiecepos[1]-1,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)
			blockedfrontw=Open.isblockedw(currentpiecepos[0],currentpiecepos[1]-1,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)
			blockedfrontb=Open.isblockedb(currentpiecepos[0],currentpiecepos[1]-1,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)
			blockeddiagonallw=Open.isblockedw(currentpiecepos[0]-1,currentpiecepos[1]-1,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)
			blockeddiagonallb=Open.isblockedb(currentpiecepos[0]-1,currentpiecepos[1]-1,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)
		#checks if forward 1 is clear
		if blockedfrontb == False and blockedfrontw==False and currentpiecepos[1]!=8:
		  front1clear=True
		  possiblemoves.append(1)
		else:
		  front1clear=False
		#checks if forwards 2 is clear and at starting pos.
		if blockedfrontb2 == False and blockedfrontw2==False and front1clear==True and (currentpiecepos[1]==2and white ==True)or(currentpiecepos[1]==7and black == True):
			 front2clear=True
			 possiblemoves.append(2)
		else:
		    front2clear=False
		#checks diagonals, depends on color for taking pieces.
		if black==True:
		  if blockeddiagonallb==False and blockeddiagonallw==True:
		    possiblemoves.append(4)
		  if blockeddiagonalrb==False and blockeddiagonalrw==True:
		    possiblemoves.append(3)
		if white==True:
		  if blockeddiagonallb==True and blockeddiagonallw==False:
		    possiblemoves.append(4)
		  if blockeddiagonalrb==True and blockeddiagonalrw==False:
		    possiblemoves.append(3)
		else:
			possiblemoves.append(0)
		return possiblemoves
		
#finds coordinates of legal moves for black pawns from functions	
def blackpawn():
  cords = cordinates.getValues()
  wpa=cords[0]
  wpb=cords[1]
  wpc=cords[2]
  wpd=cords[3]
  wpe=cords[4]
  wpf=cords[5]
  wpg=cords[6]
  wph=cords[7]
  wra=cords[16]
  wnb=cords[26]
  wbc=cords[28]
  wq=cords[20]
  wk=cords[22]
  wbf=cords[29]
  wng=cords[27]
  wrh=cords[17]
  bpa=cords[8]
  bpb=cords[9]
  bpc=cords[10]
  bpd=cords[11]
  bpe=cords[12]
  bpf=cords[13]
  bpg=cords[14]
  bph=cords[15]
  bra=cords[18]
  bnb=cords[25]
  bbc=cords[30]
  bq=cords[21]
  bk=cords[23]
  bbf=cords[31]
  bng=cords[24]
  brh=cords[19]
  pieces=[wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph, wra,wnb,wbc,wq,wk,wbf,wng,wrh,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh]
  bpawnlist=[]
  for i in range(8):
    answer=pawns(i+16)
    if 4 in answer:
      if i == 0:
    	  bpawnlist.append(bpa)
    	  new=(bpa[0]-1,bpa[1]-1)
    	  bpawnlist.append(new)
      if i == 1:
    	  bpawnlist.append(bpb)
    	  new=(bpb[0]-1,bpb[1]-1)
    	  bpawnlist.append(new)
      if i == 2:
    	  bpawnlist.append(bpc)
    	  new=(bpc[0]-1,bpc[1]-1)
    	  bpawnlist.append(new)
      if i == 3:
    	  bpawnlist.append(bpd)
    	  new=(bpd[0]-1,bpd[1]-1)
    	  bpawnlist.append(new)
      if i == 4:
    	  bpawnlist.append(bpe)
    	  new=(bpe[0]-1,bpe[1]-1)
    	  bpawnlist.append(new)
      if i == 5:
    	  bpawnlist.append(bpf)
    	  new=(bpf[0]-1,bpf[1]-1)
    	  bpawnlist.append(new)
      if i == 6:
    	  bpawnlist.append(bpg)
    	  new=(bpg[0]-1,bpg[1]-1)
    	  bpawnlist.append(new)
      if i == 7:
    	  bpawnlist.append(bph)
    	  new=(bph[0]-1,bph[1]-1)
    	  bpawnlist.append(new)
    if 3 in answer:
      if i == 0:
    	  bpawnlist.append(bpa)
    	  new=(bpa[0]+1,bpa[1]-1)
    	  bpawnlist.append(new)
      if i == 1:
    	  bpawnlist.append(bpb)
    	  new=(bpb[0]+1,bpb[1]-1)
    	  bpawnlist.append(new)
      if i == 2:
    	  bpawnlist.append(bpc)
    	  new=(bpc[0]+1,bpc[1]-1)
    	  bpawnlist.append(new)
      if i == 3:
    	  bpawnlist.append(bpd)
    	  new=(bpd[0]+1,bpd[1]-1)
    	  bpawnlist.append(new)
      if i == 4:
    	  bpawnlist.append(bpe)
    	  new=(bpe[0]+1,bpe[1]-1)
    	  bpawnlist.append(new)
      if i == 5:
    	  bpawnlist.append(bpf)
    	  new=(bpf[0]+1,bpf[1]-1)
    	  bpawnlist.append(new)
      if i == 6:
    	  bpawnlist.append(bpg)
    	  new=(bpg[0]+1,bpg[1]-1)
    	  bpawnlist.append(new)
      if i == 7:
    	  bpawnlist.append(bph)
    	  new=(bph[0]+1,bph[1]-1)
    	  bpawnlist.append(new)
    if 2 in answer:
      if i == 0:
    	  bpawnlist.append(bpa)
    	  new=(bpa[0],bpa[1]-2)
    	  bpawnlist.append(new)
      if i == 1:
    	  bpawnlist.append(bpb)
    	  new=(bpb[0],bpb[1]-2)
    	  bpawnlist.append(new)
      if i == 2:
    	  bpawnlist.append(bpc)
    	  new=(bpc[0],bpc[1]-2)
    	  bpawnlist.append(new)
      if i == 3:
    	  bpawnlist.append(bpd)
    	  new=(bpd[0],bpd[1]-2)
    	  bpawnlist.append(new)
      if i == 4:
    	  bpawnlist.append(bpe)
    	  new=(bpe[0],bpe[1]-2)
    	  bpawnlist.append(new)
      if i == 5:
    	  bpawnlist.append(bpf)
    	  new=(bpf[0],bpf[1]-2)
    	  bpawnlist.append(new)
      if i == 6:
    	  bpawnlist.append(bpg)
    	  new=(bpg[0],bpg[1]-2)
    	  bpawnlist.append(new)
      if i == 7:
    	  bpawnlist.append(bph)
    	  new=(bph[0],bph[1]-2)
    	  bpawnlist.append(new)
    if 1 in answer:
    	if i == 0:
    	  bpawnlist.append(bpa)
    	  new=(bpa[0],bpa[1]-1)
    	  bpawnlist.append(new)
    	if i == 1:
    	  bpawnlist.append(bpb)
    	  new=(bpb[0],bpb[1]-1)
    	  bpawnlist.append(new)
    	if i == 2:
    	  bpawnlist.append(bpc)
    	  new=(bpc[0],bpc[1]-1)
    	  bpawnlist.append(new)
    	if i == 3:
    	  bpawnlist.append(bpd)
    	  new=(bpd[0],bpd[1]-1)
    	  bpawnlist.append(new)
    	if i == 4:
    	  bpawnlist.append(bpe)
    	  new=(bpe[0],bpe[1]-1)
    	  bpawnlist.append(new)
    	if i == 5:
    	  bpawnlist.append(bpf)
    	  new=(bpf[0],bpf[1]-1)
    	  bpawnlist.append(new)
    	if i == 6:
    	  bpawnlist.append(bpg)
    	  new=(bpg[0],bpg[1]-1)
    	  bpawnlist.append(new)
    	if i == 7:
    	  bpawnlist.append(bph)
    	  new=(bph[0],bph[1]-1)
    	  bpawnlist.append(new)
  
  turtle.penup()
  move=0
  turtle.width(4)
  for i in range(len(bpawnlist)//2):
    turtle.color("red")
    #print(pawnlist[move])
    coordinate=bpawnlist[move]
    turtle.goto((coordinate[0]*40-182,coordinate[1]*40-177))
    turtle.pendown()
    move+=1
    coordinate=bpawnlist[move]
    turtle.goto((coordinate[0]*40-182,coordinate[1]*40-177))
    turtle.penup()
    move+=1
  
  return bpawnlist
#finds coordinates of legal moves for white pawns from functions	  
def whitepawn():
  cords = cordinates.getValues()
  wpa=cords[0]
  wpb=cords[1]
  wpc=cords[2]
  wpd=cords[3]
  wpe=cords[4]
  wpf=cords[5]
  wpg=cords[6]
  wph=cords[7]
  wra=cords[16]
  wnb=cords[26]
  wbc=cords[28]
  wq=cords[20]
  wk=cords[22]
  wbf=cords[29]
  wng=cords[27]
  wrh=cords[17]
  bpa=cords[8]
  bpb=cords[9]
  bpc=cords[10]
  bpd=cords[11]
  bpe=cords[12]
  bpf=cords[13]
  bpg=cords[14]
  bph=cords[15]
  bra=cords[18]
  bnb=cords[25]
  bbc=cords[30]
  bq=cords[21]
  bk=cords[23]
  bbf=cords[31]
  bng=cords[24]
  brh=cords[19]
  pieces=[wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph, wra,wnb,wbc,wq,wk,wbf,wng,wrh,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh]
  wpawnlist=[]
  for i in range(8):
    answer=pawns(i)
    if 4 in answer:
      if i == 0:
    	  wpawnlist.append(wpa)
    	  new=(wpa[0]-1,wpa[1]+1)
    	  wpawnlist.append(new)
      if i == 1:
    	  wpawnlist.append(wpb)
    	  new=(wpb[0]-1,wpb[1]+1)
    	  wpawnlist.append(new)
      if i == 2:
    	  wpawnlist.append(wpc)
    	  new=(wpc[0]-1,wpc[1]+1)
    	  wpawnlist.append(new)
      if i == 3:
    	  wpawnlist.append(wpd)
    	  new=(wpd[0]-1,wpd[1]+1)
    	  wpawnlist.append(new)
      if i == 4:
    	  wpawnlist.append(wpe)
    	  new=(wpe[0]-1,wpe[1]+1)
    	  wpawnlist.append(new)
      if i == 5:
    	  wpawnlist.append(wpf)
    	  new=(wpf[0]-1,wpf[1]+1)
    	  wpawnlist.append(new)
      if i == 6:
    	  wpawnlist.append(wpg)
    	  new=(wpg[0]-1,wpg[1]+1)
    	  wpawnlist.append(new)
      if i == 7:
    	  wpawnlist.append(wph)
    	  new=(wph[0]-1,wph[1]+1)
    	  wpawnlist.append(new)
    if 3 in answer:
      if i == 0:
    	  wpawnlist.append(wpa)
    	  new=(wpa[0]+1,wpa[1]+1)
    	  wpawnlist.append(new)
      if i == 1:
    	  wpawnlist.append(wpb)
    	  new=(wpb[0]+1,wpb[1]+1)
    	  wpawnlist.append(new)
      if i == 2:
    	  wpawnlist.append(wpc)
    	  new=(wpc[0]+1,wpc[1]+1)
    	  wpawnlist.append(new)
      if i == 3:
    	  wpawnlist.append(wpd)
    	  new=(wpd[0]+1,wpd[1]+1)
    	  wpawnlist.append(new)
      if i == 4:
    	  wpawnlist.append(wpe)
    	  new=(wpe[0]+1,wpe[1]+1)
    	  wpawnlist.append(new)
      if i == 5:
    	  wpawnlist.append(wpf)
    	  new=(wpf[0]+1,wpf[1]+1)
    	  wpawnlist.append(new)
      if i == 6:
    	  wpawnlist.append(wpg)
    	  new=(wpg[0]+1,wpg[1]+1)
    	  wpawnlist.append(new)
      if i == 7:
    	  wpawnlist.append(wph)
    	  new=(wph[0]+1,wph[1]+1)
    	  wpawnlist.append(new)
    if 2 in answer:
      if i == 0:
    	  wpawnlist.append(wpa)
    	  new=(wpa[0],wpa[1]+2)
    	  wpawnlist.append(new)
      if i == 1:
    	  wpawnlist.append(wpb)
    	  new=(wpb[0],wpb[1]+2)
    	  wpawnlist.append(new)
      if i == 2:
    	  wpawnlist.append(wpc)
    	  new=(wpc[0],wpc[1]+2)
    	  wpawnlist.append(new)
      if i == 3:
    	  wpawnlist.append(wpd)
    	  new=(wpd[0],wpd[1]+2)
    	  wpawnlist.append(new)
      if i == 4:
    	  wpawnlist.append(wpe)
    	  new=(wpe[0],wpe[1]+2)
    	  wpawnlist.append(new)
      if i == 5:
    	  wpawnlist.append(wpf)
    	  new=(wpf[0],wpf[1]+2)
    	  wpawnlist.append(new)
      if i == 6:
    	  wpawnlist.append(wpg)
    	  new=(wpg[0],wpg[1]+2)
    	  wpawnlist.append(new)
      if i == 7:
    	  wpawnlist.append(wph)
    	  new=(wph[0],wph[1]+2)
    	  wpawnlist.append(new)
    if 1 in answer:
    	if i == 0:
    	  wpawnlist.append(wpa)
    	  new=(wpa[0],wpa[1]+1)
    	  wpawnlist.append(new)
    	if i == 1:
    	  wpawnlist.append(wpb)
    	  new=(wpb[0],wpb[1]+1)
    	  wpawnlist.append(new)
    	if i == 2:
    	  wpawnlist.append(wpc)
    	  new=(wpc[0],wpc[1]+1)
    	  wpawnlist.append(new)
    	if i == 3:
    	  wpawnlist.append(wpd)
    	  new=(wpd[0],wpd[1]+1)
    	  wpawnlist.append(new)
    	if i == 4:
    	  wpawnlist.append(wpe)
    	  new=(wpe[0],wpe[1]+1)
    	  wpawnlist.append(new)
    	if i == 5:
    	  wpawnlist.append(wpf)
    	  new=(wpf[0],wpf[1]+1)
    	  wpawnlist.append(new)
    	if i == 6:
    	  wpawnlist.append(wpg)
    	  new=(wpg[0],wpg[1]+1)
    	  wpawnlist.append(new)
    	if i == 7:
    	  wpawnlist.append(wph)
    	  new=(wph[0],wph[1]+1)
    	  wpawnlist.append(new)
  move=0
  turtle.penup()
  turtle.width(1)
  for i in range(len(wpawnlist)//2):
    turtle.color("green")
    #print(pawnlist[move])
    coordinate=wpawnlist[move]
    turtle.goto((coordinate[0]*40-181,coordinate[1]*40-177))
    turtle.pendown()
    move+=1
    coordinate=wpawnlist[move]
    turtle.goto((coordinate[0]*40-181,coordinate[1]*40-177))
    turtle.penup()
    move+=1
  return wpawnlist  
