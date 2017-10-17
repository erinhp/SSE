#extract features leveldb
rm -r examples/sse_resnet_features/ && ./build/tools/extract_features.bin models/SSE/SSE_ResNet_50_trval_iter_83000.caffemodel script/SSE-ResNet/SSE-resnet-50_test.prototxt prob examples/sse_resnet_features 201 leveldb GPU

#leveldb to mat
cd leveldb2mat/ && python leveldb2mat.py ../examples/sse_resnet_features/ 201 29 7 features.mat