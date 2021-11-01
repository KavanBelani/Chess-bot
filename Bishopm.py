import Open

def white_bishop(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
  moves=[]
  position=(x,y)
  if (x,y)!=(12,12):
    for i in [1,2,3,4,5,6,7,8]:
      if Open.isblockedw((x,y)[0]+i,(x,y)[1]+i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or i+(x,y)[0]>8 or i +(x,y)[1]>8 or i+(x,y)[0]<=0 or i +(x,y)[1]<=0: 
        break
      elif Open.isblockedb((x,y)[0]+i,(x,y)[1]+i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True: 
        moves.append(position)
        this=((x,y)[0]+i,(x,y)[1]+i)
        moves.append(this)
        break
      elif Open.isblockedw((x,y)[0]+i,(x,y)[1]+i,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True:
        break
      else:
        moves.append(position)
        this=((x,y)[0]+i,(x,y)[1]+i)
        moves.append(this)
    for i in [1,2,3,4,5,6,7,8]:
      if Open.isblockedw((x,y)[0]-i,(x,y)[1]+i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or 0-i+(x,y)[0]>8 or i +(x,y)[1]>8 or 0-i+(x,y)[0]<=0 or i +(x,y)[1]<=0: 
        break
      elif Open.isblockedb((x,y)[0]-i,(x,y)[1]+i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True:
        moves.append(position)
        this=((x,y)[0]-i,(x,y)[1]+i)
        moves.append(this)
        break
      elif Open.isblockedw((x,y)[0]-i,(x,y)[1]+i,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True:
        
        break
      else:
        moves.append(position)
        this=((x,y)[0]-i,(x,y)[1]+i)
        moves.append(this)
    for i in [1,2,3,4,5,6,7,8]:
      if Open.isblockedw((x,y)[0]+i,(x,y)[1]-i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or i+(x,y)[0]>8 or 0-i +(x,y)[1]>8 or i+(x,y)[0]<=0 or 0-i +(x,y)[1]<=0: 
        break
      elif Open.isblockedb((x,y)[0]+i,(x,y)[1]-i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True: 
        #print("hi")
        moves.append(position)
        this=((x,y)[0]+i,(x,y)[1]-i)
        moves.append(this)
        break
      elif Open.isblockedw((x,y)[0]+i,(x,y)[1]-i,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True:
        
        break
      else:
        moves.append(position)
        this=((x,y)[0]+i,(x,y)[1]-i)
        moves.append(this)
    for i in [1,2,3,4,5,6,7,8]:
      if Open.isblockedw((x,y)[0]-i,(x,y)[1]-i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or i-(x,y)[0]>8 or 0-i +(x,y)[1]>8 or 0-i+(x,y)[0]<=0 or 0-i +(x,y)[1]<=0:
        break
      elif Open.isblockedb((x,y)[0]-i,(x,y)[1]-i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True: 
        moves.append(position)
        this=((x,y)[0]-i,(x,y)[1]-i)
        moves.append(this)
        break
      elif Open.isblockedw((x,y)[0]-i,(x,y)[1]-i,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True:
        
        break
      else:
        moves.append(position)
        this=((x,y)[0]-i,(x,y)[1]-i)
        moves.append(this)
  return(moves)
def black_bishop(x,y,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
  moves=[]
  position=(x,y)
  
  if (x,y)!=(12,12):
    for i in [1,2,3,4,5,6,7,8]:
      if Open.isblockedb((x,y)[0]+i,(x,y)[1]+i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or i+(x,y)[0]>8 or i +(x,y)[1]>8 or i+(x,y)[0]<=0 or i +(x,y)[1]<=0: 
        break
      elif Open.isblockedw((x,y)[0]+i,(x,y)[1]+i,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True:
        moves.append(position)
        end=((x,y)[0]+i,(x,y)[1]+i)
        moves.append(end)
        break
      else:
        moves.append(position)
        end=((x,y)[0]+i,(x,y)[1]+i)
        moves.append(end)
    for i in [1,2,3,4,5,6,7,8]:
      if Open.isblockedb((x,y)[0]-i,(x,y)[1]+i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or 0-i+(x,y)[0]>8 or i +(x,y)[1]>8 or 0-i+(x,y)[0]<=0 or i +(x,y)[1]<=0: 
        break
      elif Open.isblockedw((x,y)[0]-i,(x,y)[1]+i,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True:

        moves.append(position)
        end=((x,y)[0]-i,(x,y)[1]+i)
        moves.append(end)
        break
      else:
        moves.append(position)
        end=((x,y)[0]-i,(x,y)[1]+i)
        moves.append(end)
    for i in [1,2,3,4,5,6,7,8]:
      if Open.isblockedb((x,y)[0]+i,(x,y)[1]-i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or i+(x,y)[0]>8 or 0-i +(x,y)[1]>8 or i+(x,y)[0]<=0 or 0-i +(x,y)[1]<=0: 
        #print("hi")
        break
      elif Open.isblockedw((x,y)[0]+i,(x,y)[1]-i,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True:
        moves.append(position)
        end=((x,y)[0]+i,(x,y)[1]-i)
        moves.append(end)
        break
      else:
        moves.append(position)
        end=((x,y)[0]+i,(x,y)[1]-i)
        moves.append(end)
    for i in [1,2,3,4,5,6,7,8]:
      if Open.isblockedb((x,y)[0]-i,(x,y)[1]-i,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh)==True or i-(x,y)[0]>8 or 0-i +(x,y)[1]>8 or 0-i+(x,y)[0]<=0 or 0-i +(x,y)[1]<=0: 
        #print("hi")
        break
      elif Open.isblockedw((x,y)[0]-i,(x,y)[1]-i,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==True:

        moves.append(position)
        end=((x,y)[0]-i,(x,y)[1]-i)
        moves.append(end)
        break
      else:
        moves.append(position)
        end=((x,y)[0]-i,(x,y)[1]-i)
        moves.append(end)
  return(moves)
def bothbb(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
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
  return(black_bishop(bbc[0],bbc[1],wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)+black_bishop(bbf[0],bbf[1],wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf))
def bothwb(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
  return(white_bishop(wbc[0],wbc[1],wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)+white_bishop(wbf[0],wbf[1],wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf))