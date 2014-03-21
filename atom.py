class Atom:
    """Defines an atom type."""
    def __init__(self, name, mass, x=[0., 0., 0.], 
                 v=[0., 0., 0.], f=[0., 0., 0.]):
        self.name = name
        self.mass = mass
        self.x = x
        self.v = v
        self.f = f

