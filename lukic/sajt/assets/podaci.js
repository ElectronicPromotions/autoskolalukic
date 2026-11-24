/* Autoškola Lukić · prikaz predavanja i objava (čita podaci/*.js ili Google tabelu) */
(function(){
  var P=window.POSTAVKE||{};
  var $=function(s,c){return (c||document).querySelector(s)};
  var DANI=['nedjelja','ponedjeljak','utorak','srijeda','četvrtak','petak','subota'];
  var DANI_K=['ned','pon','uto','sri','čet','pet','sub'];
  var MJ=['jan','feb','mar','apr','maj','jun','jul','aug','sep','okt','nov','dec'];
  var MJ_D=['januara','februara','marta','aprila','maja','juna','jula','augusta','septembra','oktobra','novembra','decembra'];

  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  function norm(s){return String(s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/đ/g,'dj').trim()}
  function pd(s){
    s=String(s||'').trim();var m;
    if((m=s.match(/^(\d{4})-(\d{1,2})-(\d{1,2})/)))return new Date(+m[1],m[2]-1,+m[3]);
    if((m=s.match(/^(\d{1,2})[.\/](\d{1,2})[.\/](\d{4})/)))return new Date(+m[3],m[2]-1,+m[1]);
    return null;
  }
  function today(){var d=new Date();d.setHours(0,0,0,0);return d}
  function dLong(d){return d.getDate()+'. '+MJ_D[d.getMonth()]+' '+d.getFullYear()+'.'}
  function startTime(v){return String(v||'').split(/\s*(?:–|—|-|do)\s*/)[0].trim()}
  function linkify(t){return esc(t).replace(/(https?:\/\/[^\s<]+)/g,'<a href="$1" target="_blank" rel="noopener">$1</a>')}

  // CSV iz Google tabele (Datoteka, Dijeli, Objavi na webu, CSV)
  function csv(text){
    var rows=[],row=[],f='',q=false;
    for(var i=0;i<text.length;i++){var c=text[i];
      if(q){if(c=='"'){if(text[i+1]=='"'){f+='"';i++}else q=false}else f+=c}
      else if(c=='"')q=true;else if(c==','){row.push(f);f=''}
      else if(c=='\n'||c=='\r'){if(c=='\r'&&text[i+1]=='\n')i++;row.push(f);rows.push(row);row=[];f=''}
      else f+=c}
    if(f!==''||row.length){row.push(f);rows.push(row)}
    var h=(rows.shift()||[]).map(norm);
    return rows.filter(function(r){return r.join('').trim()}).map(function(r){var o={};h.forEach(function(k,i){o[k]=(r[i]||'').trim()});return o});
  }
  function pick(o,keys){for(var i=0;i<keys.length;i++){if(o[keys[i]])return o[keys[i]]}return ''}
  function splitNames(s){return String(s||'').split(/[,;\n]/).map(function(x){return x.trim()}).filter(Boolean)}
  function csvToPredavanja(rows){
    var map={},order=[],obv=[];
    rows.forEach(function(r){
      var n=pick(r,['grupa','naziv grupe','naziv'])||'Grupa';
      if(!map[n]){map[n]={naziv:n,skola:'',kategorija:'',predavac:'',mjesto:'',napomena:'',termini:[]};order.push(n)}
      var g=map[n];
      g.kategorija=g.kategorija||pick(r,['kategorija']);
      g.skola=g.skola||pick(r,['skola','škola','autoskola','autoškola']);
      g.predavac=g.predavac||pick(r,['predavac']);
      g.mjesto=g.mjesto||pick(r,['mjesto','ucionica']);
      g.napomena=g.napomena||pick(r,['napomena']);
      var d=pick(r,['datum']);
      if(d)g.termini.push({datum:d,vrijeme:pick(r,['vrijeme','sat']),tema:pick(r,['tema']),status:pick(r,['status']),napomena:pick(r,['napomena termina','izmjena'])});
      var ob=pick(r,['obavjestenje','obavještenje']);if(ob&&obv.indexOf(ob)<0)obv.push(ob);
    });
    return {primjer:false,azurirano:'',napomena:'',obavjestenja:obv,grupe:order.map(function(n){return map[n]})};
  }
  function csvToObjave(rows){
    return {primjer:false,autor:(window.OBJAVE||{}).autor||'',objave:rows.map(function(r){
      return {datum:pick(r,['datum']),naslov:pick(r,['naslov']),tekst:pick(r,['tekst','objava']),slika:pick(r,['slika']),link:pick(r,['link','facebook link','facebook'])}})};
  }
  function load(kind,cb){
    var url=kind=='p'?P.predavanjaCSV:P.objaveCSV, local=kind=='p'?window.PREDAVANJA:window.OBJAVE;
    if(!url){cb(local||null);return}
    fetch(url,{cache:'no-store'}).then(function(r){if(!r.ok)throw 0;return r.text()})
      .then(function(t){var rows=csv(t);cb(kind=='p'?csvToPredavanja(rows):csvToObjave(rows))})
      .catch(function(){cb(local||null)});
  }

  // priprema grupa
  function prep(data){
    var t0=today(),list=(data&&data.grupe||[]).map(function(g,gi){
      var ts=(g.termini||[]).map(function(t){var d=pd(t.datum),st=norm(t.status||'');return{d:d,vrijeme:t.vrijeme||'',tema:t.tema||'',cx:st.indexOf('otkaz')==0,ch:st.indexOf('promij')==0||st.indexOf('promjen')==0,nap:t.napomena||''}}).filter(function(t){return t.d}).sort(function(a,b){return a.d-b.d});
      var nx=null;ts.forEach(function(t){t.past=t.d<t0;t.today=+t.d==+t0;if(!nx&&!t.past&&!t.cx)nx=t});
      if(nx)nx.next=true;
      var cats=String(g.kategorija||'').split(/[,\/]/).map(function(s){return s.trim().toUpperCase()}).filter(Boolean);
      return{i:gi,naziv:g.naziv||('Grupa '+(gi+1)),skola:g.skola||'',kat:g.kategorija||'',cats:cats,predavac:g.predavac||'',mjesto:g.mjesto||'',napomena:g.napomena||'',ts:ts,nx:nx,done:ts.length&&!nx,start:ts[0]&&ts[0].d};
    });
    list.sort(function(a,b){if(a.done!=b.done)return a.done?1:-1;var x=a.nx?a.nx.d:a.start||0,y=b.nx?b.nx.d:b.start||0;return x-y});
    return list;
  }
  function tsRow(t){
    var cls=(t.past?'past ':'')+(t.next?'next ':'')+(t.today?'today ':'')+(t.cx?'cx ':'')+(t.ch?'ch':'');
    var tag=t.cx?'<em class="st cx">OTKAZANO</em>':t.ch?'<em class="st ch">PROMIJENJENO</em>':'';
    return '<li class="'+cls.trim()+'"><span class="d">'+t.d.getDate()+'. '+MJ[t.d.getMonth()]+'<small>'+DANI[t.d.getDay()]+'</small></span><span class="t"><b>'+esc(t.vrijeme||'Vrijeme uskoro')+tag+'</b><span>'+esc(t.tema)+'</span>'+(t.nap?'<small class="nap">'+esc(t.nap)+'</small>':'')+'</span></li>';
  }

  // stranica /predavanja/
  var app=$('#pv-app');
  if(app){
    load('p',function(data){
      var groups=prep(data),cat='SVE',sk='SVE';
      var cats=[],skole=[];groups.forEach(function(g){g.cats.forEach(function(c){if(cats.indexOf(c)<0)cats.push(c)});if(g.skola&&skole.indexOf(g.skola)<0)skole.push(g.skola)});
      var fl=$('#pv-flt'),fs=$('#pv-fsk'),out=$('#pv-list'),meta=$('#pv-meta');
      if(data&&data.primjer)$('#pv-banner').hidden=false;
      if(data&&data.napomena){$('#pv-note').textContent=data.napomena;$('#pv-note').hidden=false}
      var obv=(data&&data.obavjestenja||[]).filter(Boolean);
      if(obv.length){$('#pv-obv').innerHTML=obv.map(function(o){return '<p>📢 '+esc(o)+'</p>'}).join('');$('#pv-obv').hidden=false}
      var up=data&&pd(data.azurirano);
      function btns(list,cur,all,lbl){return ['SVE'].concat(list).map(function(c){return '<button type="button" data-c="'+esc(c)+'" aria-pressed="'+(c==cur)+'">'+(c=='SVE'?all:lbl(c))+'</button>'}).join('')}
      fl.innerHTML=cats.length>1?btns(cats,cat,'Sve kategorije',function(c){return esc(c)+' kategorija'}):'';
      fs.innerHTML=skole.length>1?btns(skole,sk,'Sve škole',esc):'';
      fl.onclick=function(e){var b=e.target.closest('button');if(!b)return;cat=b.getAttribute('data-c');[].forEach.call(fl.children,function(x){x.setAttribute('aria-pressed',x==b)});render()};
      fs.onclick=function(e){var b=e.target.closest('button');if(!b)return;sk=b.getAttribute('data-c');[].forEach.call(fs.children,function(x){x.setAttribute('aria-pressed',x==b)});render()};
      function render(){
        var shown=groups.filter(function(g){
          if(cat!='SVE'&&g.cats.indexOf(cat)<0)return false;
          if(sk!='SVE'&&g.skola!=sk)return false;
          return true});
        meta.innerHTML='<span>'+(groups.length?('Prikazano grupa: <b>'+shown.length+'</b> od '+groups.length):'')+(up?' · Ažurirano '+dLong(up):'')+'</span><button type="button" onclick="window.print()">🖨️ Odštampaj raspored</button>';
        if(!groups.length){out.innerHTML='<div class="empty"><b>Raspored uskoro</b>Nove grupe se formiraju nakon upisa. Za termine nazovi 065 537 043.</div>';return}
        if(!shown.length){out.innerHTML='<div class="empty"><b>Nema grupa za izabrani filter</b>Izaberi drugu kategoriju ili nazovi 065 537 043.</div>';return}
        out.innerHTML=shown.map(function(g){
          var st=g.done?'Završeno':g.nx?(g.nx.today?'Danas':'Sljedeće: '+DANI_K[g.nx.d.getDay()]+', '+g.nx.d.getDate()+'. '+MJ[g.nx.d.getMonth()])+(g.nx.vrijeme?' u '+esc(startTime(g.nx.vrijeme)):''):'Termini uskoro';
          return '<article class="gc" id="grupa-'+(g.i+1)+'">'
            +'<div class="gh"><h2>'+(g.kat?'<span class="bdg">'+esc(g.kat)+'</span>':'')+esc(g.naziv)+'</h2><div class="gi2">'
            +(g.skola?'<span>🏫 '+esc(g.skola)+'</span>':'')+'<span>📅 '+st+'</span>'+(g.start?'<span>▶ Početak '+dLong(g.start)+'</span>':'')+(g.predavac?'<span>🎓 '+esc(g.predavac)+'</span>':'')+(g.mjesto?'<span>📍 '+esc(g.mjesto)+'</span>':'')+'</div></div>'
            +'<div class="gb"><div><h3>Termini predavanja ('+g.ts.length+')</h3>'+(g.ts.length?'<ol class="tl">'+g.ts.map(tsRow).join('')+'</ol>':'<p class="mut">Termini će biti objavljeni uskoro.</p>')
            +(g.napomena?'<p class="gnote">ℹ️ '+esc(g.napomena)+'</p>':'')+'</div></div></article>';
        }).join('');
      }
      render();
    });
  }

  // početna: sljedeća predavanja
  var hp=$('#home-pv');
  if(hp){
    load('p',function(data){
      var all=[];prep(data).forEach(function(g){g.ts.forEach(function(t){if(!t.past&&!t.cx)all.push({g:g,t:t})})});
      all.sort(function(a,b){return a.t.d-b.t.d});all=all.slice(0,3);
      if(!all.length){hp.innerHTML='<div class="card" style="padding:24px;grid-column:1/-1;text-align:center"><h3>Nove grupe se upravo formiraju</h3><p>Nazovi 065 537 043 i saznaj kada počinje sljedeća grupa.</p></div>';return}
      hp.innerHTML=all.map(function(x){var d=x.t.d;return '<a class="card tilt" href="/predavanja/#grupa-'+(x.g.i+1)+'"><i class="gl"></i><span class="dt">'+DANI_K[d.getDay()].toUpperCase()+', '+d.getDate()+'. '+MJ[d.getMonth()]+(x.t.vrijeme?' · '+esc(x.t.vrijeme):'')+'</span><h3>'+esc(x.g.naziv)+(x.g.kat?', '+esc(x.g.kat)+' kategorija':'')+'</h3><p>'+esc(x.t.tema||'Teorijska nastava')+'</p></a>'}).join('');
      if(window.LUKIC_TILT)[].forEach.call(hp.querySelectorAll('.tilt'),function(c){window.LUKIC_TILT(c,12)});
    });
  }

  // objave
  function fbEmbed(link,w){return '<div class="post embed"><iframe title="Objava sa Facebooka" loading="lazy" src="https://www.facebook.com/plugins/post.php?href='+encodeURIComponent(link)+'&show_text=true&width='+w+'" allow="encrypted-media; clipboard-write; picture-in-picture; web-share"></iframe></div>'}
  function postCard(o,autor,clamp,h){
    var d=pd(o.datum);h=h||'h2';
    if(!o.tekst&&!o.naslov&&o.link)return fbEmbed(o.link,500);
    return '<article class="post">'+(o.slika?'<div class="ph2"><img src="'+esc(o.slika)+'" alt="'+esc(o.naslov||'Objava Autoškole Lukić')+'" loading="lazy" decoding="async"></div>':'')
      +'<div class="pb"><div class="who"><span class="av y">VL</span><div><b>'+esc(autor||'Autoškola Lukić')+'</b>'+(d?'<time datetime="'+esc(o.datum)+'">'+dLong(d)+'</time>':'')+'</div></div>'
      +(o.naslov?'<'+h+'>'+esc(o.naslov)+'</'+h+'>':'')+(o.tekst?'<div class="tx'+(clamp?' cl':'')+'">'+linkify(o.tekst)+'</div>':'')
      +'<div class="act">'+(o.tekst&&o.tekst.length>320&&clamp?'<button type="button" class="rm">Prikaži više ↓</button>':'')+(o.link?'<a class="fb" href="'+esc(o.link)+'" target="_blank" rel="noopener">f &nbsp;Pogledaj na Facebooku</a>':'')+'</div></div></article>';
  }
  function sortPosts(a){return (a||[]).slice().sort(function(x,y){var a1=pd(x.datum),b1=pd(y.datum);return (b1||0)-(a1||0)})}

  var na=$('#nw-app');
  if(na){
    var fbw=$('#nw-fb');
    if(P.facebookStranica&&fbw){
      var w=Math.max(280,Math.min(500,Math.floor(fbw.clientWidth||500)));
      fbw.innerHTML='<div class="fbx"><div class="fbh">f &nbsp;Uživo sa Facebooka</div><iframe title="Facebook objave Autoškole Lukić" loading="lazy" src="https://www.facebook.com/plugins/page.php?href='+encodeURIComponent(P.facebookStranica)+'&tabs=timeline&width='+w+'&height=900&small_header=false&adapt_container_width=true&hide_cover=false&show_facepile=false" style="min-height:900px" allow="encrypted-media; clipboard-write; picture-in-picture; web-share"></iframe></div>';
      var fl2=$('#nw-fblink');if(fl2){fl2.href=P.facebookStranica;fl2.hidden=false}
    }else if(fbw){fbw.hidden=true;na.classList.add('solo')}
    load('o',function(data){
      if(data&&data.primjer)$('#nw-banner').hidden=false;
      var list=sortPosts(data&&data.objave),box=$('#nw-list');
      if(!list.length&&P.facebookStranica){box.hidden=true;na.classList.add('fbonly');return}
      box.innerHTML=list.length?list.map(function(o){return postCard(o,data.autor,true)}).join(''):'<div class="empty"><b>Objave uskoro</b>Prati nas i na Instagramu <a href="https://www.instagram.com/autoskolalukic" target="_blank" rel="noopener">@autoskolalukic</a>.</div>';
      box.onclick=function(e){var b=e.target.closest('.rm');if(!b)return;var t=b.closest('.pb').querySelector('.tx');t.classList.toggle('cl');b.textContent=t.classList.contains('cl')?'Prikaži više ↓':'Prikaži manje ↑'};
    });
  }

  var hn=$('#home-nw');
  if(hn){
    load('o',function(data){
      var list=sortPosts(data&&data.objave).filter(function(o){return o.tekst||o.naslov}).slice(0,3);
      if(!list.length&&P.facebookStranica){hn.classList.add('fbonly');hn.innerHTML='<div class="fbx"><div class="fbh">f &nbsp;Najnovije sa Facebooka</div><iframe title="Facebook objave Autoškole Lukić" loading="lazy" src="https://www.facebook.com/plugins/page.php?href='+encodeURIComponent(P.facebookStranica)+'&tabs=timeline&width=500&height=640&small_header=true&adapt_container_width=true&hide_cover=false&show_facepile=false" style="min-height:640px" allow="encrypted-media; clipboard-write; picture-in-picture; web-share"></iframe></div>';return}
      if(!list.length){var s=hn.closest('section');if(s)s.hidden=true;return}
      hn.innerHTML=list.map(function(o){return postCard(o,data.autor,true,'h3')}).join('');
    });
  }
})();
