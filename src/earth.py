from pathlib import Path
import pyvista as pv


BASE_DIR = Path(__file__).resolve().parent.parent

TEXTURE = (
    BASE_DIR
    / "assets"
    / "textures"
    / "earth_texture.jpg"
)


def create_earth():

    earth = pv.Sphere(
        radius=6371,
        theta_resolution=500,
        phi_resolution=500
    )

    earth.texture_map_to_sphere(inplace=True)

    texture = pv.read_texture(str(TEXTURE))

    atmosphere = pv.Sphere(
        radius=6500,
        theta_resolution=500,
        phi_resolution=500
    )

    return earth, atmosphere, texture