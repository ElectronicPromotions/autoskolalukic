/* Autoškola Lukić · zajednički JS za sve stranice
   Skrolanje je rasterećeno: header prati IntersectionObserver, a sve što zavisi
   od pozicije stranice računa se najviše jednom po frejmu (requestAnimationFrame). */
(function(){
  var d=document,root=d.documentElement;
  var $=function(s,c){return (c||d).querySelector(s)},$$=function(s,c){return Array.prototype.slice.call((c||d).querySelectorAll(s))};
  var reduce=matchMedia('(prefers-reduced-motion:reduce)').matches||root.classList.contains('lite');
  var IO='IntersectionObserver' in window;

  // header: tamna pozadina čim stranica krene, bez promjene visine
  var hd=$('#hd'),ts=$('#ts');
  if(IO&&ts){new IntersectionObserver(function(e){hd.classList.toggle('sc',!e[0].isIntersecting)}).observe(ts)}
  else{var sc=function(){hd.classList.toggle('sc',scrollY>30)};addEventListener('scroll',sc,{passive:true});sc()}

  // mobilni meni
  var mm=$('#mm'),mb=$('#mb');
  function menu(o){mm.classList.toggle('o',o);mb.setAttribute('aria-expanded',o?'true':'false');mb.textContent=o?'✕':'☰'}
  if(mb){mb.onclick=function(){menu(!mm.classList.contains('o'))}}
  $$('#mm a').forEach(function(a){a.addEventListener('click',function(){menu(false)})});

  // padajući meni na dodir
  function closeDD(){$$('.dd.open').forEach(function(x){x.classList.remove('open');x.querySelector('button').setAttribute('aria-expanded','false')})}
  $$('.dd>button').forEach(function(b){b.addEventListener('click',function(e){e.stopPropagation();var p=b.parentNode,o=!p.classList.contains('open');closeDD();p.classList.toggle('open',o);b.setAttribute('aria-expanded',o?'true':'false')})});
  d.addEventListener('click',function(e){if(!e.target.closest('.dd'))closeDD()});
  d.addEventListener('keydown',function(e){if(e.key==='Escape'){closeDD();if(mm&&mm.classList.contains('o'))menu(false)}});

  // traka sa porukama
  var mq=$('#mq');
  if(mq){
    var items=['25 godina iskustva','Sve kategorije: A B C1 C CE D','Strpljivi instruktori','Moderna učionica','Plaćanje na rate'],h='';
    items.forEach(function(t){h+='<span>★ '+t+'</span>'});
    mq.innerHTML=h;
    var mqs=$$('#mq span'),mi=0;mqs[0].classList.add('on');
    var mqT=setInterval(function(){if(d.hidden)return;mqs[mi].classList.remove('on');mi=(mi+1)%mqs.length;mqs[mi].classList.add('on')},2400);setTimeout(function(){clearInterval(mqT)},5000);
  }

  // 3D kovanica "25"
  var coin=$('#coin');
  if(coin){
    var L=16,out='';
    for(var i=0;i<L;i++){var z=(i-L/2)*2.2,shade=Math.round(120+i*6);
      out+='<div class="ly" style="transform:translateZ('+z+'px);background:rgb('+(shade+60)+','+(shade+20)+',0)"></div>';}
    out+='<div class="ly ft" style="transform:translateZ('+(L/2*2.2+1)+'px)">'
       +'<svg viewBox="0 0 200 200" aria-hidden="true" focusable="false"><defs><path id="cp" d="M100 100 m-78 0 a78 78 0 1 1 156 0 a78 78 0 1 1 -156 0"/></defs>'
       +'<text font-size="11" font-weight="800" fill="#C2410C" letter-spacing="4.4" font-family="Montserrat,Arial,sans-serif"><textPath href="#cp">AUTOŠKOLA LUKIĆ • BRČKO • AUTOŠKOLA LUKIĆ • BRČKO •</textPath></text></svg>'
       +'<div style="position:relative"><b>25</b><small>godina</small></div></div>';
    coin.innerHTML=out;
  }

  // tilt kartica
  function tilt(el,max){
    var raf=0,ev=null;
    el.addEventListener('pointermove',function(e){
      if(e.pointerType==='touch'||reduce)return;ev=e;if(raf)return;
      raf=requestAnimationFrame(function(){raf=0;var r=el.getBoundingClientRect(),x=(ev.clientX-r.left)/r.width-.5,y=(ev.clientY-r.top)/r.height-.5;
        el.style.transform='perspective(900px) rotateX('+(-y*max)+'deg) rotateY('+(x*max)+'deg) translateY(-6px)';
        el.style.setProperty('--mx',(x+.5)*100+'%');el.style.setProperty('--my',(y+.5)*100+'%')});
    });
    el.addEventListener('pointerleave',function(){if(raf){cancelAnimationFrame(raf);raf=0}el.style.transform=''});
  }
  window.LUKIC_TILT=tilt;
  $$('.tilt').forEach(function(c){tilt(c,12)});
  $$('.gi').forEach(function(c){tilt(c,16)});

  // hero: auto i kovanica prate miš
  var hero=$('#pocetna'),car=$('#car');
  if(hero&&car&&coin){
    var hr=0,hev=null;
    hero.addEventListener('pointermove',function(e){
      if(e.pointerType==='touch'||reduce)return;hev=e;if(hr)return;
      hr=requestAnimationFrame(function(){hr=0;var r=hero.getBoundingClientRect(),x=(hev.clientX-r.left)/r.width-.5,y=(hev.clientY-r.top)/r.height-.5;
        car.style.transform='translateX(calc(-50% + '+(x*-26)+'px)) perspective(900px) rotateY('+(x*-12)+'deg) rotateX('+(y*6)+'deg)';
        coin.classList.add('js');coin.style.transform='rotateY('+(x*55)+'deg) rotateX('+(-y*40)+'deg)'});
    });
    hero.addEventListener('pointerleave',function(){car.style.transform='';coin.classList.remove('js');coin.style.transform=''});
    // animacije heroja stoje dok hero nije na ekranu
    if(IO)new IntersectionObserver(function(e){hero.classList.toggle('paused',!e[0].isIntersecting)}).observe(hero);
  }

  // volan na dnu i dugme "nazad na vrh": jedan izračun po frejmu
  var wh=$('#wheel'),sce=$('#scene'),st=$('#st'),px=0,py=0,max=1,ticking=false;
  var pg=st&&st.querySelector('.pg'),c3=st&&st.querySelector('.c3');
  function measure(){max=Math.max(1,root.scrollHeight-innerHeight)}
  function frame(){
    ticking=false;var y=scrollY,p=Math.min(1,Math.max(0,y/max));if(p>.995)p=1;
    if(wh)wh.style.transform='rotateX('+(-py*20)+'deg) rotateY('+(px*26)+'deg) rotateZ('+(p*720)+'deg)';
    if(st){pg.style.strokeDashoffset=169.6*(1-p);c3.style.transform='rotateY('+(p*1080)+'deg)';st.classList.toggle('on',y>400)}
  }
  function req(){if(!ticking){ticking=true;requestAnimationFrame(frame)}}
  if(wh||st){
    measure();addEventListener('resize',function(){measure();req()},{passive:true});addEventListener('load',function(){measure();req()});
    if('ResizeObserver' in window)new ResizeObserver(function(){measure()}).observe(d.body);
    addEventListener('scroll',req,{passive:true});req();
  }
  if(wh&&sce){
    sce.addEventListener('pointermove',function(e){var r=sce.getBoundingClientRect();px=(e.clientX-r.left)/r.width-.5;py=(e.clientY-r.top)/r.height-.5;req()});
    sce.addEventListener('pointerleave',function(){px=py=0;req()});
  }
  if(st)st.onclick=function(){scrollTo({top:0,behavior:reduce?'auto':'smooth'})};

  // pojavljivanje sadržaja
  if(IO){
    var io=new IntersectionObserver(function(a){a.forEach(function(x){if(x.isIntersecting){x.target.classList.add('on');io.unobserve(x.target)}})},{threshold:.08});
    window.LUKIC_REVEAL=function(c){$$('.rvl:not(.on)',c).forEach(function(e){io.observe(e)})};
  }else{window.LUKIC_REVEAL=function(c){$$('.rvl',c).forEach(function(e){e.classList.add('on')})}}
  window.LUKIC_REVEAL(d);

  // galerija: uvećan prikaz fotografije
  var gi=$$('[data-lb]');
  if(gi.length){
    var lb=d.createElement('div');lb.className='lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');lb.setAttribute('aria-label','Fotografija');
    lb.innerHTML='<button type="button" class="lb-x" aria-label="Zatvori">✕</button><button type="button" class="lb-p" aria-label="Prethodna fotografija">‹</button><figure><img alt=""><figcaption></figcaption></figure><button type="button" class="lb-n" aria-label="Sljedeća fotografija">›</button>';
    d.body.appendChild(lb);
    var cur=0,im=lb.querySelector('img'),cap=lb.querySelector('figcaption'),last=null;
    var show=function(i){cur=(i+gi.length)%gi.length;var s=gi[cur].querySelector('img');im.src=s.currentSrc||s.src;im.alt=s.alt;cap.textContent=s.alt};
    var open=function(i){last=d.activeElement;show(i);lb.classList.add('on');root.classList.add('lock');lb.querySelector('.lb-x').focus()};
    var close=function(){lb.classList.remove('on');root.classList.remove('lock');if(last)last.focus()};
    gi.forEach(function(el,i){el.addEventListener('click',function(e){e.preventDefault();open(i)})});
    lb.addEventListener('click',function(e){if(e.target===lb||e.target.closest('.lb-x'))close();else if(e.target.closest('.lb-p'))show(cur-1);else if(e.target.closest('.lb-n'))show(cur+1)});
    d.addEventListener('keydown',function(e){if(!lb.classList.contains('on'))return;if(e.key==='Escape')close();else if(e.key==='ArrowLeft')show(cur-1);else if(e.key==='ArrowRight')show(cur+1)});
  }
})();

/* WCAG 2.2.2: ukrasni pokret staje nakon 5 sekundi */
(function(){function stop(){document.documentElement.classList.add('still');if(document.getAnimations)document.getAnimations().forEach(function(a){try{if(a.effect&&a.effect.getTiming().iterations===Infinity)a.pause()}catch(e){}})}
setTimeout(stop,5000);})();
/* WCAG 1.4.13: Escape zatvara padajući meni (i kad je otvoren mišem ili fokusom) i vraća fokus na dugme */
(function(){document.querySelectorAll('nav.d .dd').forEach(function(dd){var b=dd.querySelector('button');if(!b)return;
  dd.addEventListener('keydown',function(e){if(e.key==='Escape'){dd.classList.add('x');b.setAttribute('aria-expanded','false');b.focus();}});
  dd.addEventListener('mouseleave',function(){dd.classList.remove('x')});
  dd.addEventListener('focusout',function(e){if(!dd.contains(e.relatedTarget))dd.classList.remove('x')});
  b.addEventListener('click',function(){dd.classList.remove('x')});});})();
