"""Bundle the interface so buttons do not depend on a separate app.js request.
Run python3 build.py after editing app.js, style.css or index.template.html.
"""
from pathlib import Path
root=Path(__file__).resolve().parent
public=root/'dist' if (root/'dist').is_dir() else root
boot='''<script>
window.fitYouBooted=false;
window.fitYouStartupError=function(message){
 var el=document.getElementById('status');
 if(el) el.textContent='FitYou could not start: '+message+' Open the full HTTPS page in Safari or Chrome, and check the deployed files.';
};
window.addEventListener('error',function(event){if(!window.fitYouBooted)window.fitYouStartupError(event.message||'a required script was blocked');});
window.setTimeout(function(){if(!window.fitYouBooted)window.fitYouStartupError('JavaScript did not initialise');},7000);
</script>
<noscript><p role="alert">FitYou needs JavaScript. Enable JavaScript in your browser and open the full HTTPS website.</p></noscript>'''
css=(public/'style.css').read_text()
js=(public/'app.js').read_text()
assert '</script' not in js.lower()
page=(public/'index.template.html').read_text().replace('<!-- FITYOU_STYLE -->','<style>\n'+css+'\n</style>').replace('<!-- FITYOU_BOOT -->',boot).replace('<!-- FITYOU_APP -->','<script>\n(function(){\n'+js+'\n})();\n</script>')
assert '<!-- FITYOU_' not in page
(public/'index.html').write_text(page)
print('Bundled FitYou interface:',public/'index.html')
