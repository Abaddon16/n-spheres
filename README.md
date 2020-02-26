# n-spheres

A Python tool for displaying properties about higher dimension spheres. Sparked by a curiosity of the volume of higher dimensional spheres versus higher dimensional cubes.

## Files

### multiDimensionalSpheres.py

This is the main dish. Defines an `n_sphere` object that holds onto a couple pieces of relevant information.

Computes the top and bottom of the equations in their most reduced form, and saves that to the object. Uses multiple ways to keep the values as small as possible while still doing the requisite multiplication and exponentiation.

To use, import as usual (`import multiDimensionalSpheres as mds`). From there, you can create an `n_sphere` directly (not recommended). Alternatively, you can create an `n_sphere` via the `create_sphere(dimension, radius)` function. This will return the `n_sphere` object with everything properly initialized.

Additionally, you can call the `sphere_list(limit, radius)` function to return a list of `limit` spheres.

### Profiler.py

Just a simple profiler I used to find bottlenecks in the code. I used this to make sure any function calls that were backing up the process were critical, or not my functions.
