// één gedeeld cursorspoor (viewport-coordinaten): elk scherm tekent het stuk binnen zijn eigen vlak, zodat het naadloos over de schermen loopt
window.Spoor=(function(){var o={A:0,f:-1,pts:[],gezien:false,luist:[]};for(var i=0;i<7;i++)o.pts.push({x:0,y:0});var lx=0,ly=0;
 o.step=function(nu){if(nu===o.f)return;o.f=nu;if(o.A<=0)return;
  for(var j=0;j<o.pts.length;j++){var v=j?o.pts[j-1]:{x:lx,y:ly},p=o.pts[j];p.x+=(v.x-p.x)*.3;p.y+=(v.y-p.y)*.3}
  o.A=Math.max(0,o.A-.012)};
 addEventListener('pointermove',function(ev){if(!o.gezien||o.A<=0)o.pts.forEach(function(p){p.x=ev.clientX;p.y=ev.clientY});
  lx=ev.clientX;ly=ev.clientY;o.A=1;o.gezien=true;o.luist.forEach(function(f){f()})},{passive:true});
 return o})();
// cursorspoor op scherm 2 en 3: tekent het gedeelde spoor, begrensd door het eigen vlak
(function(){if(window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
['start','werking','skills'].forEach(function(id){var sec=document.getElementById(id);if(!sec)return;
 var cv=document.createElement('canvas');cv.className='spoorvlak';cv.setAttribute('aria-hidden','true');sec.insertBefore(cv,sec.firstChild);
 var c=cv.getContext('2d'),W=0,H=0,DPR=1,loopt=false,zicht=false;
 function maat(){var r=sec.getBoundingClientRect();DPR=Math.min(window.devicePixelRatio||1,1.5);W=r.width;H=r.height;cv.width=Math.round(W*DPR);cv.height=Math.round(H*DPR)}
 function vlek(x,y,r,k,a){var g=c.createRadialGradient(x,y,0,x,y,r);g.addColorStop(0,'rgba('+k+','+a+')');g.addColorStop(.4,'rgba('+k+','+(a*.9)+')');
  g.addColorStop(.72,'rgba('+k+','+(a*.35)+')');g.addColorStop(1,'rgba('+k+',0)');c.fillStyle=g;c.fillRect(x-r,y-r,2*r,2*r)}
 function stap(nu){Spoor.step(nu);c.setTransform(DPR,0,0,DPR,0,0);c.clearRect(0,0,W,H);
  if(Spoor.A>0&&zicht){var r=sec.getBoundingClientRect(),P=Spoor.pts;if(Math.abs(r.height-H)>2||Math.abs(r.width-W)>2)maat();
   for(var k=P.length-1;k>=0;k--){var w=1-k/P.length;vlek(P[k].x-r.left,P[k].y-r.top,24+30*w,w>.5?'72,202,228':'255,255,0',.7*w*Spoor.A)}}
  if(Spoor.A>0)requestAnimationFrame(stap);else loopt=false}
 function start(){if(!loopt){loopt=true;requestAnimationFrame(stap)}}
 addEventListener('resize',maat);maat();Spoor.luist.push(start);
 if('IntersectionObserver' in window)new IntersectionObserver(function(e){zicht=e[0].isIntersecting}).observe(sec);else zicht=true;
});
})();
