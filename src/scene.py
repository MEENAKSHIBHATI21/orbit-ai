import pyvista as pv

from earth import create_earth


class Scene:

    def __init__(self):

        self.plotter = pv.Plotter(
            window_size=(1200,900)
        )

        self.plotter.set_background("#02030a")

        self.plotter.remove_all_lights()

        sun = pv.Light(
            position=(50000,30000,20000),
            focal_point=(0,0,0),
            intensity=1.5
        )

        self.plotter.add_light(sun)

    def build(self):

        earth, atmosphere, texture = create_earth()

        self.plotter.add_mesh(
            atmosphere,
            color="#6bb6ff",
            opacity=0.05,
            smooth_shading=True
        )

        self.plotter.add_mesh(
            earth,
            texture=texture,
            smooth_shading=True
        )

        self.plotter.camera_position = [
            (18000,-22000,14000),
            (0,0,0),
            (0,0,1)
        ]

        self.plotter.enable_anti_aliasing()

    def run(self):

        self.plotter.show()