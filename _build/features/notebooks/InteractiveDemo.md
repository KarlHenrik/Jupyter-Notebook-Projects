---
redirect_from:
  - "/features/notebooks/interactivedemo"
interact_link: content/C:\Users\KarlH\Dropbox\GitHubRepositories\Jupyter-Book-Showroom\content\features/notebooks/InteractiveDemo.ipynb
kernel_name: python3
has_widgets: false
title: 'Interactive Demo'
prev_page:
  url: /features/notebooks/Volleyball-Narrative
  title: 'Narrative-version'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from ipywidgets import interact, FloatSlider
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, HTML
plt.ion()

x = np.arange(500)
y = np.random.randn(500)

def update_plot_size(s, cmap):
    if cmap == "jet":
        display(HTML("<h2 style='color: red; margin: 0px auto;'>Nope</h2>"))
        return
    fig, ax = plt.subplots()
    ax.scatter(x, y, c=y, s=x*s, cmap=cmap)

interact(update_plot_size, s=FloatSlider(value=1, min=.1, max=2, step=.1), cmap=['viridis', 'magma', 'jet']);
```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_data_text}
```
interactive(children=(FloatSlider(value=1.0, description='s', max=2.0, min=0.1), Dropdown(description='cmap', …
```

</div>
</div>
</div>
