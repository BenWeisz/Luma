from luma.image.image import Image

class PPMWriter():
    @staticmethod
    def write(path: str, image: Image) -> None:
        with open(f"data/out/{path}", "wb") as out_file:
            file_header = f"P6\n{image.width}\n{image.height}\n255\n"
            
            header_data = [ord(c) for c in file_header]
            header_data = bytearray(header_data)
            out_file.write(header_data)

            image_data = []
            for y in range(image.height):
                for x in range(image.width):
                    pixel = image[image.height - 1 - y, x]
                    image_data.extend([
                        int(pixel[0]), 
                        int(pixel[1]), 
                        int(pixel[2])
                    ])
            
            image_data = bytearray(image_data)
            out_file.write(image_data)
