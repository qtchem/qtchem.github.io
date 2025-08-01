#!/bin/bash
# Setup script for local development
# This script configures the environment to disable automatic publication updates

echo "🔧 Setting up local development environment..."
echo ""

# Export the environment variable for the current session
export DISABLE_AUTO_UPDATE=true

# Add to shell profile for persistence
SHELL_PROFILE=""
if [ -f "$HOME/.zshrc" ]; then
    SHELL_PROFILE="$HOME/.zshrc"
elif [ -f "$HOME/.bash_profile" ]; then
    SHELL_PROFILE="$HOME/.bash_profile"
elif [ -f "$HOME/.bashrc" ]; then
    SHELL_PROFILE="$HOME/.bashrc"
fi

if [ -n "$SHELL_PROFILE" ]; then
    # Check if already exists
    if ! grep -q "DISABLE_AUTO_UPDATE=true" "$SHELL_PROFILE"; then
        echo "" >> "$SHELL_PROFILE"
        echo "# Disable automatic publication updates for local Jekyll development" >> "$SHELL_PROFILE"
        echo "export DISABLE_AUTO_UPDATE=true" >> "$SHELL_PROFILE"
        echo "✅ Added DISABLE_AUTO_UPDATE=true to $SHELL_PROFILE"
    else
        echo "✅ DISABLE_AUTO_UPDATE already configured in $SHELL_PROFILE"
    fi
else
    echo "⚠️  Could not detect shell profile. Please manually add:"
    echo "   export DISABLE_AUTO_UPDATE=true"
    echo "   to your shell configuration file."
fi

echo ""
echo "🚀 Local development setup complete!"
echo ""
echo "Now you can run Jekyll locally without automatic publication updates:"
echo "   bundle exec jekyll serve --livereload --port 4001"
echo ""
echo "To manually update publications when needed:"
echo "   DISABLE_AUTO_UPDATE=false python _scripts/update_publications.py"
echo ""
echo "Publications will still update automatically in GitHub Actions."
