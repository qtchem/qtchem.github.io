#!/usr/bin/env python3
"""
Automated Publications Updater for Heidar-Zadeh Group Website

This script automatically fetches publication data from Google Scholar
and updates the papers.bib file for the Jekyll website.

Usage:
    python update_publications.py

    # To disable automatic updates (useful for local development):
    DISABLE_AUTO_UPDATE=true python update_publications.py

    # To force enable updates:
    DISABLE_AUTO_UPDATE=false python update_publications.py

Environment Variables:
    DISABLE_AUTO_UPDATE: Set to 'true' to disable automatic updates
                        (ignored in GitHub Actions - updates always run)
    GITHUB_ACTIONS: Automatically set by GitHub Actions workflow

Requirements:
    pip install requests beautifulsoup4

Author: Heidar-Zadeh Group Website Automation
"""

import os
import sys
import json
import time
import re
from datetime import datetime
from urllib.parse import quote, unquote

try:
    import requests
    from bs4 import BeautifulSoup
    import json
except ImportError:
    print("Required packages not installed. Please run:")
    print("pip install requests beautifulsoup4")
    sys.exit(1)

# Configuration
SCHOLAR_ID = "JlIWcccAAAAJ"  # Prof. Farnaz Heidar-Zadeh's Google Scholar ID
BIBLIOGRAPHY_DIR = "_bibliography"
BIBTEX_FILE = "papers.bib"
BIB_FILE_PATH = os.path.join(BIBLIOGRAPHY_DIR, BIBTEX_FILE)
BACKUP_FILE_PATH = os.path.join(BIBLIOGRAPHY_DIR, f"{BIBTEX_FILE}.backup")

# Journal abbreviation cache
JOURNAL_ABBR_CACHE = {}

# Common journal abbreviations (manually curated for chemistry/physics journals)
COMMON_JOURNAL_ABBR = {
    "Journal of Chemical Physics": "J. Chem. Phys.",
    "Journal of Physical Chemistry": "J. Phys. Chem.",
    "Journal of the American Chemical Society": "J. Am. Chem. Soc.",
    "Angewandte Chemie International Edition": "Angew. Chem. Int. Ed.",
    "Chemical Reviews": "Chem. Rev.",
    "Nature": "Nature",
    "Science": "Science",
    "Physical Review Letters": "Phys. Rev. Lett.",
    "Physical Review A": "Phys. Rev. A",
    "Physical Review B": "Phys. Rev. B",
    "Chemical Science": "Chem. Sci.",
    "Journal of Computational Chemistry": "J. Comput. Chem.",
    "Journal of Chemical Theory and Computation": "J. Chem. Theory Comput.",
    "Theoretical Chemistry Accounts": "Theor. Chem. Acc.",
    "International Journal of Quantum Chemistry": "Int. J. Quantum Chem.",
    "Molecular Physics": "Mol. Phys.",
    "Chemical Physics Letters": "Chem. Phys. Lett.",
    "Journal of Molecular Structure": "J. Mol. Struct.",
    "Computational and Theoretical Chemistry": "Comput. Theor. Chem.",
    "Journal of Physical Chemistry A": "J. Phys. Chem. A",
    "Journal of Physical Chemistry B": "J. Phys. Chem. B",
    "Journal of Physical Chemistry C": "J. Phys. Chem. C",
    "Proceedings of the National Academy of Sciences": "Proc. Natl. Acad. Sci.",
    "Journal of Medicinal Chemistry": "J. Med. Chem.",
    "Organic Letters": "Org. Lett.",
    "Journal of Organic Chemistry": "J. Org. Chem.",
    "Inorganic Chemistry": "Inorg. Chem.",
    "Organometallics": "Organometallics",
}

def get_journal_abbreviation(journal_name):
    """Get journal abbreviation using common abbreviations and LTWA-style rules"""
    if not journal_name:
        return ""

    # Check cache first
    if journal_name in JOURNAL_ABBR_CACHE:
        return JOURNAL_ABBR_CACHE[journal_name]

    # Check common abbreviations
    if journal_name in COMMON_JOURNAL_ABBR:
        abbr = COMMON_JOURNAL_ABBR[journal_name]
        JOURNAL_ABBR_CACHE[journal_name] = abbr
        return abbr

    # Apply basic LTWA-style abbreviation rules
    abbr = apply_ltwa_rules(journal_name)
    JOURNAL_ABBR_CACHE[journal_name] = abbr
    return abbr

