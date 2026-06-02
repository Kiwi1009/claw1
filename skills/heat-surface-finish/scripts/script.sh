#!/bin/zsh
# heat-surface-finish skill — reference dispatcher
HERE="${0:A:h}"
REFS="$HERE/../refs"

cmd="${1:-intro}"
case "$cmd" in
  intro|anneal|harden|case|hardness|plating|anodize|passivate|coatings|paint|defects|standards)
    cat "$REFS/$cmd.md"
    ;;
  all)
    for f in intro anneal harden case hardness plating anodize passivate coatings paint defects standards; do
      echo
      echo "═══════════════════════════════════════════════════════════════════════"
      echo "                         $f"
      echo "═══════════════════════════════════════════════════════════════════════"
      cat "$REFS/$f.md"
    done
    ;;
  *)
    echo "Usage: $0 {intro|anneal|harden|case|hardness|plating|anodize|passivate|coatings|paint|defects|standards|all}"
    exit 1
    ;;
esac
