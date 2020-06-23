# project-template
A template for Jupyter Notebook based research projects. I try to describe the project goals, organization, and data here.

## Notebooks: the project narrative
- `*.ipynb` | The core of your project narrative and analyses. TODO create template notebook `Template.ipynb`.

- `presentation.mplstyle` | My custom `matplotlib` stylesheet for default plot properties How to use in notebooks:
    ```
    import matplotlib.pyplot as plt
    >>> plt.style.use('presentation.mplstyle')
    ```

- `environment.yml` | The project virtual environment generated with `conda env export --no-builds > environment.yml`. I strongly recommend documenting the packages you use for analyses for the sake of reproducibility. [conda](https://www.anaconda.com/products/individual) is a cross-platform package manager that allows you to do so easily.

## Stay organized with a couple folders
- `data` | Store data here. Provide instructions to access data if it's too big, sensitive, etc. and is stored somewhere else.

- `plots` | Save generated figures here; this way, figures can be viewed without rendering notebooks.

- `scripts` | I usually store bash scripts and utility functions/classes here.

## References

Inspiration taken from googling many blog posts (and dealing with clutter over the years).

https://github.com/outlierbio/ob-project-template
