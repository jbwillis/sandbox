module ModuleC
# include("ModuleA.jl")
using ..ModuleA # use ModuleA definition from parent scope
function create_module_a_struct()
	s = ModuleA.ModuleAStruct("Apples", "Bananas")
end
end
