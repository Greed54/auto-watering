#!/usr/bin/env bash
set -euo pipefail

# ——— Configuration ———
REMOTE_USER="dmitry.usatenko"
REMOTE_HOST="auto-watering-rasp"
REMOTE_PATH="/home/dmitry.usatenko/auto-watering"
REPO_URL="git@github.com:Greed54/auto-watering.git"
BRANCH="${1:-main}"

# Deploy via SSH with agent‑forwarding
ssh -A "${REMOTE_USER}@${REMOTE_HOST}" bash <<EOF
  set -euo pipefail

  # Prepare project directory
  mkdir -p "${REMOTE_PATH}"
  cd       "${REMOTE_PATH}"

  # Trust GitHub host key (avoid host verification prompts)
  mkdir -p ~/.ssh
  touch    ~/.ssh/known_hosts
  ssh-keyscan github.com >> ~/.ssh/known_hosts 2>/dev/null

  # Clone or update the repository
  if [ ! -d .git ]; then
    git clone -b "${BRANCH}" "${REPO_URL}" .
  else
    git fetch origin "${BRANCH}"
    git reset --hard "origin/${BRANCH}"
  fi

  # Create and activate virtual environment
  python3 -m venv venv
  source venv/bin/activate

  # Install Python dependencies
  pip install --upgrade pip
  pip install -r requirements.txt
EOF

echo "✅ Deployment complete!"
echo
echo "Next steps on the Pi:"
echo "  ssh ${REMOTE_USER}@${REMOTE_HOST}"
echo "  cd ${REMOTE_PATH}"
echo "  source venv/bin/activate"
echo "  python3 src/main.py  # fullscreen, frameless"
