set -e
gunicorn server:app $1