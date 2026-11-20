// Theme toggle and image viewer. Everything works without this file.
(function(){
  var root=document.documentElement,btn=document.querySelector('.theme');
  try{var t=localStorage.getItem('theme');if(t)root.setAttribute('data-theme',t);}catch(e){}
  if(btn)btn.addEventListener('click',function(){
    var cur=root.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
    var next=cur==='dark'?'light':'dark';root.setAttribute('data-theme',next);
    try{localStorage.setItem('theme',next);}catch(e){}
  });
  var lb=document.getElementById('lb');if(!lb||!lb.showModal)return;
  var li=lb.querySelector('img'),lp=lb.querySelector('p');
  function open(src,alt,txt){li.src=src;li.alt=alt;lp.textContent=txt||alt;lb.showModal();}
  document.addEventListener('click',function(ev){
    var b=ev.target.closest('button.open');
    if(b){var im=b.querySelector('img');open(im.dataset.full,im.alt,b.dataset.title+'. '+b.dataset.text);return;}
    var im=ev.target.closest('img[data-full]');
    if(im&&!im.closest('summary')&&!im.closest('.card')){open(im.dataset.full,im.alt);}
  });
  lb.addEventListener('click',function(e){if(e.target===lb||e.target===li)lb.close();});
})();
