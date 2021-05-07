module ModuleB
# include("ModuleA.jl") # this brings ModuleA into the current scope (Main.ModuleB.ModuleA)
using ..ModuleA # use ModuleA definition from parent scope
function use_module_a_struct(s::ModuleA.ModuleAStruct)
	println("thing1 = ", s.thing1)
	println("thing2 = ", s.thing2)
end
end
