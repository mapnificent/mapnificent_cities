import json
import sys
import os

import yaml
import html2text


def ydump(e):
    return yaml.safe_dump(e, allow_unicode=True, default_flow_style=False, encoding='utf-8', width=10000)


def to_md(html):
    h = html2text.HTML2Text()
    h.body_width = 0
    return h.handle(html)


def main(filename, outpath):
    for city in json.load(file(filename)):
        sys.stderr.write(city['cityid'] + '\n')
        filename = os.path.join(outpath, '%s.md' % city['cityid'])
        copyright = to_md(city.pop('copyright'))
        city.pop('pending', None)
        city.pop('active', None)
        city.pop('hidden', None)
        city['northwest'] = {'lat': city.pop('nwlat'), 'lng': city.pop('nwlng')}
        city['southeast'] = {'lat': city.pop('selat'), 'lng': city.pop('selng')}
        city['options'] = json.loads(city['options'])['urbanDistance']
        with file(filename, 'w') as f:
            f.write('---\n')
            f.write(ydump(city))
            f.write('\n---\n\n')
            f.write(copyright.replace('\\-', '-').encode('utf-8'))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
