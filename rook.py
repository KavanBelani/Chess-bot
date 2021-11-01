import Open


def black_rook(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
  moves=[]
  pos=(x,y)
  for i in [1,2,3,4,5,6,7,8]:
    if (x,y)==(12,12):
      continue
    if Open.isblockedw(x,y+i,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True and (x,y)!=(12,12) and y+i <9:
      moves.append(pos)
      end=(x,y+i)
      moves.append(end)
      break
    elif Open.isblockedb(x,y+i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or y+i>8:
      break
    elif (x,y)!=(12,12):
      moves.append(pos)
      end=(x,y+i)
      moves.append(end)
  for i in [1,2,3,4,5,6,7,8]:
    if Open.isblockedw(x,y-i,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True and y-i>0:
      moves.append(pos)
      end=(x,y-i)
      moves.append(end)
      break
    elif Open.isblockedb(x,y-i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or y-i<=0:
      break
    else:
      moves.append(pos)
      end=(x,y-i)
      moves.append(end)
  for i in [1,2,3,4,5,6,7,8]:
    if Open.isblockedw(x+i,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True and (x+i)<9:
      if x+i==9:
      	print(x+i,"kavan")
      moves.append(pos)
      end=(x+i,y)
      moves.append(end)
      break
    elif Open.isblockedb(x+i,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or x+i>8:
      break
    elif (x+i)<9:
      if x+i==9:
      	print(x+i,"kavan")
      moves.append(pos)
      end=(x+i,y)
      moves.append(end)
  for i in [1,2,3,4,5,6,7,8]:
    if Open.isblockedw(x-i,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True and x-i>0:
      moves.append(pos)
      end=(x-i,y)
      moves.append(end)
      break
    elif Open.isblockedb(x-i,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or x-i<=0:
      break
    else:
      moves.append(pos)
      end=(x+i,y)
      moves.append(end)
  return(moves)


def white_rook(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
  moves=[]
  pos=(x,y)
  for i in [1,2,3,4,5,6,7,8]:
    if (x,y)==(12,12):
      continue
    if Open.isblockedw(x,y+i,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True or y+i>8:
      break
    elif Open.isblockedb(x,y+i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True:
      moves.append(pos)
      end=(x,y+i)
      moves.append(end)
      break
    else:
      moves.append(pos)
      end=(x,y+i)
      moves.append(end)
  for i in [1,2,3,4,5,6,7,8]:
    if Open.isblockedw(x,y-i,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True or y-i<=0:
      break
    elif Open.isblockedb(x,y-i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True:
      moves.append(pos)
      end=(x,y-i)
      moves.append(end)
      break
    else:
      moves.append(pos)
      end=(x,y-i)
      moves.append(end)
  for i in [1,2,3,4,5,6,7,8]:
    if Open.isblockedw(x+i,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True or x+i>8:
      break
    elif Open.isblockedb(x+i,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True:
      moves.append(pos)
      end=(x+i,y)
      moves.append(end)
      break
    else:
      moves.append(pos)
      end=(x+i,y)
      moves.append(end)
  for i in [1,2,3,4,5,6,7,8]:
    if Open.isblockedw(x-i,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True or x-i<=0:
      break
    elif Open.isblockedb(x-i,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True:
      moves.append(pos)
      end=(x-i,y)
      moves.append(end)
      break
    else:
      moves.append(pos)
      end=(x-i,y)
      moves.append(end)
  return(moves)
def bwr(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
  return(white_rook(wra[0],wra[1],wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)+white_rook(wrh[0],wrh[1],wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf))
def bbr(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
	return(black_rook(bra[0],bra[1],wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)+black_rook(brh[0],brh[1],wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf))