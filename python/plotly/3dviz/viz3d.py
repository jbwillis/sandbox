# %%
import plotly.graph_objects as go
import numpy as np

# %%

fig = go.Figure(data=[
    go.Mesh3d(
        # 8 vertices of a cube
        x=[0, 0, 1, 1, 0, 0, 1, 1],
        y=[0, 1, 1, 0, 0, 1, 1, 0],
        z=[0, 0, 0, 0, 1, 1, 1, 1],
        colorbar=dict(title=dict(text='z')),
        colorscale=[[0, 'gold'],
                    [0.5, 'mediumturquoise'],
                    [1, 'magenta']],
        # Intensity of each vertex, which will be interpolated and color-coded
        intensity = np.linspace(0, 1, 8, endpoint=True),
        # i, j and k give the vertices of triangles
        i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
        j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
        name='y',
        showscale=True
    )
])

fig.show()

# %%
fig = go.Figure(data=[
    go.Mesh3d(
        # 8 vertices of a cube
        x=[0, 0, 1, 1, 0, 0, 1, 1],
        y=[0, 1, 1, 0, 0, 1, 1, 0],
        z=[0, 0, 0, 0, 1, 1, 1, 1],
        colorbar=dict(title=dict(text='z')),
        colorscale=[[0, 'gold'],
                    [0.5, 'mediumturquoise'],
                    [1, 'magenta']],
        # Intensity of each vertex, which will be interpolated and color-coded
        intensity = np.linspace(0, 1, 12, endpoint=True),
        intensitymode='cell',
        # i, j and k give the vertices of triangles
        i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
        j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
        name='y',
        showscale=True
    )
])

fig.show()

# %%
def hat(v):
    return np.array([
        [0.0, -v[2], v[1]],
        [v[2], 0.0, -v[0]],
        [-v[1], v[0], 0.0],
    ])

# %%
xyz = np.array([ 
        #  0     1     2     3     4     5     6     7     8     9
        [+0.0, +0.7, +0.7, -0.7, -0.7, +0.0, +0.7, +0.7, -0.7, -0.7],
        [+0.5, +0.0, -1.0, -1.0, +0.0, +0.5, +0.0, -1.0, -1.0, +0.0],
        [+1.0, +1.0, +1.0, +1.0, +1.0, -1.0, -1.0, -1.0, -1.0, -1.0],
])
fig = go.Figure(data=[
    go.Mesh3d(
        x = xyz[0,:],
        y = xyz[1,:],
        z = xyz[2,:],
        #  a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p
        i=[0, 1, 1, 0, 4, 3, 3, 5, 6, 7, 0, 0, 1, 1, 2, 2],
        j=[1, 3, 2, 4, 5, 4, 8, 6, 7, 8, 5, 1, 6, 2, 7, 3],
        k=[4, 4, 3, 5, 9, 9, 9, 9, 9, 9, 6, 6, 7, 7, 8, 8],
        facecolor=[
            "grey", # a
            "grey", # b
            "grey", # c
            "magenta", # d
            "magenta", # e
            "black", # f
            "black", # g
            "black", # h
            "black", # i
            "black", # j
            "magenta", # k
            "magenta", # l
            "black", # m
            "black", # n
            "grey", # o
            "grey", # p
        ],
        # Intensity of each vertex, which will be interpolated and color-coded
        # intensity = np.linspace(0, 1, 16, endpoint=True),
        # intensitymode='cell',
        showscale=False,
        opacity=1.0,
        flatshading=True,
        name="Vehicle",
    ),
    go.Scatter3d(
        x=[0.0, 1.0],
        y=[0.0, 1.0],
        z=[0.0, 1.0],
        line=dict(
            color="yellow",
            width=5,
        ),
        name="Sun Vector"
    )
])

fig.update_layout(
    scene = dict(
        xaxis = dict(nticks=5, range=[-2,2],),
        yaxis = dict(nticks=5, range=[-2,2],),
        zaxis = dict(nticks=5, range=[-2,2],),
    ),
    width=700,
    margin=dict(r=10, l=10, b=10, t=10),
)


fig.show()
# %%
theta = 0.1
phi = np.array([1.0, 0, 0])
phi_hat = hat(phi)
R = np.eye(3) + np.sin(theta) * phi_hat + (1 - np.cos(theta)) * (phi_hat @ phi_hat)
xyz = R @ xyz
fig.update_traces(
        x = xyz[0,:],
        y = xyz[1,:],
        z = xyz[2,:],
        selector=dict(name="Vehicle"),
)
fig.show()

# %%
