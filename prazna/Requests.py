import re
import orodja

sahist_regex = re.compile(
    r'<tr bgcolor=#.*?><td width=10>&nbsp;(?P<rank>\d+)</a></td><td>&nbsp;'
    r'(?P<ime>.*?)</td><td>&nbsp;g</td><td>&nbsp;'
    r'(?P<drzava>\w{3})</td><td>&nbsp;'
    r'(?P<rating>\d{4})</td><td>&nbsp;\d*?</td><td>&nbsp;'
    r'(?P<letnik>\d{4})</td></tr>'
    , flags=re.DOTALL)

def pocisti_sahisti(sahisti):
    infos = sahisti.groupdict()
    infos['rank'] = int(infos['rank'])
    infos['ime'] = infos['ime'].strip()
    infos['drzava'] = infos['drzava'].strip()
    infos['rating'] = int(infos['rating'])
    infos['letnik'] = int(infos['letnik'])
    return infos

def naredi_csv_datoteke():
    sahisti = []
    for html_datoteka in orodja.datoteke('lista/'):
        for sahist in re.finditer(sahist_regex, orodja.vsebina_datoteke(html_datoteka)):
            sahisti.append(pocisti_sahisti(sahist))
    return sahisti

sahisti = naredi_csv_datoteke()
orodja.zapisi_tabelo(sahisti, ['rank', 'ime', 'drzava', 'rating', 'letnik'], 'sahisti.csv')


