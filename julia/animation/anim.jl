using Plots
# pyplot()
gr()

t = -2*pi:.01:2*pi
phase = 0:.1:2*pi

plot(t, sin.(t), show=true, reuse=true)
# gui(fig)

for p in phase
	fig = plot(t, sin.(t .+ p), show=true, reuse=true)
	sleep(.1)
end
