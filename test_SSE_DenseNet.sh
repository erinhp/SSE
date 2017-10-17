#extract features leveldb
rm -r examples/sse_densenet_features/ && ./build/tools/extract_features.bin models/SSE/SSE_DenseNet_121_trval_iter_69500.caffemodel script/SSE-DenseNet/SSE-densenet-121_test.prototxt prob examples/sse_densenet_features 215 leveldb GPU

#leveldb to mat
cd leveldb2mat/ && python leveldb2mat.py ../examples/sse_densenet_features/ 215 27 7 features.mat