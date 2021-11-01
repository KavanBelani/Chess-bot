import rook 
import Bishopm
import knight
import Queen
import king
import Pawn2
import cordinates

def black_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
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
  pieces=[wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,bra,bnb,bbc,bq,bk,bbf,bng,brh]
  
  km=king.blackKingLegalMoves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  bm=Bishopm.bothbb(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  nm=knight.black_knight(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  rm=rook.bbr(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  qm=Queen.black_queen(bq[0],bq[1],wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  pm=Pawn2.black_pawn(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  return(pm+bm+nm+rm+km+qm)
def white_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf):
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
  
  km=king.whiteKingLegalMoves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  bm=Bishopm.bothwb(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  nm=knight.white_knight(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  rm=rook.bwr(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  qm=Queen.white_queen(wq[0],wq[1],wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  pm=Pawn2.white_pawn(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  return(km+bm+nm+rm+qm+pm)
  
    
