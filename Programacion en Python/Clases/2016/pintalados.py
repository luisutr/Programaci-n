__author__ = 'luxsutrxlla'

def pinta_lados(lado):
    for x in range(1, lado):
        print "",
        for y in range(1, lado):
            if(x==1 or y==1):
                print "*"
            else:
                if(x==lado or y==lado):
                    print "*"
                else:
                    print " "


#pinta_lados(6)

def pinta_cad(lado):
    y=1
    while (y < lado+1):
              x = 1
              while (x < lado+1):
                    if (y == 1):
                       print("* ")
                    if (y != 1):
                       if (y != lado):
                          if (x == 1):
                             print("* ")
                          else:
                              if (x < lado):
                                 print("  ")
                              else:
                                  print("* ")
                       else:
                            print("* ")
                    x=x+1
              print(" \n")
              y=y+1

pinta_cad(6)