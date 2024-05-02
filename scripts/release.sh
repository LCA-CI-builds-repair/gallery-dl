# Ensure ROOTDIR is correctly assigned without trailing slash
ROOTDIR="$(realpath "$(dirname "$0")/..")"

# Correct the command to get the Python version based on module import
PYVERSION="$(python -c "import gallery_dl; print(gallery_dl.__version__)")"


prompt
supportedsites
cleanup
update
changelog
build-python
build-linux
build-windows
sign
upload-pypi
upload-git
update-dev
