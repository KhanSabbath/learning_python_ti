## Muitos sites têm APis públicas que oferecem feeds de dados usando JSON ou outro formato. Para baixá-las
## Precimos utilizar o pacote "request" (http://docs.python-requests.org)
import request
url =  'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = request.get(url)
resp
#OUT:       <response [200]

## O método json do objeto Response devolverá um dicionário contendo o parse dos dados JSON em objetos Python nativos
data = resp.json()
data[0]['title']  # OUT:  rank  with +-inf,  #6945'


## Podemos passar data diretamente para DataFrame e extrair os campos de interesse:
issues = pd.Dataframe(data, columns=['number' ,'title', 'labels', 'state'])
issues












##      OUT: number title\ 
# 0 17903 BUG: rank wi.th +-i.nf, #6945
# 1 17902 Revert "ERR: Rai.se ValueError when setti.ng sca .. .
# 2 17901 Wrong ori.entati.on of operati.ons between DataFr . . .
# 3 17900 added 'i.nfer' opti.on to co111pressi.on i.n _get_ha .. .
# 4 17898 Last day of 111onth should group wi.th that 111onth
# .. . . .. 
# 25 17854 Addi.ng an i.nteger-locati.on based "get" 111ethod
# 26 17853 BUG: adds vali.dati.on for boolean keywords i.n D .. .
# 27 17851 BUG: dupli.cate i.ndexi.ng wi.th e111bedded non-orde .. .
# 28 17850 I111portError: No 111odule na111ed 'pandas.plotti.ng'
# 29 17846 BUG: Ignore di.vi.si.on by 0 when 111ergi.ng e111pty d ...
# labels state
# 0 [] open
# 1 [{'i.d': 35818298, 'url': 'https://api..gi.thub.c ... open
# 2 [] open
# 3 [] open
# 4 ({'i.d': 76811, 'url': 'https://api..github.co111/ ... open
# .. . . .. 
# 25 [ { 1 i.d' : 35818298, 'url': ' https://api. .gi.thub.c . .. open
# 26 [ { 1 i.d' : 42670965, 'url': 'https://api..gi.thub.c ... open
# 27 [ { 1 i.d' : 76811, 'url': 'https://api..gi.thub. co111/ ... open
# 28 [ { 'i.d' : 31932467, 'url': ' https://api..gi.thub .c ... open
# 29 [ { 1 i.d ' : 76865106, 'url': ' https://api. .gi.thub.c ... open
# [30 rows x 4 colu111ns] 
