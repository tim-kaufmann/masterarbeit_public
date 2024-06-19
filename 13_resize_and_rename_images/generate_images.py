import os
from PIL import Image
import random

def create_test_images(base_dir, image_specs):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    for spec in image_specs:
        input_dir = os.path.join(base_dir, spec['input'])
        if not os.path.exists(input_dir):
            os.makedirs(input_dir)
        
        for i in range(spec['count']):
            img = Image.new('RGB', (random.randint(500, 1000), random.randint(500, 1000)), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            img.save(os.path.join(input_dir, f"{str(i + 1).zfill(3)}.jpg"))

# Spezifikationen der Testfälle
image_specs = [
    {'input': 'test2/input', 'count': 2},
    {'input': 'test3/input', 'count': 1},
    {'input': 'test4/input', 'count': 8},
    {'input': 'test5/input', 'count': 2},
    {'input': 'test6/input', 'count': 3},
    {'input': 'test7/input', 'count': 0},  # Dieser Test scheint keine Bilder zu benötigen
]

base_dir = 'test_images'
create_test_images(base_dir, image_specs)
