(function(){
document.addEventListener('click',function(e){var b=e.target.closest('.kopie');if(!b)return;
 var el=document.getElementById(b.dataset.kopie),tekst=el.textContent.trim();
 function klaar(){b.classList.add('ok');var o=b.innerHTML;b.innerHTML='<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8.5l3.2 3.2L13 4.8"/></svg>';
  setTimeout(function(){b.classList.remove('ok');b.innerHTML=o},1400)}
 function oud(){var t=document.createElement('textarea');t.value=tekst;t.setAttribute('readonly','');t.style.cssText='position:fixed;opacity:0';document.body.appendChild(t);t.select();
  try{if(document.execCommand('copy'))klaar()}catch(x){}document.body.removeChild(t)}
 if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(tekst).then(klaar,oud)}else{oud()}});
})();
(function(){
var root=document.documentElement,knoppen=document.querySelectorAll('.taal button');
function zet(l){root.lang=l;root.dataset.sel=l;
 knoppen.forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.l===l))});
 document.querySelectorAll('[data-nl]').forEach(function(el){var v=el.dataset[l];
  if(el.tagName==='TITLE')el.textContent=v;else if(el.hasAttribute('content'))el.setAttribute('content',v);
  else if(el.dataset.attr)el.setAttribute(el.dataset.attr,v);});
 try{localStorage.setItem('taal',l)}catch(e){}
 if(window.vast)window.vast()}
var s=null;try{s=localStorage.getItem('taal')}catch(e){}
zet(s||((navigator.language||'nl').slice(0,2)==='nl'?'nl':'en'));
knoppen.forEach(function(b){b.addEventListener('click',function(){var l=b.dataset.l;if(l===root.lang)return;
 if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){zet(l);return}
 root.dataset.sel=l;root.classList.add('wisselt');setTimeout(function(){zet(l);requestAnimationFrame(function(){requestAnimationFrame(function(){root.classList.remove('wisselt')})})},190)})});
requestAnimationFrame(function(){requestAnimationFrame(function(){root.classList.add('anim')})});

var lijst=JSON.parse(document.getElementById('skilllijst').textContent);
var inp=document.getElementById('zoek'),reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var i=0,j=0,weg=false;
function tik(){if(document.activeElement===inp||inp.value){setTimeout(tik,800);return}
 var w='/'+lijst[i];
 if(reduce){inp.placeholder=w;i=(i+1)%lijst.length;setTimeout(tik,2200);return}
 if(!weg){j++;inp.placeholder=w.slice(0,j);if(j>=w.length){weg=true;setTimeout(tik,1500);return}setTimeout(tik,60)}
 else{j=Math.max(1,j-2);inp.placeholder=w.slice(0,j);if(j<=1){weg=false;i=(i+1)%lijst.length;setTimeout(tik,250);return}setTimeout(tik,22)}}
tik();

var f=document.getElementById('filter'),tabs=document.querySelectorAll('.tabs button'),kaarten=document.querySelectorAll('.skill'),groep=0;
function toon(){var v=f.value.toLowerCase().replace(/^\//,'').trim(),n=0;
 tabs.forEach(function(b,k){b.setAttribute('aria-selected',String(!v&&k===groep))});
 kaarten.forEach(function(k){var ok=v?k.dataset.t.indexOf(v)>-1:+k.dataset.g===groep,was=k.hidden;k.hidden=!ok;if(ok){if(was&&!reduce){k.style.animation='none';void k.offsetWidth;k.style.animation='kin .38s cubic-bezier(.2,.7,.2,1) '+(n*28)+'ms both'}n++}});
 document.getElementById('leeg').hidden=n>0;if(window.plaats)window.plaats()}
tabs.forEach(function(b,k){b.addEventListener('click',function(){groep=k;f.value='';toon()})});
function vast(){var K=document.querySelector('.kaarten');if(!K||!kaarten)return;K.style.height='';
 if(window.matchMedia('(max-width:760px)').matches)return;
 var was=[].map.call(kaarten,function(k){return k.hidden}),mx=0;
 for(var g=0;g<tabs.length;g++){kaarten.forEach(function(k){k.hidden=+k.dataset.g!==g});mx=Math.max(mx,K.scrollHeight)}
 kaarten.forEach(function(k,x){k.hidden=was[x]});
 var cap=parseFloat(getComputedStyle(K).maxHeight);K.style.height=Math.ceil(Math.min(mx+12,isNaN(cap)?mx:cap))+'px'}
function plaats(){var B=document.getElementById('skillknoppen'),K=document.querySelector('.kaarten');if(!B||!K)return;
 if(window.matchMedia('(max-width:760px)').matches){B.style.transform='';return}
 var ch=0;kaarten.forEach(function(k){if(!k.hidden)ch=Math.max(ch,k.offsetTop+k.offsetHeight)});
 var H=K.clientHeight,sh=ch>0?Math.min(0,ch+2-H):0;B.style.transform=sh?'translateY('+Math.round(sh)+'px)':''}
window.vast=function(){vast();plaats()};window.plaats=plaats;
f.addEventListener('input',toon);toon();window.vast();addEventListener('resize',window.vast);
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(window.vast);
inp.form.addEventListener('submit',function(ev){ev.preventDefault();f.value=inp.value.replace(/^\//,'').trim();toon();
 document.getElementById('skills').scrollIntoView({behavior:reduce?'auto':'smooth'})});
})();
