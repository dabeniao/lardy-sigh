import sys
#import fileinput
import os
#import shutil

SHOW_ORPHAN_REQUESTS = False

def doLds(search_terms, files):
    columns = 80
    #columns = shutil.get_terminal_size((80, 24)).columns

    pending = dict()
    num_search_terms = len(search_terms)
    search_enabled = num_search_terms > 0

    hr = '=' * columns
    print(hr)

    #with fileinput.input(files=files) as fp:
    #    for line in fp:
    for line in sys.stdin:
        hashtag_idx = line.find('#')
        if hashtag_idx < 0:
            continue
        rp_idx = line.find(']', hashtag_idx)
        if rp_idx < 0:
            continue

        pid = line[hashtag_idx + 1: rp_idx]
        req = pending.get(pid, '')

        time = line[line.find('[') + 1: hashtag_idx]
        log = line[line.find(':', rp_idx) + 1:].strip()

        req = ''.join([req, time, log, '\n'])
        pending[pid] = req

        if 'Completed' in log or 'Performed' in log or 'FATAL' in line:
            pending.pop(pid)
            if sum(term in req for term in search_terms) == num_search_terms:
                print(req + hr)
    if SHOW_ORPHAN_REQUESTS and pending:
        ohr = '-' * columns
        print(ohr)
        print ('Orphan Requests:')
        print(ohr)
        for pid, req in pending.items():
            if sum(term in req for term in search_terms) == num_search_terms:
                print(req + ohr)


if __name__ == '__main__':
    search_terms = []
    files = []
    if len(sys.argv) > 1:
        for term in sys.argv[1::]:
            if os.path.isfile(term):
                files.append(term)
            else:
                print(term)
                search_terms.append(term)
    doLds(search_terms, files)

