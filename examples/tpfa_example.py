import numpy

from Padmec.Kernel import TPFA
from Padmec.Mesh.MeshFactory import MeshFactory
from Padmec.Physical.PhysicalMap import PhysicalMap
from Padmec.Physical import Physical


physical = PhysicalMap()
physical[101] = Physical.Dirichlet(1.0)
physical[102] = Physical.Dirichlet(-1.0)
physical[103] = Physical.Symmetric()
physical[50] = Physical.Permeability(numpy.eye(3))

meshfile = 'tests/cube_small.h5m'
mf = MeshFactory()
m = mf.load_mesh(meshfile, physical)

tpfa = TPFA
