// Cut Paper: the hero layers drift apart as you scroll. Off for reduced motion.
(function(){
  if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  var layers=[].slice.call(document.querySelectorAll('.scene .layer[data-depth]'));if(!layers.length)return;
  var tick=false;
  function run(){var y=window.scrollY;layers.forEach(function(l){l.style.transform='translate3d(0,'+(y*parseFloat(l.dataset.depth)*-0.35)+'px,0)';});tick=false;}
  window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(run);}},{passive:true});
})();
