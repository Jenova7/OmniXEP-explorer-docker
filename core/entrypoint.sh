#!/bin/bash
set -e

if [[ $(echo "$1" | cut -c1) = "-" ]]; then
  echo "$0: assuming arguments for omnixepd"

  set -- omnixepd "$@"
fi

if [[ $(echo "$1" | cut -c1) = "-" ]] || [[ "$1" = "omnixepd" ]]; then
  mkdir -p "$DATA_DIR"
  chmod 700 "$DATA_DIR"

  echo "$0: setting data directory to $DATA_DIR"

  set -- "$@" -datadir="$DATA_DIR"
fi

if [[ "$1" = "omnixepd" ]] || [[ "$1" = "omnixep-cli" ]] || [[ "$1" = "omnixep-tx" ]]; then
  echo
  exec "$@"
fi

echo
exec "$@"
