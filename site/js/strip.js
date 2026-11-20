// The Timeline: on wide screens, a vertical wheel travels along the strip.
(function(){
  var s=document.getElementById('strip');if(!s)return;
  var wide=matchMedia('(min-width:60rem)');var r=s.querySelector('.river');function fit(){if(r)r.style.width=(wide.matches?s.scrollWidth:s.clientWidth)+'px';}fit();addEventListener('resize',fit);addEventListener('load',fit);
  s.addEventListener('wheel',function(e){
    if(!wide.matches||Math.abs(e.deltaY)<Math.abs(e.deltaX))return;
    var max=s.scrollWidth-s.clientWidth;
    if((e.deltaY>0&&s.scrollLeft<max-1)||(e.deltaY<0&&s.scrollLeft>0)){s.scrollLeft+=e.deltaY;e.preventDefault();}
  },{passive:false});
  document.querySelectorAll('.legend a').forEach(function(a){a.addEventListener('click',function(e){
    if(!wide.matches)return;var t=document.querySelector(a.getAttribute('href'));if(!t)return;
    e.preventDefault();s.scrollTo({left:t.offsetLeft-s.offsetLeft,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});t.setAttribute('tabindex','-1');t.focus({preventScroll:true});
  });});
})();
