#include <bits/stdc++.h>

using namespace std;

struct point2d
{
    double x;
    double y;
};
double cross(point2d a, point2d b) {
    return a.x * b.y - a.y * b.x;
}
int signed_area_parallelogram(point2d p1, point2d p2, point2d p3) {
    return cross(p2 - p1, p3 - p2);
}

double triangle_area(point2d p1, point2d p2, point2d p3) {
    return abs(signed_area_parallelogram(p1, p2, p3)) / 2.0;
}

bool clockwise(point2d p1, point2d p2, point2d p3) {
    return signed_area_parallelogram(p1, p2, p3) < 0;
}

bool counter_clockwise(point2d p1, point2d p2, point2d p3) {
    return signed_area_parallelogram(p1, p2, p3) > 0;
}

int main()
{
    struct point2d p1,p2,p3;
    
    
    return 0;
}