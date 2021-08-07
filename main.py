from luma.world.world_reader import WorldReader

if __name__ == "__main__":
    world = WorldReader.read('world.json')
    camera = list(filter(lambda e: e.name == "Main Camera", world.entities))[0]
    print(camera.camera_matrix)
    print("Done")