if ! command -v "poetry"; then
    pip3 install --upgrade --user poetry
fi

bash -c "poetry install"
