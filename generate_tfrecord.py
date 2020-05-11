"""
Usage:
  # From tensorflow/models/
  # Create train data:
  python generate_tfrecord.py --csv_input=data/train_labels.csv  --output_path=train.record

  # Create test data:
  python generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=test.record
"""
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import pandas as pd
import tensorflow as tf

from PIL import Image
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict

flags = tf.app.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
flags.DEFINE_string('image_dir', '', 'Path to images')
FLAGS = flags.FLAGS


# TO-DO replace this with label map
def class_text_to_int(row_label):
    #if row_label == 'raccoon':
     #   return 1
    #else:
     #   None
     switch (row_label) {
        if row_label == "amulet"
            return 1
        else if row_label == "crossbow"
            return 10
        else if row_label == "dragonshield"
            return 11
        else if row_label == "egg"
            return 12
        else if row_label == "lavacape"
            return 13
        else if row_label == "infernocape"
            return 14
        else if row_label == "fish1"
            return 15
        else if row_label == "wizardhat"
            return 16
        else if row_label == "kiteshield"
            return 17
        else if row_label == "genielamp"
            return 18
        else if row_label == "logs"
            return 19
        else if row_label == "axe"
            return 2
        else if row_label == "mask"
            return 20
        else if row_label == "necklace"
            return 21
        else if row_label == "partyhat"
            return 22
        else if row_label == "platearmour"
            return 23
        else if row_label == "ironplatearmour"
            return 24
        else if row_label == "egg2"
            return 25
        else if row_label == "vial"
            return 26
        else if row_label == "angrypumpkin"
            return 27
        else if row_label == "scroll2"
            return 28
        else if row_label == "scroll3"
            return 29
        else if row_label == "beret"
            return 3
        else if row_label == "fishingcape"
            return 30
        else if row_label == "skull"
            return 31
        else if row_label == "birdbook"
            return 32
        else if row_label == "prayerbook"
            return 4
        else if row_label == "mysterybox"
            return 5
        else if row_label == "bracelet"
            return 6
        else if row_label == "cannon"
            return 7
        else if row_label == "chest"
            return 8
        else if row_label == "scroll"
            return 9
#..... up to 32
        else
            return None

         
        case 1:  item = "January";
             break;
        case 2:  item = "February";
             break;
        case 3:  item = "March";
             break;
        case 4:  item = "April";
             break;
        case 5:  item = "May";
             break;
        case 6:  item = "June";
             break;
        case 7:  item = "July";
             break;
        case 8:  item = "August";
             break;
        case 9:  item = "September";
             break;
        case 10: item = "October";
             break;
        case 11: item = "November";
             break;
        case 12: item = "December";
             break;
        case 13:  item = "January";
             break;
        case 14:  item = "February";
             break;
        case 15:  item = "March";
             break;
        case 16:  item = "April";
             break;
        case 17:  item = "May";
             break;
        case 18:  item = "June";
             break;
        case 19:  item = "July";
             break;
        case 20:  item = "August";
             break;
        case 21:  item = "September";
             break;
        case 22: item = "October";
             break;
        case 23: item = "November";
             break;
        case 24: item = "December";
             break;
        case 25:  item = "January";
             break;
        case 26:  item = "February";
             break;
        case 27:  item = "March";
             break;
        case 28:  item = "April";
             break;
        case 29:  item = "May";
             break;
        case 30:  item = "June";
             break;
        case 31:  item = "July";
             break;
        case 32:  item = "August";
             break;
        default: item = None;
             break;
        }


def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


def main(_):
    writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
    path = os.path.join(FLAGS.image_dir)
    examples = pd.read_csv(FLAGS.csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())

    writer.close()
    output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    tf.app.run()
