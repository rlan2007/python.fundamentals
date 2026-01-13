with open('out.txt', 'w') as outf:
  pass
with open('dataset.txt') as inf:
  for line in inf:    
    with open ('out.txt','r' ) as outf,  open ('tmp.txt','w' ) as tmpf:
      for line_out in outf:
        tmpf.write(line_out)
    outf = open ('out.txt','w')
    outf.write(line)    
    outf.close()
    with open ('out.txt','a' ) as outf,  open ('tmp.txt','r' ) as tmpf:
      for line_tmp in tmpf:
        outf.write(line_tmp)
	
