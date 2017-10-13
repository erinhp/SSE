./build/tools/caffe train \
    --solver = script/SSE-ResNet/SSE-resnet-50_train_solver.prototxt  \
    --weights = models/pretrained_model/ResNet-50-model.caffemodel \
    --gpu = 0