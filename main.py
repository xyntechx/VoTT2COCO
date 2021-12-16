import argparse
import utils


parser = argparse.ArgumentParser()

parser.add_argument("--train-ann", help="Path to train annotations", default=None)
parser.add_argument("--test-ann", help="Path to test annotations", default=None)
parser.add_argument("--output-dir", help="Path to output directory", default=None)

args = parser.parse_args()

# For train dataset
categories, categories_to_id = utils.get_categories(args.train_ann)
images, annotations = utils.convert(args.train_ann, categories_to_id, args.output_dir, "train")
utils.create_coco("train.json", images, annotations, categories)

# For test dataset
categories, categories_to_id = utils.get_categories(args.test_ann)
images, annotations = utils.convert(args.test_ann, categories_to_id, args.output_dir, "test")
utils.create_coco("test.json", images, annotations, categories)
