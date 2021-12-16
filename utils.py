import os
import json


def get_categories(ann_path):
    if ann_path == None:
        return None

    categories_temp = []
    categories = []
    categories_to_id = {}

    for i in range(len(os.listdir(ann_path))):
        with open(ann_path.rstrip("/") + "/" + str(i+1) + ".json") as file:
            data = json.load(file)

            for obj in data['regions']:
                category = obj['tags'][0]
                if category not in categories_temp:
                    categories_temp.append(category)

    for category in categories_temp:
        categories.append(
            {
                "supercategory": category,
                "id": categories_temp.index(category) + 1,
                "name": category
            }
        )

        categories_to_id[category] = categories_temp.index(category) + 1
    
    return categories, categories_to_id


def convert(ann_path, categories_to_id, output_dir, train_or_test):
    if ann_path == None:
        return None
    
    images = []
    annotations = []
    obj_id = 1

    for i in range(len(os.listdir(ann_path))):
        with open(ann_path + str(i+1) + ".json") as file:
            data = json.load(file)

            image_path = output_dir.rstrip("/") + "/" + train_or_test + "/" + data['asset']['name']
            image_id = i+1
            image_width = data['asset']['size']['width']
            image_height = data['asset']['size']['height']

            images.append(
                {
                    "height": image_height,
                    "width": image_width,
                    "id": image_id,
                    "file_name": image_path
                }
            )

            for obj in data['regions']:
                category = obj['tags'][0]
                bbox = obj['boundingBox']
                
                annotations.append(
                    {
                        "iscrowd": 0,
                        "image_id": image_id,
                        "bbox": [
                                float(bbox['left']),
                                float(bbox['top']),
                                float(bbox['width']),
                                float(bbox['height'])
                        ],
                        "category_id": categories_to_id[category],
                        "id": obj_id,
                        "area": image_height*image_width
                    }
                )

                obj_id += 1
    
    return images, annotations


def create_coco(file_name, images, annotations, categories):
    result_data = {}
    result_data['images'] = images
    result_data['annotations'] = annotations
    result_data['categories'] = categories

    with open(file_name, 'w') as outfile:
        json.dump(result_data, outfile, indent=4)
