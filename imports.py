import bs4
import io
import matplotlib.pyplot as plt
import pandas as pd
import pulp
import numpy as np
import os
import re
import requests

from tqdm import tqdm_notebook


if __name__ == '__main__':
    # Render all variables on a single line with display.
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = 'all'
    # Interactive plots.
    from IPython import get_ipython
    get_ipython().run_line_magic('matplotlib', 'notebook')
    # Retina quality plots (only for `%matplotlib inline`).
    get_ipython().run_line_magic(
        'config', "InlineBackend.figure_format = 'retina'")
    # Better default figure size.
    plt.rcParams['figure.figsize'] = 9.5, 9.5 / (16 / 9)
    # Better default figure margins.
    plt.rcParams['figure.autolayout'] = True
    # Better default font families (falls back to defaults if missing).
    # Run `matplotlib.font_manager._rebuild()` to rebuild the font cache.
    plt.rcParams['font.sans-serif'].insert(0, 'Roboto')
    plt.rcParams['font.monospace'].insert(0, 'Roboto Mono')
    # Auto-reload modified packages.
    get_ipython().run_line_magic('load_ext', 'autoreload')
    get_ipython().run_line_magic('autoreload', '2')
    # change default number of colums to display
    pd.options.display.max_columns = 200