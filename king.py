import cordinates
import Open
#White king
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
def whiteKingLegalMoves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
	
	wk = wk
	kingx = wk[0]
	kingy = wk[1]
	newMoves = []
	newPos = (wk)
	legalk = []

	if kingx == 1:
		canMoveLeft = False
	else:
		canMoveLeft = True

	if kingx == 8:
		canMoveRight = False
	else:
		canMoveRight = True
	
	if kingy == 1:
		canMoveDown = False
	else:
		canMoveDown = True
	
	if kingy == 8:
		canMoveUp = False
	else:
		canMoveUp = True
	
	if canMoveLeft == True and canMoveUp == True:
		newPos = ((kingx-1), (kingy+1))
		x = newPos[0]
		y = newPos[1]

		if False == Open.isblockedw(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh):
			legalk.append(wk)
			legalk.append(newPos)
			
	if canMoveRight == True and canMoveUp == True:
		newPos = ((kingx+1), (kingy+1))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedw(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh):
			legalk.append(wk)
			legalk.append(newPos)
	if canMoveLeft == True and canMoveDown == True:
		newPos = ((kingx-1), (kingy-1))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedw(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh):
			legalk.append(wk)
			legalk.append(newPos)
	if canMoveRight == True and canMoveDown == True:
		newPos = ((kingx+1), (kingy-1))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedw(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh):
			
			legalk.append(wk)
			legalk.append(newPos)
	if canMoveLeft == True:
		newPos = ((kingx-1), (kingy))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedw(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh):
			legalk.append(wk)
			legalk.append(newPos)
	if canMoveRight == True:
		newPos = ((kingx+1), (kingy))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedw(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh):
			legalk.append(wk)
			legalk.append(newPos)
	if canMoveUp == True:
		newPos = (kingx), (kingy+1)
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedw(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh):
			legalk.append(wk)
			legalk.append(newPos)
	if canMoveDown == True:
		newPos = ((kingx), (kingy-1))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedw(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh):
			legalk.append(wk)
			legalk.append(newPos)
	return(legalk)



	



def blackKingLegalMoves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
	
	bk = bk
	kingx = bk[0]
	kingy = bk[1]
	newMoves = []
	newPos = (bk)
	legalk = []
	

	if kingx == 1:
		canMoveLeft = False
	else:
		canMoveLeft = True

	if kingx == 8:
		canMoveRight = False
	else:
		canMoveRight = True
	
	if kingy == 1:
		canMoveDown = False
	else:
		canMoveDown = True
	
	if kingy == 8:
		canMoveUp = False
	else:
		canMoveUp = True
	
	if canMoveLeft == True and canMoveUp == True:
		newPos = ((kingx-1), (kingy+1))
		x = newPos[0]
		y = newPos[1]

		if False == Open.isblockedb(x,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh):

			legalk.append(bk)
			legalk.append(newPos)
			
	if canMoveRight == True and canMoveUp == True:
		newPos = ((kingx+1), (kingy+1))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedb(x,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh):
			
			legalk.append(bk)
			legalk.append(newPos)
	if canMoveLeft == True and canMoveDown == True:
		newPos = ((kingx-1), (kingy-1))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedb(x,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh):
			legalk.append(bk)
			legalk.append(newPos)
	if canMoveRight == True and canMoveDown == True:
		newPos = ((kingx+1), (kingy-1))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedb(x,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh):
			
			legalk.append(bk)
			legalk.append(newPos)
	if canMoveLeft == True:
		newPos = ((kingx-1), (kingy))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedb(x,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh):
			legalk.append(bk)
			legalk.append(newPos)
	if canMoveRight == True:
		newPos = ((kingx+1), (kingy))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedb(x,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh):
			legalk.append(bk)
			legalk.append(newPos)
	if canMoveUp == True:
		newPos = ((kingx), (kingy+1))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedb(x,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh):
			legalk.append(bk)
			legalk.append(newPos)
	if canMoveDown == True:
		newPos = ((kingx), (kingy-1))
		x = newPos[0]
		y = newPos[1]
		if False == Open.isblockedb(x,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh):
			legalk.append(bk)
			legalk.append(newPos)
	return(legalk)






