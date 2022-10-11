using Pkg;
Pkg.activate(joinpath(@__DIR__, ".."));
using PGFPlotsX
const def_linewidth = "very thick"
const color_eDMD = "orange"
const color_jDMD = "cyan"
const color_nominal = "black"
# lineopts = @pgf {no_marks, "very thick", "error bars/y dir=both", "error bars/y explicit"}
lineopts = @pgf {no_marks, "very thick"}

x = -5:0.01:5

y1 = sinc.(x)
y2 = sinc.(2 * x)
y3 = sinc.(4 * x)

p_demo_1 = @pgf Axis(
    {
        xmajorgrids,
        ymajorgrids,
        xlabel = "Equilibirum offset",
        ylabel = "Tracking error",
        legend_pos = "north west",
        ymax = 3,},
    PlotInc({lineopts..., color = "black"}, Coordinates(x, y1)),
    PlotInc({lineopts..., color = color_eDMD}, Coordinates(x, y2)),
    PlotInc({lineopts..., color = color_jDMD}, Coordinates(x, y3)), Legend(["nominal MPC", "eDMD", "jDMD"])
)
# pgfsave(joinpath(BilinearControl.FIGDIR, "rex_full_quadrotor_mpc_error_by_equilibrium_change.tikz"), p_equilibrium_err, include_preamble=false)