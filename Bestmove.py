import cordinates
import Legalm
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
blackmoves=Legalm.black_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
whitemoves=Legalm.white_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
def value(piece):
  
  if piece[1] =="p":    
    return 10
  if piece[1]=="r":    
    return 50
  if piece[1]=="n":  	
    return 30
  if piece[1]=="b":   
    return 30
  if piece[1]=="q":    
    return 90
  if piece[1]=="k":
    return 900
    
def best(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
  import cordinates
  import Bestmove
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
  blackmoves=Legalm.black_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  whitemoves=Legalm.white_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)

  moves=0
  movestested=0
  blackrank=[]
  for i in range(len(blackmoves)//2):
    start=blackmoves[i*2]
    end=blackmoves[(i*2+1)]
    endx=end[0]
    endy=end[1]
    blackpiece=[]
    piece=cordinates.whatPiece((start[0]),(start[1]))
    originalpos=[wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf]
    endpiece=cordinates.whatPiece(endx,endy)
    currentvalue0=0
    if end == (3,6) or end == (3,5) or end == (6,6)or end == (6,5):
    	currentvalue0+=0.1
    if end ==(4,6) or end == (5,6):
    	currentvalue0+=0.2
    if end ==(4,5) or end == (5,5):
    	currentvalue0+=0.3
    if endpiece[0]=="w":	                                currentvalue0=Bestmove.value(endpiece)
    if endpiece=="none":
      endpiece=0
    if end == wpa:
    	wpa = (12,12)
    if end == wpb:
    	wpb = (12,12)
    if end == wpc:
    	wpc = (12,12)
    if end == wpd:
    	wpd = (12,12)
    if end == wpe:
    	wpe = (12,12)
    if end == wpf:
    	wpf = (12,12)
    if end == wpg:
    	wpg = (12,12)
    if end == wph:
    	wph = (12,12)
    if end == wra:
    	wra = (12,12)
    if end == wnb:
    	wnb = (12,12)
    if end == wbc:
    	wbc = (12,12)
    if end == wq:
    	wq = (12,12)
    if end == wk:
    	wk = (12,12)
    if end == wbf:
    	wbf = (12,12)
    if end == wng:
    	wng = (12,12)
    if end == wrh:
    	wrh = (12,12)
    if piece=="bpa":
      bpa=end
    elif piece=="bpb":
      bpb=end
    elif piece=="bpc":
      bpc=end
    elif piece=="bpc":
      bpc=end
    elif piece=="bpd":
      bpd=end
    elif piece=="bpe":
      bpe=end
    elif piece=="bpf":
      bpf=end
    elif piece=="bpg":
      bpg=end
    elif piece=="bph":
      bph=end
    elif piece=="bra":
      bra=end
    elif piece=="bnb":
      bnb=end
    elif piece=="bbc":
      bbc=end
    elif piece=="bq":
      bq=end
    elif piece=="bk":
      bk=end
    elif piece=="bbf":
      bpf=end
    elif piece=="bng":
      bng=end
    elif piece=="brh":
      brh=end
    cordinates.changeValuest(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
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

    whiterank=[]    
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
    whitemoves=Legalm.white_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
    blackmoves2=Legalm.black_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
    for i in range((len(whitemoves)//2)-1):
      originalpos2=[wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf]
      whitemoves=Legalm.white_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
      blackmoves2=Legalm.black_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
      start2=whitemoves[i*2]
      end2=whitemoves[i*2+1]
      endx2=end2[0]
      endy2=end2[1]
      piece2=cordinates.whatPiece((start2[0]),(start2[1]))
      currentvalue=0
      endpiece2=cordinates.whatPiece(endx2,endy2)
      if endpiece2[0]=="b":
      	currentvalue=Bestmove.value(endpiece2)
      elif endpiece2=="none":
        endpiece2=0    
      if end2 == bpa:
        bpa = (12,12)
      elif end2 == bpb:
      	bpb = (12,12)
      elif end2 == bpc:
      	bpc = (12,12)
      elif end2 == bpd:
      	bpd = (12,12)
      elif end2 == bpe:
      	bpe = (12,12)
      elif end2 == bpf:
      	bpf = (12,12)
      elif end2 == bpg:
      	bpg = (12,12)
      elif end2 == bph:
      	bph = (12,12)
      elif end2 == bra:
      	bra = (12,12)
      elif end2 == bnb:
      	bnb = (12,12)
      elif end2 == bbc:
      	bbc = (12,12)
      elif end2 == bq:
      	bq = (12,12)
      elif end2 == bk:
      	bk = (12,12)
      elif end2 == bbf:
      	bbf = (12,12)
      elif end2 == bng:
      	bng = (12,12)
      elif end2 == brh:
      	brh = (12,12)
      elif piece2=="wpa":
        wpa=end2
      elif piece2=="wpb":
        wpb=end2
      elif piece2=="wpc":
        wpc=end2
      elif piece2=="wpd":
        wpd=end2
      elif piece2=="wpe":
        wpe=end2
      elif piece2=="wpf":
        wpf=end2
      elif piece2=="wpg":
        wpg=end2
      elif piece2=="wph":
        wph=end2
      elif piece2=="wra":
        wra=end2
      elif piece2=="wnb":
        wnb=end2
      elif piece2=="wbc":
        wbc=end2
      elif piece2=="wq":
        wq=end2
      elif piece2=="wk":
        wk=end2
      elif piece2=="wbf":
        wpf=end2
      elif piece2=="wng":
        wng=end2
      elif piece2=="wrh":
        wrh=end2
      cordinates.changeValuest(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
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
      whitemoves=Legalm.white_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
      blackmoves2=Legalm.black_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
      blackrank2=[]
      if currentvalue>-1:
        for k in range(len(blackmoves2)//2):
          movestested+=1
          start3=blackmoves2[k*2]
          end3=blackmoves2[k*2+1]
          piece3=cordinates.whatPiece(start3[0],start3[1])
          piece4=cordinates.whatPiece(end3[0],end3[1])
          if piece4[0]=="w":  
            blackrank2.append([Bestmove.value(piece4),piece3,end3])
          else:
            blackrank2.append([0,piece3,end3])
        blackrank2.sort()
        bestblack2=blackrank2[0]
        whiterank.append([(currentvalue-int(bestblack2[0])),piece2,end2])
        whiterank.append([currentvalue,piece2,end2])																										    
        
      if piece2=="wpa":
        
        wpa=start2
      elif piece2=="wpb":
        wpb=start2
      elif piece2=="wpc":
        wpc=start2
      elif piece2=="wpd":
        wpd=start2
      elif piece2=="wpe":
        wpe=start2
      elif piece2=="wpf":
        wpf=start2
      elif piece2=="wpg":
        wpg=start2
      elif piece2=="wph":
        wph=start2
      elif piece2=="wra":
        wra=start2
      elif piece2=="wnb":
        wnb=start2
      elif piece2=="wbc":
        wbc=start2
      elif piece2=="wq":
        wq=start2
      elif piece2=="wk":
        wk=start2
      elif piece2=="wbf":
        wbf=start2
      elif piece2=="wng":
        wng=start2
      elif piece2=="wrh":
        wrh=start2
      elif piece2=="wpa":
        wpa=start2
      elif piece2=="wpb":
        wpb=start2
      elif piece2=="wpc":
        wpc=start2
      elif piece2=="wpd":
        wpd=start2
      elif piece2=="wpe":
        wpe=start2
      elif piece2=="wpf":
        wpf=start2
      elif piece2=="wpg":
        wpg=start2
      elif piece2=="wph":
        wph=start2
      elif piece2=="wra":
        wra=start2
      elif piece2=="wnb":
        wnb=start2
      elif piece2=="wbc":
        wbc=start2
      elif piece2=="wq":
        wq=start2
      elif piece2=="wk":
        wk=start2
      elif piece2=="wbf":
        wbf=start2
      elif piece2=="wng":
        wng=start2
      elif piece2=="wrh":
        wrh=start2
      cordinates.changeValuest(originalpos2[0],originalpos2[1],originalpos2[2],originalpos2[3],originalpos2[4],originalpos2[5],originalpos2[6],originalpos2[7],originalpos2[8],originalpos2[9],originalpos2[10],originalpos2[11],originalpos2[12],originalpos2[13],originalpos2[14],originalpos2[15],originalpos2[16],originalpos2[17],originalpos2[18],originalpos2[19],originalpos2[20],originalpos2[21],originalpos2[22],originalpos2[23],originalpos2[24],originalpos2[25],originalpos2[26],originalpos2[27],originalpos2[28],originalpos2[29],originalpos2[30],originalpos2[31])
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
      whitemoves=Legalm.white_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
      blackmoves2=Legalm.black_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
      
      
    whiterank.sort(reverse=True)
    if len(whiterank)>0:
      whitebest=whiterank[0]
    blackrank.append([(currentvalue0-int(whitebest[0])),piece,end,whitebest[1],whitebest[2]])
    cordinates.changeValuest(originalpos[0],originalpos[1],originalpos[2],originalpos[3],originalpos[4],originalpos[5],originalpos[6],originalpos[7],originalpos[8],originalpos[9],originalpos[10],originalpos[11],originalpos[12],originalpos[13],originalpos[14],originalpos[15],originalpos[16],originalpos[17],originalpos[18],originalpos[19],originalpos[20],originalpos[21],originalpos[22],originalpos[23],originalpos[24],originalpos[25],originalpos[26],originalpos[27],originalpos[28],originalpos[29],originalpos[30],originalpos[31])
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
    moves+=1
    print(str(int(round(moves/(len(blackmoves)//2),2)*100))+"% done", end="\r")
  blackrank.sort(reverse=True)
  print(movestested,"situations tested")
  print("bot moves",str(blackrank[0][1]).upper(),"to",blackrank[0][2])
  
  return(blackrank[0])