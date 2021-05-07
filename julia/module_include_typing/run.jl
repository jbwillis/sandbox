include("ModuleA.jl")
include("ModuleB.jl")
include("ModuleC.jl")

s1 = ModuleC.create_module_a_struct()
ModuleB.use_module_a_struct(s1)
