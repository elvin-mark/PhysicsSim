import numpy as np

ndim = 3 # Our world with 3 dimensions

# Simple Physical Object with mass and charge
class MyObject:
    def __init__(self,m=1,q=0,r0=np.array([0.,0.,0.]),v0=np.array([0.,0.,0.])):
        self.m = m   # Mass
        self.q = q   # Charge
        self.r = r0  # Position
        self.v = v0  # Speed

        self.history = [self.r.copy()]

    def update(self,dt=0.1,F=np.array([0.,0.,0.])):
        self.r += self.v * dt
        self.v += (F/self.m) * dt
        self.history.append(self.r.copy())

# Simple World where our objects can move
class MyWorld:
    def __init__(self,dt=0.1):
        self.objects = []
        self.dt = 0.1
        self.t = 0.
        self.history = [self.t]

    def init_random(self,N=2):
        for i in range(N):
            mass = np.random.rand()
            r0 = np.random.rand(ndim,)
            v0 = np.random.rand(ndim,)
            self.objects.append(MyObject(m=mass,r0=r0,v0=v0))

    def add_object(self,o):
        self.objects.append(o)

    def add_force_field(self,fn):
        self.force_field_fn = fn

    def update(self):
        self.t += self.dt
        self.history.append(self.t)
        for o in self.objects:
            F = self.force_field_fn(o)
            o.update(dt=self.dt,F=F)

    def run(self,num_steps=100):
        for i in range(num_steps):
            self.update()