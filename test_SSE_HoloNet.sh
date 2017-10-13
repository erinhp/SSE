#extract features leveldb
rm -r examples/sse_holonet_features/ && ./build/tools/extract_features.bin models/SSE/SSE_HoloNet_trval_iter_69500.caffemodel script/SSE-HoloNet/SSE_holonet_test.prototxt prob examples/sse_holonet_features 215 leveldb GPU

#leveldb to mat
cd leveldb2mat/ && python leveldb2mat.py ../../examples/sse_holonet_features/ 215 27 7 features.mat