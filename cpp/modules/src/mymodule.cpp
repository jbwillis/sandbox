export module mymodule
    import std

    export void
    print_a_number(auto num)
{
    std::cout << "Your number is " << num << std::endl;
}