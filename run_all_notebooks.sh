for notebook in notebooks/*/*.ipynb; do
    uv run jupyter nbconvert \
        --to notebook \
        --execute "$notebook" \
        --inplace
done