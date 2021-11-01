#this file just has 2 functions, one that checks if there is a black piece and one that checks if there is a white piece.
def isblockedw(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh):
  import cordinates
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
  if wpa==(x,y) or wpb==(x,y) or wpc==(x,y) or wpd==(x,y) or wpe==(x,y) or wpf==(x,y) or wpg==(x,y) or wph==(x,y) or wra==(x,y) or wnb==(x,y) or wbc==(x,y) or wq==(x,y) or wk==(x,y) or wbf==(x,y) or wng==(x,y) or wrh==(x,y):
    return (True)
  else:
    return (False)
def isblockedb(x,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh):
  import cordinates
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
  if bpa==(x,y) or bpb==(x,y) or bpc==(x,y) or bpd==(x,y) or bpe==(x,y) or bpf==(x,y) or bpg==(x,y) or bph==(x,y) or bra==(x,y) or bnb==(x,y) or bbc==(x,y) or bq==(x,y) or bk==(x,y) or bbf==(x,y) or bng==(x,y) or brh==(x,y):
    return (True)
  else:
    return (False)