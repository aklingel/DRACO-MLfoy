import pandas as pd
from keras.utils import to_categorical

class DataFrame( object ):
    def __init__(self, path_to_input_file, output_label = "class_label"):
        print("-"*40)
        print("loading data from "+str(path_to_input_file))
        with pd.HDFStore( path_to_input_file, mode = "r") as store:
            df          = store.select("data")
            label_dict  = store.select("label_dict")
            image_size  = store.select("image_size")

        self.input_shape        = image_size.values[0]
        print("extracted input shape "+str(self.input_shape))
        self.input_size         = self.input_shape[0]*self.input_shape[1]*self.input_shape[2]
        print("size of input image: "+str(self.input_size))
        self.n_events           = df.shape[0]
        print("extracted number of events: "+str(self.n_events))

        # output labels
        print("chose '"+str(output_label)+"' as label for output classes")
        self.Y = df[output_label].values

        # generating label vectors (one-hot-encoding)
        self.one_hot = to_categorical( self.Y )

        # loading label dictionary:
        label_dict = label_dict.to_dict('list')
        for key in label_dict:
            label_dict[key] = label_dict[key][0]
        self.inverted_label_dict = {val: key for key, val in label_dict.items()}
        self.label_dict = label_dict
        self.num_classes = len(label_dict)

        # input data
        self.X  = df.values[:,:self.input_size]
        # reshape as CNN inputs
        self.X = self.X.reshape(-1, *self.input_shape)
        print("data shape: {}, {}".format( self.X.shape, self.one_hot.shape ))
        print("-"*40)



