#this file just has 2 functions, one that checks if there is a black piece and one that checks if there is a white piece.
def isblockedw(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh):
  if wpa==(x,y) or wpb==(x,y) or wpc==(x,y) or wpd==(x,y) or wpe==(x,y) or wpf==(x,y) or wpg==(x,y) or wph==(x,y) or wra==(x,y) or wnb==(x,y) or wbc==(x,y) or wq==(x,y) or wk==(x,y) or wbf==(x,y) or wng==(x,y) or wrh==(x,y):
    return (True)
  else:
    return (False)
def isblockedb(x,y,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh):
  if bpa==(x,y) or bpb==(x,y) or bpc==(x,y) or bpd==(x,y) or bpe==(x,y) or bpf==(x,y) or bpg==(x,y) or bph==(x,y) or bra==(x,y) or bnb==(x,y) or bbc==(x,y) or bq==(x,y) or bk==(x,y) or bbf==(x,y) or bng==(x,y) or brh==(x,y):
    return (True)
  else:
    return (False)