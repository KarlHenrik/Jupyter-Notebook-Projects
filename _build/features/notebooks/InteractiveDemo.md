---
redirect_from:
  - "/features/notebooks/interactivedemo"
interact_link: content/features/notebooks/InteractiveDemo.ipynb
kernel_name: python3
has_widgets: true
title: 'Interactivity Demo'
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
import ipywidgets as widgets
from ipywidgets import HBox, VBox
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
%matplotlib inline
```
</div>

</div>

<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
@widgets.interact
def f(x=5):
    print(x**5)
```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_data_text}
```
interactive(children=(IntSlider(value=5, description='x', max=15, min=-5), Output()), _dom_classes=('widget-in…
```

</div>
</div>
</div>
