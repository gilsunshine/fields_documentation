# "Documentation" for functions available to users of Fields
# If you're more familiar with python, see the file here for patterns for defining your own functions:
# https://github.com/gilsunshine/implicit-sandbox/blob/main/src/python/scalar_field_lib.py
# IMPORTANT! All based on the work of Inigo Quilez: https://iquilezles.org/


# --- SDF Primitives ---

sdf_sphere(center=(0.5, 0.5, 0.5), radius=0.3)
sdf_box(bounds=(0.5, 0.5, 0.5), center=(0.5, 0.5, 0.5))
sdf_rounded_box(bounds=(0.5, 0.5, 0.5), radius=0.1, center=(0.5, 0.5, 0.5))
sdf_box_frame(bounds=(0.5, 0.5, 0.5), edge_thickness=0.05, center=(0.5, 0.5, 0.5))
sdf_torus(t=(1.0, 0.25), center=(0.5, 0.5, 0.5))
sdf_capped_torus(sc=(0.5, 1.0), ra=1.0, rb=0.1, center=(0.5, 0.5, 0.5))
sdf_link(le=1.0, r1=0.5, r2=0.1, center=(0.5, 0.5, 0.5))
sdf_cone(c=(0.8, 0.6), h=1.0, center=(0.5, 0.5, 0.5))
sdf_plane(n=(0.0, 1.0, 0.0), h=0.0, center=(0.5, 0.5, 0.5))
sdf_hex_prism(h=(1.0, 1.0), center=(0.5, 0.5, 0.5))
sdf_tri_prism(h=(1.0, 1.0), center=(0.5, 0.5, 0.5))
sdf_capsule(a=(0.0, 0.0, 0.0), b=(1.0, 1.0, 1.0), r=0.2, center=(0.5, 0.5, 0.5))
sdf_capped_cylinder(a=(0.0, 0.0, 0.0), b=(0.0, 1.0, 0.0), r=0.5, center=(0.5, 0.5, 0.5))
sdf_rounded_cylinder(ra=0.5, rb=0.1, h=1.0, center=(0.5, 0.5, 0.5))
sdf_capped_cone(a=(0.0, 0.0, 0.0), b=(0.0, 1.0, 0.0), ra=0.5, rb=0.1, center=(0.5, 0.5, 0.5))
sdf_cut_sphere(r=1.0, h=0.5, center=(0.5, 0.5, 0.5))
sdf_cut_hollow_sphere(r=1.0, h=0.5, t=0.1, center=(0.5, 0.5, 0.5))
sdf_round_cone(a=(0.0, 0.0, 0.0), b=(0.0, 1.0, 0.0), r1=0.5, r2=0.1, center=(0.5, 0.5, 0.5))
sdf_ellipsoid(r=(1.0, 0.5, 1.0), center=(0.5, 0.5, 0.5))
sdf_pyramid(h=1.0, center=(0.5, 0.5, 0.5))
sdf_octahedron(s=1.0, center=(0.5, 0.5, 0.5))


# --- Patterns ---

wave_pattern(freq=8.0)
gyroid(freq=5.0)


# --- Compositing ---

union(a, b)
intersection(a, b)
difference(a, b)
xor(a, b)
smooth_union(a, b, k)
smooth_intersection(a, b, k)
smooth_difference(a, b, k)


# --- Transformations ---
# Usage: my_sdf.rotate_x(some_angle), etc.

translate(tx=0.0, ty=0.0, tz=0.0)
rotate_x(theta, origin=(0.0, 0.0, 0.0))
rotate_y(theta, origin=(0.0, 0.0, 0.0))
rotate_z(theta, origin=(0.0, 0.0, 0.0))
scale(sx=1.0, sy=1.0, sz=1.0, origin=(0.0, 0.0, 0.0))
    

# --- Utilities ---

blend(a, b, mask)
lerp(a, b, t)
normalize_to_sdf_range(f)
op_round(primitive, rad=0.1)
op_onion(primitive, thickness=0.1)
op_displace(primitive, displacement_fn)
op_twist(primitive, k=10.0, center=(0.5, 0.5, 0.5), axis=(0.0, 1.0, 0.0))
op_cheap_bend(primitive, k=10.0, center=(0.5, 0.5, 0.5), axis=(1.0, 0.0, 0.0), bend_axis=(0.0, 1.0, 0.0))
  