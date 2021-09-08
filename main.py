from luma.world.world_reader import WorldReader
from luma.image.ppm_writer import PPMWriter

if __name__ == "__main__":
    world = WorldReader.read('world.json')
    camera = list(filter(lambda e: e.name == "Main Camera", world.entities))[0]

    frame = camera.render_frame(world)
    PPMWriter.write("test.ppm", frame)

    print("Done")