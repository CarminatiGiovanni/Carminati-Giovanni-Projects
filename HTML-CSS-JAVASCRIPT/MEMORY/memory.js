let indirizzi_immagini = [];
for(let i=1;i<=17;i++) indirizzi_immagini.push("./IMG/" + i +".png"); //carica le immagini


let GLOBALS_LET = {
    a : null,
    b : null,
    coppie_trovate : 0,
    N_TESSERE : NaN,
};

function carica(){
    coppie_trovate = 0;
    N_TESSERE = NaN;
    do {
        GLOBALS_LET.N_TESSERE = parseInt(prompt('numero di tessere: '));
    } while(isNaN(GLOBALS_LET.N_TESSERE) || GLOBALS_LET.N_TESSERE<2 || GLOBALS_LET.N_TESSERE>17);
    let immagini_mixed = indirizzi_immagini.slice(0,GLOBALS_LET.N_TESSERE);
    let len = immagini_mixed.length;
    for(let k=0;k<len;k++) immagini_mixed.push(immagini_mixed[k]); 
    immagini_mixed = mescola(immagini_mixed);
    let G = Math.ceil(Math.sqrt(GLOBALS_LET.N_TESSERE*2));
    let conta = 0;
    document.write('<head> <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous"></head>');
    document.write('<body>');
    //document.write('<div style="position:fixed;top:0;left:0;background-color:cornflowerblue;color:black;" id="opened_cards">0</div>');
    document.body.style.backgroundColor = "cornflowerblue";
    document.body.style.marginTop = "100px";
    document.write('<table id="tabella" style="border:cornflowerblue 4px solid;border-collapse:collapse;size:cover;margin-left:auto;margin-right:auto">');
    while(conta<GLOBALS_LET.N_TESSERE*2){
        document.write('<tr style="border:cornflowerblue 4px solid;">');
        for(let i = 0;i<G && conta<GLOBALS_LET.N_TESSERE*2;i++){
            let img = '<img style="opacity:0;width:100px;height:100px;" id="image" onmousedown="scopri(this)" src="' + immagini_mixed[conta] +'">';
            let td = '<td style="border:cornflowerblue 4px solid;background-image: url(\'IMG/wall.jpg\');">'+img+'</td>';
            document.write(td);
            conta++;
        }
        document.write('</tr>');
    }
    document.write('<table>');
    document.write('</body>');

}

function confronta(){
    if(GLOBALS_LET.a.src == GLOBALS_LET.b.src){
        GLOBALS_LET.a.src = "./IMG/muro-di-mattoni.jpg"; 
        GLOBALS_LET.b.src = "./IMG/muro-di-mattoni.jpg"; 
        GLOBALS_LET.coppie_trovate++;
        //alert(GLOBALS_LET.coppie_trovate + " " + GLOBALS_LET.N_TESSERE);
    }
    copri();
}

function copri(){  
    if(GLOBALS_LET.a.src.search('./IMG/muro-di-mattoni.jpg') == -1) {GLOBALS_LET.a.style.opacity = 0;}
    if(GLOBALS_LET.b.src.search('./IMG/muro-di-mattoni.jpg') == -1) {GLOBALS_LET.b.style.opacity = 0;}
    GLOBALS_LET.a = null;
    GLOBALS_LET.b = null;
    if(GLOBALS_LET.coppie_trovate == GLOBALS_LET.N_TESSERE){vittoria();}
}

function scopri(obj){
    //console.log(GLOBALS_LET.a);
    //console.log(GLOBALS_LET.b);
    if (GLOBALS_LET.a == null) {
        GLOBALS_LET.a = obj;
        obj.style.opacity = 100;
    }
    else if (GLOBALS_LET.b == null && GLOBALS_LET.a != obj) {
        GLOBALS_LET.b = obj;
        obj.style.opacity = 100;
        setTimeout(()=>{confronta();},1500);
    }
}

function vittoria(){
    // //document.open();
    // document.body.style.backgroundColor = 'lime'; 
    // document.getElementById("tabella").style.backgroundColor = 'lime';
    // let sn;
    // do{
    //     sn = prompt("giovare ancora? S/N");
    // }while(sn != 's' && sn != 'N' && sn != 'n' && sn != 'S');
    // if(sn == 's' || sn == 'S'){
    //     document.open();
    //     carica();
    // } 
    setTimeout(2100);   
    alert("complimenti hai vinto!");
    
    document.write('<a class="btn btn-primary" style="position:absolute;left:45%;" href="../../../index.html" role="button">back Homepage</a><script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>');

}

function mescola(array) {
 
    //Ci prendiamo la lunghezza dell'array e partiamo dal fondo!
    var currentIndex = array.length, temporaryValue, randomIndex;
   
    // Finché ci sono elementi da mescolare, iteriamo l'array
    while (0 !== currentIndex) {
   
      //Prendiamo un indice a caso dell'array, purché sia compreso tra 0 e la lunghezza dell'array
      randomIndex = Math.floor(Math.random() * currentIndex);
   
      //Riduciamo di un'unità l'indice corrente
      currentIndex -= 1;
   
      // Una volta che abbiamo preso l'indice casuale, invertiamo l'elemento che stiamo analizzando alla posizione corrente (currentIndex) con quello alla posizione presa casualmente (randomIndex)
   
      //Variabile temporanea
      temporaryValue = array[currentIndex];
      //Eseguiamo lo scambio
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }
    //Torniamo l'array mescolato a fine ciclo
    return array;
}