"""Reproducible source corrections, applied before publication hashes are computed."""
import json
from pathlib import Path

def correct_text(name, text):
    records=json.loads(Path(__file__).with_name('morphic_corrections_2026_09_25.json').read_text())
    for entry in records[name]:
        before,after=entry['before'],entry['after']
        if before in text:
            if text.count(before)!=1: raise ValueError('ambiguous correction context: '+name)
            text=text.replace(before,after,1)
        elif after not in text:
            raise ValueError('correction source context changed: '+name)
    return text
