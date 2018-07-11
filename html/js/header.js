window.onload = function() {
   console.log("HHHHHHHHH    HHHHHHHHH\n\
 HHHHHHH      HHHHHHH\n\
  HHHH         HHHH\n\
  HHHH         HHHH\n\
  HHHH         HHHH\n\
  HHHH         HHHH\n\
  HHHH         HHHH            aaaaaa                   ccccc              rrrr      rrr             aaaaaa\n\
  HHHH         HHHH         aaaaaaaaaaaa             ccccccccccc       rrrrrrrr   rrrrrrrr        aaaaaaaaaaaa\n\
  HHHH         HHHH       aaaa       aaaa          ccccc     cccc           rrr rrrr  rrrrr     aaaa       aaaa\n\
  HHHHHHHHHHHHHHHHH       aaaa        aaaa        cccc       ccccc          rrrrrr    rrrr      aaaa        aaaa\n\
  HHHH         HHHH       aaaa        aaaa       ccccc       cccc           rrrrr               aaaa        aaaa\n\
  HHHH         HHHH              aaaaaaaaa       cccc          c            rrrr                       aaaaaaaaa\n\
  HHHH         HHHH          aaaaaaaaaaaaa       cccc                       rrr                    aaaaaaaaaaaaa\n\
  HHHH         HHHH        aaaaa      aaaa       cccc                       rrr                  aaaaa      aaaa\n\
  HHHH         HHHH       aaaa        aaaa       cccc                       rrr                 aaaa        aaaa\n\
  HHHH         HHHH      aaaa         aaaa       cccc            cc         rrr                aaaa         aaaa\n\
  HHHH         HHHH      aaaa         aaaa aa    ccccc          cc          rrr                aaaa         aaaa aa\n\
  HHHH         HHHH      aaaa        aaaaa aa     cccc         ccc          rrr                aaaa        aaaaa aa\n\
  HHHHH        HHHHH      aaaaaaaaaaaaaaaaaaa      cccccccccccccc           rrrr                aaaaaaaaaaaaaaaaaaa\n\
HHHHHHHHH    HHHHHHHHH     aaaaaaaaa   aaaaa         cccccccccc        rrrrrrrrrrrrrr             aaaaaaaa   aaaaa\n\
  ")
}

window.onscroll = function() {
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop
    if(scrollTop >= 70){
        this.document.getElementById("header").style.display = "inline";
    }
    else {
        this.document.getElementById("header").style.display = "none";
    }
}