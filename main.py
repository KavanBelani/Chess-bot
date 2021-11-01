import cordinates

cordinates.assignValues()
movesnotcrashed = 0
import os
os.system('clear')
import Bestmove
import Legalm
import SPAWN
import cordinates
cords = cordinates.getValues()
wpa = cords[0]
wpb = cords[1]
wpc = cords[2]
wpd = cords[3]
wpe = cords[4]
wpf = cords[5]
wpg = cords[6]
wph = cords[7]
wra = cords[16]
wnb = cords[26]
wbc = cords[28]
wq = cords[20]
wk = cords[22]
wbf = cords[29]
wng = cords[27]
wrh = cords[17]
bpa = cords[8]
bpb = cords[9]
bpc = cords[10]
bpd = cords[11]
bpe = cords[12]
bpf = cords[13]
bpg = cords[14]
bph = cords[15]
bra = cords[18]
bnb = cords[25]
bbc = cords[30]
bq = cords[21]
bk = cords[23]
bbf = cords[31]
bng = cords[24]
brh = cords[19]
SPAWN.draw(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
SPAWN.draw(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,
bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
for i in range(50):
	cordinates.usermove()
	cords = cordinates.getValues()
	wpa = cords[0]
	wpb = cords[1]
	wpc = cords[2]
	wpd = cords[3]
	wpe = cords[4]
	wpf = cords[5]
	wpg = cords[6]
	wph = cords[7]
	wra = cords[16]
	wnb = cords[26]
	wbc = cords[28]
	wq = cords[20]
	wk = cords[22]
	wbf = cords[29]
	wng = cords[27]
	wrh = cords[17]
	bpa = cords[8]
	bpb = cords[9]
	bpc = cords[10]
	bpd = cords[11]
	bpe = cords[12]
	bpf = cords[13]
	bpg = cords[14]
	bph = cords[15]
	bra = cords[18]
	bnb = cords[25]
	bbc = cords[30]
	bq = cords[21]
	bk = cords[23]
	bbf = cords[31]
	bng = cords[24]
	brh = cords[19]
	cordinates.changeValuest(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc, bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	blackmoves=Legalm.black_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	whitemoves=Legalm.white_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	botmove=Bestmove.best(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	piece = botmove[1]
	cor = botmove[2]
	if cor == wpa:
		wpa = (12, 12)
	if cor == wpb:
		wpb = (12, 12)
	if cor == wpc:
		wpc = (12, 12)
	if cor == wpd:
		wpd = (12, 12)
	if cor == wpe:
		wpe = (12, 12)
	if cor == wpf:
		wpf = (12, 12)
	if cor == wpg:
		wpg = (12, 12)
	if cor == wph:
		wph = (12, 12)
	if cor == wra:
		wra = (12, 12)
	if cor == wnb:
		wnb = (12, 12)
	if cor == wbc:
		wbc = (12, 12)
	if cor == wq:
		wq = (12, 12)
	if cor == wk:
		wk = (12, 12)
	if cor == wbf:
		wbf = (12, 12)
	if cor == wng:
		wng = (12, 12)
	if cor == wrh:
		wrh = (12, 12)
	if piece == "bpa":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,cor,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="bpb":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,cor,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="bpc":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,cor,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="bpd":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,cor,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="bpe":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,cor,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="bpf":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,cor,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="bpg":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,cor,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="bph":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,cor,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="bra":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,cor,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="bnb":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,cor,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="bbc":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,cor,bbf)
	elif piece=="bq":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,cor,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="bk":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,cor,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="bbf":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,cor)
	elif piece=="bng":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,cor,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="brh":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,cor,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	elif piece=="wra":
		cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,cor,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	cords = cordinates.getValues()
	wpa = cords[0]
	wpb = cords[1]
	wpc = cords[2]
	wpd = cords[3]
	wpe = cords[4]
	wpf = cords[5]
	wpg = cords[6]
	wph = cords[7]
	wra = cords[16]
	wnb = cords[26]
	wbc = cords[28]
	wq = cords[20]
	wk = cords[22]
	wbf = cords[29]
	wng = cords[27]
	wrh = cords[17]
	bpa = cords[8]
	bpb = cords[9]
	bpc = cords[10]
	bpd = cords[11]
	bpe = cords[12]
	bpf = cords[13]
	bpg = cords[14]
	bph = cords[15]
	bra = cords[18]
	bnb = cords[25]
	bbc = cords[30]
	bq = cords[21]
	bk = cords[23]
	bbf = cords[31]
	bng = cords[24]
	brh = cords[19]
	cordinates.changeValuest(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	blackmoves=Legalm.black_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	whitemoves=Legalm.white_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	movesnotcrashed+=1
	if movesnotcrashed== 1:
		print(movesnotcrashed,"move completed")
	else:
		print(movesnotcrashed,"moves completed")