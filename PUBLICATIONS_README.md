# Automated Publications System

This system automatically updates the publications page with Prof. Farnaz Heidar-Zadeh's latest research from Google Scholar while maintaining the individual publication display format you prefer.

## How It Works

The system combines the best of both approaches:

- **Individual Publication Display**: Each publication is shown separately with full details (like the original BibTeX system)
- **Automatic Updates**: Publications are automatically fetched from Google Scholar and converted to BibTeX format
- **No Manual Maintenance**: The system updates itself whenever the website is rebuilt

## Files Created

### 1. `_scripts/update_publications.py`

- **Purpose**: Python script that fetches publications from Google Scholar
- **What it does**:
  - Connects to Prof. Heidar-Zadeh's Google Scholar profile (`JlIWcccAAAAJ`)
  - Downloads all publication data
  - Converts to BibTeX format compatible with jekyll-scholar
  - Updates `_bibliography/papers.bib`

### 2. `.github/workflows/update-publications.yml`

- **Purpose**: GitHub Actions workflow for automation
- **Triggers**:
  - Every time you push to the main branch
  - Weekly (Sundays at midnight) to catch new publications
  - Manually when needed
- **What it does**:
  - Runs the Python script
  - Commits any changes to papers.bib
  - Rebuilds and deploys the website

### 3. `update_publications.sh`

- **Purpose**: Manual update script for immediate use
- **Usage**: Run `./update_publications.sh` from the website root directory

## Usage Options

### Option 1: Automatic (Recommended)

1. **Push to GitHub**: The system automatically updates publications on every push
2. **Weekly Updates**: New publications are automatically detected weekly
3. **Zero Maintenance**: Just publish papers to Google Scholar as usual

### Option 2: Manual Updates

```bash
# From the website root directory
./update_publications.sh
```

### Option 3: Direct Python Script

```bash
# Install dependencies
pip install scholarly requests beautifulsoup4

# Run the update script
python _scripts/update_publications.py
```

## Configuration

The system is pre-configured with Prof. Heidar-Zadeh's details:

- **Google Scholar ID**: `JlIWcccAAAAJ`
- **Email**: `farnaz.heidarzadeh@queensu.ca`
- **Output File**: `_bibliography/papers.bib`

## Features

### ✅ What This System Provides

1. **Individual Publication Display**: Each paper shows separately with full details
2. **Automatic BibTeX Generation**: Converts Google Scholar data to proper BibTeX format
3. **Search Functionality**: Maintains the original publication search feature
4. **Citation Metrics**: Includes Google Scholar citation counts when available
5. **Backup System**: Automatically backs up existing papers.bib before updates
6. **Error Handling**: Gracefully handles network issues and missing data

### 📊 Publication Data Included

- Title, authors, journal/venue
- Publication year
- Abstract (when available)
- Google Scholar citation metrics
- Direct links to papers
- Proper BibTeX formatting for jekyll-scholar

## Troubleshooting

### If Publications Don't Update

1. Check that the Google Scholar ID is correct in the script
2. Verify internet connection
3. Google Scholar may have rate limiting - wait and try again

### If Website Build Fails

1. Check the GitHub Actions logs
2. Verify that all dependencies are properly installed
3. Ensure the papers.bib file is valid BibTeX format

### Manual Verification

```bash
# Test the website locally
bundle exec jekyll serve

# Check for BibTeX syntax errors
bundle exec jekyll build --verbose
```

## Benefits Over Manual System

| Manual BibTeX                   | Automated System                    |
| ------------------------------- | ----------------------------------- |
| ❌ Must manually add each paper | ✅ Automatically detects new papers |
| ❌ Risk of formatting errors    | ✅ Consistent formatting            |
| ❌ Time-consuming maintenance   | ✅ Zero maintenance required        |
| ❌ May miss new publications    | ✅ Weekly automatic checks          |
| ❌ Citation counts get outdated | ✅ Always current citation metrics  |

## Security & Privacy

- Uses only public Google Scholar data
- No API keys or authentication required
- All processing happens in your GitHub repository
- No external services store your data

## Support

If you encounter issues:

1. Check the GitHub Actions logs in your repository
2. Verify the Google Scholar profile is public and accessible
3. Ensure all required Python packages are installed
4. Contact the development team for assistance

---

**Last Updated**: January 2025  
**System Version**: 1.0  
**Compatible With**: Jekyll 4.x, al-folio theme