def apply_ltwa_rules(journal_name):
    """Apply basic LTWA (List of Title Word Abbreviations) rules"""
    # Common word abbreviations based on LTWA
    word_abbr = {
        'journal': 'J.',
        'american': 'Am.',
        'chemical': 'Chem.',
        'chemistry': 'Chem.',
        'physical': 'Phys.',
        'physics': 'Phys.',
        'society': 'Soc.',
        'international': 'Int.',
        'science': 'Sci.',
        'letters': 'Lett.',
        'communications': 'Commun.',
        'proceedings': 'Proc.',
        'national': 'Natl.',
        'academy': 'Acad.',
        'molecular': 'Mol.',
        'theoretical': 'Theor.',
        'computational': 'Comput.',
        'accounts': 'Acc.',
        'research': 'Res.',
        'materials': 'Mater.',
        'applied': 'Appl.',
        'organic': 'Org.',
        'inorganic': 'Inorg.',
        'analytical': 'Anal.',
        'biological': 'Biol.',
        'biochemical': 'Biochem.',
        'medicinal': 'Med.',
        'pharmaceutical': 'Pharm.',
        'european': 'Eur.',
        'review': 'Rev.',
        'reviews': 'Rev.',
        'annual': 'Annu.',
        'quarterly': 'Q.',
        'monthly': 'Mon.',
        'weekly': 'Wkly.',
    }

    words = journal_name.split()
    abbreviated_words = []

    for word in words:
        word_lower = word.lower().rstrip('.,;:')
        if word_lower in word_abbr:
            abbreviated_words.append(word_abbr[word_lower])
        elif len(word) > 4:  # Abbreviate longer words
            abbreviated_words.append(word[:4] + '.')
        else:
            abbreviated_words.append(word)

    return ' '.join(abbreviated_words)

def fetch_publication_details(pub_data, session):
    """Fetch additional details for a publication from its Google Scholar page"""
    if not pub_data.get('scholar_url'):
        return pub_data

    try:
        # Add longer delay and retry logic to handle anti-bot measures
        time.sleep(3)

        # Use more realistic headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

        # Retry logic for failed requests
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = session.get(pub_data['scholar_url'], headers=headers, timeout=30)
                if response.status_code == 200:
                    break
                elif response.status_code == 429:  # Rate limited
                    print(f"  ⚠️  Rate limited, waiting {(attempt + 1) * 5} seconds...")
                    time.sleep((attempt + 1) * 5)
                    continue
                else:
                    print(f"  ⚠️  HTTP {response.status_code} for {pub_data.get('title', 'Unknown')}")
                    if attempt == max_retries - 1:
                        return pub_data
                    time.sleep(2)
                    continue
            except requests.RequestException as e:
                print(f"  ⚠️  Request failed (attempt {attempt + 1}): {e}")
                if attempt == max_retries - 1:
                    return pub_data
                time.sleep(2)
                continue

        soup = BeautifulSoup(response.content, 'html.parser')

        # Try to extract abstract
        abstract_div = soup.find('div', {'id': 'gsc_oci_merged_snippet'})
        if abstract_div:
            pub_data['abstract'] = clean_bibtex_string(abstract_div.get_text().strip())

        # Try to extract DOI and other metadata from citation details
        citation_table = soup.find('table', {'id': 'gsc_oci_table'})
        if citation_table:
            rows = citation_table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) >= 2:
                    field = cells[0].get_text().strip().lower()
                    value = cells[1].get_text().strip()

                    if 'journal' in field:
                        pub_data['journal'] = clean_bibtex_string(value)
                        pub_data['abbr'] = get_journal_abbreviation(value)
                    elif 'volume' in field:
                        pub_data['volume'] = value
                    elif 'issue' in field or 'number' in field:
                        pub_data['number'] = value
                    elif 'pages' in field:
                        pub_data['pages'] = value.replace('-', '--')  # BibTeX style
                    elif 'publisher' in field:
                        pub_data['publisher'] = clean_bibtex_string(value)
                    elif 'doi' in field:
                        pub_data['doi'] = value

        # Try to find external links
        links = soup.find_all('a', href=True)
        for link in links:
            href = link.get('href', '')
            if 'doi.org' in href:
                pub_data['doi'] = href.split('doi.org/')[-1]
            elif 'arxiv.org' in href:
                pub_data['arxiv'] = href
            elif href.endswith('.pdf'):
                pub_data['pdf'] = href

    except Exception as e:
        print(f"  ⚠️  Could not fetch details: {e}")

    return pub_data

