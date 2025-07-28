#!/bin/bash
# Publications Update Script for Heidar-Zadeh Group Website
# 
# This script respects the DISABLE_AUTO_UPDATE environment variable
# and only runs automatically in GitHub Actions.

echo "🚀 Heidar-Zadeh Group Publications Updater"
echo "==========================================="
echo ""

# Check if automatic updates are disabled (except in GitHub Actions)
if [ "$DISABLE_AUTO_UPDATE" = "true" ] && [ -z "$GITHUB_ACTIONS" ]; then
    echo "⚠️  Automatic publications updates are disabled."
    echo "   To enable updates, either:"
    echo "   1. Run with: DISABLE_AUTO_UPDATE=false ./update_publications.sh"
    echo "   2. Or unset the DISABLE_AUTO_UPDATE environment variable"
    echo "   3. Updates are always enabled in GitHub Actions workflow"
    echo ""
    echo "   To force update now: DISABLE_AUTO_UPDATE=false ./update_publications.sh"
    exit 0
fi

# Check if Python script exists
if [ ! -f "_scripts/update_publications.py" ]; then
    echo "❌ Error: _scripts/update_publications.py not found"
    echo "Please ensure you're running this from the website root directory"
    exit 1
fi

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed"
    exit 1
fi

echo "📦 Installing required Python packages..."
pip3 install requests beautifulsoup4 --quiet

echo ""
echo "🔄 Updating publications from Google Scholar..."
python3 _scripts/update_publications.py

echo ""
echo "✅ Publications update completed!"
echo ""
echo "Next steps:"
echo "1. Review the updated _bibliography/papers.bib file"
echo "2. Test the website locally: bundle exec jekyll serve"
echo "3. Commit and push changes to deploy"
echo ""
echo "To automate this process, set up the GitHub Actions workflow"
echo "in .github/workflows/update-publications.yml"
