function linkPrint(count) {
    var txtId = "memotxt"+count;
    var Mtxt = document.getElementById(txtId).innerHTML;
    var lines = Mtxt.split("\n");
    
    var Ptxt = "";
    if(lines.length>=3){
        for (var i =0 ; i<3; i++) {
            if(i==3) break;
            Ptxt += '<div class="link-txt">'
            Ptxt += "<a href=";
            Ptxt += lines[i];
            Ptxt += ' target="_blank">';
            Ptxt += lines[i];
            Ptxt += "</a></div>"
        }
        Ptxt += '<a href="#">&nbsp;더보기...</a>'
    } else{
        for (var i =0 ; i<lines.length; i++) {
            Ptxt += '<div class="link-txt">'
            Ptxt += "<a href=";
            Ptxt += lines[i];
            Ptxt += ' target="_blank">';
            Ptxt += lines[i];
            Ptxt += "</a></div>"
        }
        Ptxt += '<a href="#">&nbsp;더보기...</a>'
    }
    var memoID = "result"+count;
    var blk = document.getElementById(memoID);
    blk.innerHTML = Ptxt;
    console.log(memoID);
}