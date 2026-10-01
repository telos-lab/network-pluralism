for notebook in notebooks/*/*.ipynb; do
    jupyter nbconvert \
        --to notebook \
        --execute "$notebook" \
        --inplace \
        --allow-errors
done