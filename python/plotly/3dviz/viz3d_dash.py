import plotly.graph_objects as go
import numpy as np

from dash import Dash, dcc, html, Input, Output, State, callback
import logging

logging.getLogger().setLevel(logging.DEBUG)

def hat(v):
    return np.array([
        [0.0, -v[2], v[1]],
        [v[2], 0.0, -v[0]],
        [-v[1], v[0], 0.0],
    ])

def main(): 
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

    app = Dash(__name__)

    app.layout = html.Div([
        dcc.Dropdown(
            ['X-Axis', 'Y-Axis', 'Z-Axis'],
            ['X-Axis'],
            multi=True,
            id='axes',
        ),
        dcc.Slider(-360, 360, 5,
                marks = {v: f"{v}" for v in range(-360, 361, 45)},
                value=0,
                id='theta',
                updatemode='drag',
                tooltip={"placement": "bottom", "always_visible": True}
        ),
        dcc.Graph(id='visualizer', figure=fig),
    ])

    @callback(
        Output('visualizer', 'figure'),
        Input('theta', 'value'),
        Input('axes', 'value'),
        State('visualizer', 'figure'))
    def update_viz(theta, axes, fig_state):
        logging.info(f"theta = {theta}")
        xyz = np.array([ 
                #  0     1     2     3     4     5     6     7     8     9
                [+0.0, +0.7, +0.7, -0.7, -0.7, +0.0, +0.7, +0.7, -0.7, -0.7],
                [+0.5, +0.0, -1.0, -1.0, +0.0, +0.5, +0.0, -1.0, -1.0, +0.0],
                [+1.0, +1.0, +1.0, +1.0, +1.0, -1.0, -1.0, -1.0, -1.0, -1.0],
        ])

        phi = np.array([1.0, 1.0, 1.0])
        if len(axes) > 0:
            if 'X-Axis' not in axes:
                phi[0] = 0.0
            if 'Y-Axis' not in axes:
                phi[1] = 0.0
            if 'Z-Axis' not in axes:
                phi[2] = 0.0
        phi = phi / np.linalg.norm(phi)
        phi_hat = hat(phi)
        theta = np.deg2rad(theta)
        R = np.eye(3) + np.sin(theta) * phi_hat + (1 - np.cos(theta)) * (phi_hat @ phi_hat)
        xyz = R @ xyz
        # breakpoint()
        fig = go.Figure(fig_state)
        fig.update_traces(
                x = xyz[0,:],
                y = xyz[1,:],
                z = xyz[2,:],
                selector=dict(name="Vehicle"),
        )
        fig.update_layout(
            scene = dict(
                xaxis = dict(nticks=5, range=[-2,2],),
                yaxis = dict(nticks=5, range=[-2,2],),
                zaxis = dict(nticks=5, range=[-2,2],),
            ),
            width=700,
            margin=dict(r=10, l=10, b=10, t=10),
        )
        return fig

    app.run(debug=True)

if __name__ == "__main__":
    main()