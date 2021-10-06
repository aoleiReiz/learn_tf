import os
os.environ["TF_XLA_FLAGS"] = "--tf_xla_enable_xla_devices"

import tensorflow as tf

x = tf.config.list_physical_devices("GPU")