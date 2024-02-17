from mpi4py import MPI
from dolfinx import mesh
from dolfinx import fem

domain = mesh.create_unit_square(MPI.COMM_WORLD, 8, 8, mesh.CellType.quadrilateral)

V_space = fem.FunctionSpace(domain, ("CG", 1))

# rho = fem.Function(V_space)
# rho.interpolate(lambda x: (x[1]-0.5)**3 - (x[1]-0.5)**2)
# # Define source function
# x = ufl.SpatialCoordinate(mesh)
# f = 10*ufl.exp(-((x[0] - 0.5)**2 + (x[1] - 0.5)**2) / 0.02)

V_bc_upper = 1
V_bc_lower = 0
