#include <fmt/core.h>
#include <glog/logging.h>
#include <ceres/ceres.h>

struct CostFunctor
{
    template <typename T>
    bool operator()(const T *const x, T *residual) const
    {
        residual[0] = 10.0 - x[0];
        return true;
    }
};

int main(int argc, char **argv)
{
    google::InitGoogleLogging(argv[0]);

    const double initial_x = 5.0;
    while (1 == 1)
    {
        double x = initial_x;

        ceres::Problem problem;

        ceres::CostFunction *cost_function = new ceres::AutoDiffCostFunction<CostFunctor, 1, 1>(new CostFunctor);

        problem.AddResidualBlock(cost_function, nullptr, &x);

        ceres::Solver::Options options;
        options.minimizer_progress_to_stdout = true;
        ceres::Solver::Summary summary;
        ceres::Solve(options, &problem, &summary);

        fmt::print("{}\n", summary.BriefReport());
        fmt::print("x : {} -> {}\n", initial_x, x);
    }

    return 0;
}