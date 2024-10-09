#install pycirclize
import matplotlib.pyplot as plt
from pycirclize import Circos
import pandas as pd

# Create matrix dataframe (3 x 6)
row_names = ["B. rapa", "B. nigra", "B. oleracea" ]
col_names = ["B. carinata","B. napus","B. juncea"]
matrix_data = [
    [0,  10,10],
    [8,  0,8],
    [9,  9,0],
]

matrix_df = pd.DataFrame(matrix_data, index=row_names, columns=col_names)


species_colors = {
    "B. nigra": "#FFFF00",
    "B. juncea": "#ffa600",
    "B. rapa": "#FF0000",
    "B. napus": "#c098ed",
    "B. oleracea": "#2e65e6",
    "B. carinata": "#bee683"
}

# Initialize from matrix (Can also directly load tsv matrix file)
circos = Circos.initialize_from_matrix(
    matrix_df,
    start=-265,
    end=95,
    space=3,
    cmap=species_colors,
    ticks_interval=1,
    r_lim=(93, 100),
    label_kws=dict(r=94, size=12, color="black",fontstyle= 'italic'),
    link_kws=dict(direction=1, ec="black", lw=0.5, alpha=0.5),
)

print(matrix_df)
fig = circos.plotfig()

plt.show()




#install pycirclize
import matplotlib.pyplot as plt
from pycirclize import Circos
import pandas as pd

# Create matrix dataframe (3 x 6)
row_names = ["B. rapa", "B. napus", "B. oleracea","B. carinata","B. nigra","B. juncea" ]
col_names = ["B. rapa", "B. napus", "B. oleracea","B. carinata","B. nigra","B. juncea"]
matrix_data = [
    [0, 10,0,0,0,10],
    [0, 0,0,0,0,0],
    [0, 9,0,9,0,0],
    [0, 0,0,0,0,0],
    [0, 0,0,8,0,8],
    [0, 0,0,0,0,0],
]

matrix_df = pd.DataFrame(matrix_data, index=row_names, columns=col_names)


species_colors = {
    "B. nigra": "#FFFF00",
    "B. juncea": "#ffa600",
    "B. rapa": "#FF0000",
    "B. napus": "#c098ed",
    "B. oleracea": "#2e65e6",
    "B. carinata": "#bee683"
}

# Initialize from matrix (Can also directly load tsv matrix file)
circos = Circos.initialize_from_matrix(
    matrix_df,
    start=-265,
    end=95,
    space=3,
    cmap=species_colors,
    ticks_interval=1,
    r_lim=(93, 100),
    label_kws=dict(r=94, size=12, color="black",fontstyle= 'italic'),
    link_kws=dict(direction=1, ec="black", lw=0.5, alpha=0.5),
)

print(matrix_df)
fig = circos.plotfig()

plt.show()



