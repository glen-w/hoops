"""Markdown matrix of Zotero data-source rows with access flags.

Usage: python3 -I source_matrix.py ds.json

ds.json is a list of {p, title, url, abs}, copied from the tick ds block.
Flags are keyword matches on the abs text only. They are triage hints, not
license findings. Read the cited ToS before redistributing any data.
"""
import json
import sys

FLAGS = {
    'R': ('r package', 'r interface'),
    'Python': ('python',),
    'scrape': ('scrape', 'scraper'),
    'paywall': ('subscription', 'premium', 'paywall'),
    'tos-check': (' tos', 'license', 'redistribut', 'terms'),
}


def flags(text):
    low = ' ' + text.lower()
    return [k for k, words in FLAGS.items() if any(w in low for w in words)]


def main(path):
    with open(path, encoding='utf-8') as f:
        rows = json.load(f)
    print('| title | flags | url | zotero path |')
    print('|---|---|---|---|')
    for r in rows:
        fl = ', '.join(flags(r.get('abs', ''))) or '-'
        print('| %s | %s | %s | %s |' % (r['title'], fl, r['url'], r['p']))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: source_matrix.py ds.json')
    main(sys.argv[1])
