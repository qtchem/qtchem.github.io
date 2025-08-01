#!/usr/bin/env python3
"""
Sort BibTeX entries by year (newest first) and citation count (highest first)
"""

import re
import os

def parse_bibtex_entries(content):
    """Parse BibTeX content and extract entries with their metadata"""
    entries = []
    
    # Split content into header and entries
    lines = content.split('\n')
    header_lines = []
    entry_lines = []
    in_header = True
    
    for line in lines:
        if line.strip().startswith('@') and not line.strip().startswith('@comment'):
            in_header = False
        
        if in_header:
            header_lines.append(line)
        else:
            entry_lines.append(line)
    
    # Join entry lines and split by @article or @inproceedings
    entry_content = '\n'.join(entry_lines)
    entry_blocks = re.split(r'\n(?=@(?:article|inproceedings))', entry_content)
    
    for block in entry_blocks:
        if not block.strip():
            continue
            
        # Extract year and citation count
        year_match = re.search(r'year=\{(\d+)\}', block)
        citation_match = re.search(r'note=\{Cited by (\d+)\}', block)
        
        year = int(year_match.group(1)) if year_match else 0
        citations = int(citation_match.group(1)) if citation_match else 0
        
        entries.append({
            'content': block.strip(),
            'year': year,
            'citations': citations
        })
    
    return '\n'.join(header_lines), entries

def sort_bibtex_file(file_path):
    """Sort BibTeX file by year (newest first) and citations (highest first)"""
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse entries
    header, entries = parse_bibtex_entries(content)
    
    # Sort entries by year (descending) then by citations (descending)
    entries.sort(key=lambda x: (x['year'], x['citations']), reverse=True)
    
    # Reconstruct the file
    sorted_content = header + '\n\n' + '\n\n'.join(entry['content'] for entry in entries) + '\n'
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(sorted_content)
    
    print(f"✅ Sorted {len(entries)} publications by year (newest first)")
    print(f"📅 Year range: {entries[0]['year']} - {entries[-1]['year']}")

if __name__ == "__main__":
    bibtex_file = "_bibliography/papers.bib"
    
    if not os.path.exists(bibtex_file):
        print(f"❌ File not found: {bibtex_file}")
        exit(1)
    
    sort_bibtex_file(bibtex_file)
