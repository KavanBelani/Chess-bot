import Open
def knight(x,y,color,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
  x1=[1,1,-1,-1,2,2,-2,-2]
  y1=[2,-2,2,-2,1,-1,1,-1]
  moves=[]
  if color=="white":
    for i in range(8):
      if Open.isblockedw(x+x1[i],y+y1[i],wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True or x+x1[i]>8 or x+x1[i]<=0 or y+y1[i]>8 or y+y1[i]<=0:
        continue
      elif (x,y)!=(12,12):
        moves.append((x,y))
        moves.append(((x+x1[i]),(y+y1[i])))
  if color=="black":
    for i in range(8):
      if Open.isblockedb(x+x1[i],y+y1[i],bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or x+x1[i]>8 or x+x1[i]<=0 or y+y1[i]>8 or y+y1[i]<=0:
        continue
      elif (x,y)!=(12,12):
        moves.append((x,y))
        moves.append(((x+x1[i]),(y+y1[i])))
  return(moves)
def black_knight(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
  return(knight(bnb[0],bnb[1],"black",wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)+knight(bng[0],bng[1],"black",wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf))
def white_knight(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
  return(knight(wnb[0],wnb[1],"white",wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)+knight(wng[0],wng[1],"white",wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf))