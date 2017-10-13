./build/tools/caffe train \
    --solver = script/SSE-DenseNet/SSE-densenet-121_train_solver.prototxt  \
    --weights = models/pretrained_model/DenseNet_121.caffemodel \
    --gpu = 0