from tensorflow.python.lib.io.file_io import FileIO
with FileIO('model.h5', 'rb') as f:
    print(f.read())