def backup_existing_bib():
    """Create a backup of the existing papers.bib file"""
    if os.path.exists(BIB_FILE_PATH):
        import shutil
        shutil.copy2(BIB_FILE_PATH, BACKUP_FILE_PATH)
        print(f"✓ Backup created: {BACKUP_FILE_PATH}")

def get_scholar_publications():
    """Fetch publications from Google Scholar using direct scraping"""
    print(f"🔍 Fetching publications for Scholar ID: {SCHOLAR_ID}")

    # Set up session with headers to mimic a real browser
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    })

    try:
        # Construct the Google Scholar URL
        base_url = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en&cstart=0&pagesize=100"

        print(f"📡 Requesting: {base_url}")

        # Use much more aggressive retry strategy with longer delays
        max_retries = 5
        response = None

        for attempt in range(max_retries):
            try:
                print(f"  Attempt {attempt + 1}/{max_retries}...")

                # Progressive delay: 5s, 15s, 30s, 60s, 120s
                delay = min(5 * (2 ** attempt), 120)
                print(f"  Waiting {delay} seconds to avoid rate limiting...")
                time.sleep(delay)

                # Rotate User-Agent strings to appear more natural
                user_agents = [
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'
                ]
                session.headers.update({'User-Agent': user_agents[attempt % len(user_agents)]})

                response = session.get(base_url, timeout=45)

                if response.status_code == 200:
                    print(f"  ✅ Success on attempt {attempt + 1}")
                    break
                elif response.status_code == 429:  # Rate limited
                    wait_time = (attempt + 1) * 30
                    print(f"  ⚠️  Rate limited, waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                    continue
                elif response.status_code == 503:  # Service unavailable
                    wait_time = (attempt + 1) * 20
                    print(f"  ⚠️  Service unavailable, waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                    continue
                else:
                    print(f"  ⚠️  HTTP {response.status_code}, retrying...")
                    if attempt == max_retries - 1:
                        print(f"  ❌ Failed after {max_retries} attempts with status {response.status_code}")
                        raise requests.RequestException(f"Failed after {max_retries} attempts")
                    continue

            except requests.RequestException as e:
                print(f"  ⚠️  Request failed (attempt {attempt + 1}): {e}")
                if attempt == max_retries - 1:
                    print(f"  ❌ All {max_retries} attempts failed")
                    raise
                continue

        if not response or response.status_code != 200:
            raise requests.RequestException("Failed to get valid response from Google Scholar")

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find author name
        author_name = "Unknown Author"
        name_element = soup.find('div', {'id': 'gsc_prf_in'})
        if name_element:
            author_name = name_element.get_text().strip()
            print(f"✓ Found author: {author_name}")

        # Find publication entries
        publications = []
        pub_table = soup.find('table', {'id': 'gsc_a_t'})

        if not pub_table:
            print("❌ Could not find publications table")
            return []

        rows = pub_table.find_all('tr', class_='gsc_a_tr')
        print(f"✓ Found {len(rows)} publications")

        for i, row in enumerate(rows):
            try:
                pub_data = parse_publication_row(row, session)
                if pub_data:
                    print(f"  📄 {i+1}/{len(rows)}: {pub_data.get('title', 'Unknown title')}")
                    publications.append(pub_data)

            except Exception as e:
                print(f"  ⚠️  Error parsing publication {i+1}: {e}")
                continue

        print(f"📊 Processing {len(publications)} publications with basic metadata...")
        print("  ⚠️  Skipping detailed metadata fetching to avoid rate limiting")
        print("  ✓ Using citation counts and basic info from main page")

        # Just add basic journal abbreviations for known journals
        for i, pub in enumerate(publications):
            if pub.get('venue'):
                pub['abbr'] = get_journal_abbreviation(pub['venue'])
                pub['journal'] = pub['venue']

        # Sort publications by year (newest first), then by citation count (highest first)
        publications.sort(key=lambda x: (x.get('year', 0), x.get('citations', 0)), reverse=True)

        return publications

    except requests.RequestException as e:
        print(f"❌ Network error fetching from Google Scholar: {e}")
        return []
    except Exception as e:
        print(f"❌ Error fetching from Google Scholar: {e}")
        return []

def parse_publication_row(row, session):
    """Parse a single publication row from Google Scholar"""
    pub_data = {}

    # Get title and link
    title_cell = row.find('td', class_='gsc_a_t')
    if title_cell:
        title_link = title_cell.find('a', class_='gsc_a_at')
        if title_link:
            pub_data['title'] = title_link.get_text().strip()
            pub_data['scholar_url'] = "https://scholar.google.com" + title_link.get('href', '')

        # Get authors and venue info
        author_info = title_cell.find('div', class_='gs_gray')
        if author_info:
            author_text = author_info.get_text().strip()
            pub_data['authors_raw'] = author_text

            # Try to separate authors from venue
            parts = author_text.split(' - ')
            if len(parts) >= 2:
                pub_data['authors'] = parts[0].strip()
                pub_data['venue'] = parts[1].strip()
            else:
                pub_data['authors'] = author_text

    # Get citation count
    citation_cell = row.find('td', class_='gsc_a_c')
    if citation_cell:
        citation_link = citation_cell.find('a', class_='gsc_a_ac')
        if citation_link:
            citation_text = citation_link.get_text().strip()
            if citation_text.isdigit():
                pub_data['citations'] = int(citation_text)

    # Get year
    year_cell = row.find('td', class_='gsc_a_y')
    if year_cell:
        year_span = year_cell.find('span', class_='gsc_a_h')
        if year_span:
            year_text = year_span.get_text().strip()
            if year_text.isdigit():
                pub_data['year'] = int(year_text)

    return pub_data if pub_data.get('title') else None

def format_author_name(author_name):
    """Format author name for BibTeX"""
    # Handle special characters and formatting
    name = author_name.replace("*", "").replace("†", "").strip()

    # Split name into parts
    parts = name.split()
    if len(parts) >= 2:
        last_name = parts[-1]
        first_names = " ".join(parts[:-1])
        return f"{last_name}, {first_names}"
    return name

def generate_bibtex_key(title, year):
    """Generate a unique BibTeX key"""
    # Clean title and take first few words
    clean_title = ''.join(c for c in title if c.isalnum() or c.isspace())
    words = clean_title.split()[:3]
    key_base = ''.join(words).lower()
    return f"heidarzadeh{year}{key_base}"

def publication_to_bibtex(pub):
    """Convert a scraped publication to comprehensive BibTeX format"""

    # Extract basic information
    title = pub.get('title', 'Unknown Title')
    year = pub.get('year', datetime.now().year)
    authors_raw = pub.get('authors', '')
    venue = pub.get('venue', '')

    # Clean and format title
    title = clean_bibtex_string(title)

    # Generate BibTeX key
    bib_key = generate_bibtex_key(title, year)

    # Format authors
    authors_str = format_authors_for_bibtex(authors_raw)

    # Determine publication type and venue
    pub_type = "article"  # Default
    journal = pub.get('journal', venue if venue else '')
    booktitle = ""

    # Use more sophisticated venue detection
    if venue or journal:
        venue_text = (journal or venue).lower()
        conference_keywords = ['conference', 'proceedings', 'symposium', 'workshop', 'meeting', 'proc', 'congress', 'summit']
        if any(keyword in venue_text for keyword in conference_keywords):
            pub_type = "inproceedings"
            booktitle = clean_bibtex_string(journal or venue)
            journal = ""  # Clear journal for conference papers
        else:
            journal = clean_bibtex_string(journal or venue)

    # Build comprehensive BibTeX entry
    bibtex_lines = [f"@{pub_type}{{{bib_key},"]

    # Essential display flags
    bibtex_lines.append(f"  bibtex_show={{true}},")

    # Mark highly cited papers as selected
    if pub.get('citations', 0) > 50:
        bibtex_lines.append(f"  selected={{true}},")

    bibtex_lines.append("")

    # Core publication information
    bibtex_lines.append(f"  title={{{title}}},")

    if authors_str:
        bibtex_lines.append(f"  author={{{authors_str}}},")

    # Journal/Conference information
    if journal:
        bibtex_lines.append(f"  journal={{{journal}}},")
    if booktitle:
        bibtex_lines.append(f"  booktitle={{{booktitle}}},")

    # Volume, number, pages
    if pub.get('volume'):
        bibtex_lines.append(f"  volume={{{pub['volume']}}},")
    if pub.get('number'):
        bibtex_lines.append(f"  number={{{pub['number']}}},")
    if pub.get('pages'):
        bibtex_lines.append(f"  pages={{{pub['pages']}}},")

    # Year and month
    bibtex_lines.append(f"  year={{{year}}},")

    # Publisher
    if pub.get('publisher'):
        bibtex_lines.append(f"  publisher={{{pub['publisher']}}},")

    bibtex_lines.append("")

    # DOI and URLs
    if pub.get('doi'):
        bibtex_lines.append(f"  doi={{{pub['doi']}}},")

    if pub.get('scholar_url'):
        bibtex_lines.append(f"  url={{{pub['scholar_url']}}},")

    if pub.get('arxiv'):
        bibtex_lines.append(f"  arxiv={{{pub['arxiv']}}},")

    if pub.get('pdf'):
        bibtex_lines.append(f"  pdf={{{pub['pdf']}}},")

    bibtex_lines.append("")

    # Abstract
    if pub.get('abstract'):
        # Truncate very long abstracts
        abstract = pub['abstract']
        if len(abstract) > 500:
            abstract = abstract[:500] + "..."
        bibtex_lines.append(f"  abstract={{{abstract}}},")
        bibtex_lines.append("")

    # Journal abbreviation
    if pub.get('abbr'):
        bibtex_lines.append(f"  abbr={{{pub['abbr']}}},")

    # Metrics and identifiers
    if pub.get('citations'):
        bibtex_lines.append(f"  note={{Cited by {pub['citations']}}},")

    # Google Scholar ID (extract from URL)
    if pub.get('scholar_url'):
        scholar_match = re.search(r'citation_for_view=([^&]+)', pub['scholar_url'])
        if scholar_match:
            scholar_id = scholar_match.group(1).split(':')[-1]
            bibtex_lines.append(f"  google_scholar_id={{{scholar_id}}},")

    # Remove trailing comma from last entry and close
    if bibtex_lines[-1].endswith(','):
        bibtex_lines[-1] = bibtex_lines[-1][:-1]

    bibtex_lines.append("}")

    return "\n".join(bibtex_lines)

def clean_bibtex_string(text):
    """Clean a string for use in BibTeX"""
    if not text:
        return ""

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text.strip())

    # Handle special characters that might break BibTeX
    # Keep basic punctuation but escape problematic characters
    text = text.replace('{', '').replace('}', '')

    return text

def format_authors_for_bibtex(authors_raw):
    """Format author string for BibTeX"""
    if not authors_raw:
        return ""

    # Clean the authors string
    authors_raw = clean_bibtex_string(authors_raw)

    # Split by common separators
    if ',' in authors_raw:
        # If there are commas, split by them
        authors = [author.strip() for author in authors_raw.split(',')]
    else:
        # Otherwise, try to split by 'and'
        authors = [author.strip() for author in re.split(r'\s+and\s+', authors_raw, flags=re.IGNORECASE)]

    # Format each author
    formatted_authors = []
    for author in authors:
        if author:
            formatted_author = format_author_name(author)
            if formatted_author:
                formatted_authors.append(formatted_author)

    return " and ".join(formatted_authors)

def update_papers_bib(publications):
    """Update the papers.bib file with new publications"""

    print(f"📝 Updating {BIB_FILE_PATH}")

    # Create BibTeX header
    header = f"""---
---

@comment{{
  This file is automatically generated from Google Scholar.
  Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  Scholar ID: {SCHOLAR_ID}

  DO NOT EDIT MANUALLY - Changes will be overwritten on next update.
  To update: run python _scripts/update_publications.py
}}

"""

    # Generate BibTeX entries
    bibtex_entries = []
    for pub in publications:
        try:
            entry = publication_to_bibtex(pub)
            bibtex_entries.append(entry)
        except Exception as e:
            print(f"  ⚠️  Error converting publication to BibTeX: {e}")
            continue

    # Write to file
    with open(BIB_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(header)
        f.write("\n\n".join(bibtex_entries))

    print(f"✓ Updated {BIB_FILE_PATH} with {len(bibtex_entries)} publications")

def main():
    """Main function"""
    print("🚀 Starting automated publications update...")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Check if automatic updates are disabled (except in GitHub Actions)
    if os.getenv('DISABLE_AUTO_UPDATE', '').lower() == 'true' and not os.getenv('GITHUB_ACTIONS'):
        print("⚠️  Automatic updates are disabled.")
        print("   To enable updates, either:")
        print("   1. Run with: DISABLE_AUTO_UPDATE=false python update_publications.py")
        print("   2. Or unset the DISABLE_AUTO_UPDATE environment variable")
        print("   3. Updates are always enabled in GitHub Actions workflow")
        return

    # Create backup
    backup_existing_bib()

    # Fetch publications
    publications = get_scholar_publications()

    if not publications:
        print("❌ No publications found. Keeping existing file.")
        return

    # Update BibTeX file
    update_papers_bib(publications)

    print()
    print("✅ Publications update completed successfully!")
    print(f"📊 Total publications processed: {len(publications)}")
    print()
    print("Next steps:")
    print("1. Review the updated papers.bib file")
    print("2. Commit changes to your repository")
    print("3. The website will automatically rebuild with new publications")

if __name__ == "__main__":
    main()
