import random, math, pathlib
root=pathlib.Path('/mnt/data/atelier-cookie-projet/assets')
flavors={
 'chocolat': {'base':'#b77b4a','light':'#eac094','edge':'#90552f','chips':'#493028','crum':'#71442b','drizzle':False},
 'pistache': {'base':'#bc9e66','light':'#e6d5a6','edge':'#8f7943','chips':'#607c43','crum':'#7a5f35','drizzle':True},
 'caramel': {'base':'#bb7b45','light':'#e9b981','edge':'#91502d','chips':'#764122','crum':'#a46d35','drizzle':True},
 'framboise': {'base':'#c69b79','light':'#ecd0b0','edge':'#9b7255','chips':'#8a273b','crum':'#78412f','drizzle':True},
}
for name,c in flavors.items():
 rng=random.Random({'chocolat':12,'pistache':24,'caramel':38,'framboise':57}[name]); fragments=[]
 # baked edge freckles
 for i in range(175):
  a=rng.uniform(0,math.tau); r=math.sqrt(rng.random())*195; x=300+math.cos(a)*r; y=295+math.sin(a)*r*.92
  size=rng.uniform(.5,3.0)
  fragments.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size:.1f}" fill="{c["crum"]}" opacity="{rng.uniform(.09,.37):.2f}"/>')
 # visible chocolate chunks or nuts
 for i in range(31 if name=='chocolat' else 26):
  a=rng.uniform(0,math.tau); r=math.sqrt(rng.random())*168; x=300+math.cos(a)*r; y=290+math.sin(a)*r*.86
  rx=rng.uniform(6,17); ry=rng.uniform(4,11); rot=rng.uniform(-70,70)
  color=c['chips']
  if name=='pistache' and i%4==0: color='#e5e0be'
  if name=='caramel' and i%4==0: color='#f7d39a'
  if name=='framboise' and i%4==0: color='#fae0d0'
  fragments.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" transform="rotate({rot:.1f} {x:.1f} {y:.1f})" fill="{color}" opacity="{rng.uniform(.74,.99):.2f}"/>')
  fragments.append(f'<ellipse cx="{x-1.2:.1f}" cy="{y-1.1:.1f}" rx="{rx*.4:.1f}" ry="{ry*.18:.1f}" transform="rotate({rot:.1f} {x:.1f} {y:.1f})" fill="#fff5dc" opacity=".26"/>')
 # irregular circle outline
 points=[]
 for i in range(90):
  a=math.tau*i/90; r=211+6*math.sin(11*a)+5*math.sin(19*a+1.4)+3*math.sin(29*a+.9)
  points.append(f'{300+r*math.cos(a):.1f},{295+.92*r*math.sin(a):.1f}')
 outline=' '.join(points)
 caramel=''
 if name=='caramel':
  caramel='<path d="M193 246 C255 220 285 338 356 271 S403 244 424 285" fill="none" stroke="#e8aa54" stroke-width="19" opacity=".65" stroke-linecap="round"/><path d="M218 351 C295 299 336 389 401 329" fill="none" stroke="#e6a75b" stroke-width="14" opacity=".68" stroke-linecap="round"/>'
 if name=='framboise':
  caramel='<path d="M189 279 C237 234 300 335 355 287 S410 273 420 309" fill="none" stroke="#af5067" stroke-width="17" opacity=".50" stroke-linecap="round"/><path d="M222 360 C282 306 331 370 399 334" fill="none" stroke="#b74e69" stroke-width="12" opacity=".55" stroke-linecap="round"/>'
 if name=='pistache':
  caramel='<path d="M208 266 C284 207 303 351 389 278" fill="none" stroke="#d4c6a4" stroke-width="13" opacity=".5" stroke-linecap="round"/>'
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600" role="img" aria-label="Illustration originale de cookie {name}">
 <defs>
 <radialGradient id="biscuit" cx="36%" cy="28%" r="78%"><stop stop-color="{c['light']}"/><stop offset=".54" stop-color="{c['base']}"/><stop offset=".85" stop-color="{c['base']}"/><stop offset="1" stop-color="{c['edge']}"/></radialGradient>
 <radialGradient id="shine" cx="28%" cy="18%" r="73%"><stop stop-color="#fff5da" stop-opacity=".40"/><stop offset="1" stop-color="#fff5da" stop-opacity="0"/></radialGradient>
 <filter id="shadow" x="-35%" y="-35%" width="180%" height="190%"><feGaussianBlur stdDeviation="17"/></filter>
 </defs>
 <ellipse cx="306" cy="514" rx="186" ry="37" fill="#2e1810" opacity=".20" filter="url(#shadow)"/>
 <g transform="rotate(-9 300 295)">
 <polygon points="{outline}" fill="{c['edge']}" transform="translate(0 10)" opacity=".9"/>
 <polygon points="{outline}" fill="url(#biscuit)"/>
 <ellipse cx="267" cy="246" rx="153" ry="123" fill="url(#shine)"/>
 {caramel}
 {''.join(fragments)}
 </g></svg>'''
 (root/f'cookie-{name}.svg').write_text(svg, encoding='utf-8')
print('Assets created:', len(flavors))
