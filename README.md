# SSE: Learning Supervised Scoring Ensemble for Emotion Recognition in the Wild
SSE is a state-of-the-art algorithm for face emotion recognition. You can use the code to train/evaluate a network for emotion recognition task. For more details, please refer to our ICMI 2017 paper.
## Citing SSE
If you find SSE useful in your research, please consider citing:
``` 
@inproceedings{HupICMI2017,
    Author = {Ping Hu, Dongqi Cai, Shandong Wang, Anbang Yao, Yurong Chen},
    Title = {Learning Supervised Scoring Ensemble for Emotion Recognition in the Wild},
    Booktitle = {19th ACM International Conference on Multimodal Interaction},
    Year = {2017} 
}
```
## Total recognition accuracy of our top 4 submissions to Emotion Challenge 2017
  Validation(%) | Test(%) |	Methods
  ------------- | ------------- | -------------
  54.57 | 55.74 | 3rd Fusion of 1 SSE-ResNet + 1 SSE-DenseNet + 1 SSE-HoloNet + 1 audio model 
  55.09 | 56.66 | 5th Fusion of 1 SSE-ResNet + 1 SSE-DenseNet + 1 SSE-HoloNet + 1 audio model
  56.14 | 57.58 | 6th Fusion of 1 SSE-ResNet + 1 SSE-DenseNet + 1 SSE-HoloNet + 1 hand-crafted model + 1 audio model
  59.01 | 60.34 | 7th Fusion of 1 SSE-ResNet + 1 SSE-DenseNet + 1 SSE-HoloNet + 1 hand-crafted model + 1 audio model

## Result comparison of our SSE networks on the Emotion Challenge validation set (%)  
  Methods | Original | 3conv-s + Eltwise | 3conv-s + Concat | 4conv-c + Eltwise | 4conv-c + Concat
   ------------- | ------------- | ------------- | ------------- | ------------- | -------------
  DenseNet-121 | 41.3594 | 44.1253 | 45.6919 | 43. 5625 | 44.6719
  HoloNet | 40.9922 | 44.2839 | 46.4752 | 41.4308 | 43.6031
  ResNet-50 | 41.7755 | \ | \ | \ | 42.5587

## SSE Installation
0. Clone the SSE repository 
``` 
    git clone https://github.com/erinhp/SSE.git
```
1. Build Caffe and pycaffe, it can be dowonload from [here](https://github.com/BVLC/caffe/) 
```
   cd $ROOT/caffe
   # Now follow the Caffe installation instructions here:
   #   http://caffe.berkeleyvision.org/installation.html

   # If you're experienced with Caffe and have all of the requirements installed
   # and your Makefile.config in place, then simply do:
   make -j8 && make pycaffe
```
2. Data initialization for training and testing on Emotion Challenge dataset  
   First, we locate and track target faces in the frames of video clips, then cut face regions, scale them to the same size and do face frontalization, at last rescale the frontalized face images to a resolution of 128*128 pixels. For more details, please refer to our ICMI 2017 paper.
3. Train SSE with Emotion Challenge dataset  
   Train a SSE learning Strategy network. For example, train SSE-HoloNet on Emotion Challange train dataset. To train SSE-DenseNet or SSE-ResNet, you can finetune with the pretrained DenseNet/ResNet models. You can find the pretrained DenseNet_121, ResNet_50 models on [BaiduYun](https://pan.baidu.com/s/1cdJvGi) 
```Java
    ./build/tools/caffe train \
    --solver = script/SSE-HoloNet/SSE_holonet_train_solver.prototxt
    --gpu = 0
```  
```Java
    ./build/tools/caffe train \
    --solver = script/SSE-DenseNet/SSE-densenet-121_train.prototxt  \
    --weights = models/pretrained_model/DenseNet_121.caffemodel \
    --gpu = 0 
```    
4. Test SSE with Emotion Challenge dataset  
    Now we provide three models for testing the Emotion Challenge dataset. To use demo you need to download our pretrained SSE models, please download the model manually from [BaiduYun](https://pan.baidu.com/s/1cdJvGi), and put it under `$models`.  
	You can use the command in test_SSE_HoloNet.sh like this to get face emotion recognition result for each frame:
```
   #extract features leveldb
   rm -r examples/sse_holonet_features/ && ./build/tools/extract_features.bin models/SSE/SSE_HoloNet_trval_iter_69500.caffemodel script/SSE-HoloNet/SSE_holonet_test.prototxt prob examples/sse_holonet_features 215 leveldb GPU

   #leveldb to mat
   cd leveldb2mat/ && python leveldb2mat.py ../../examples/sse_holonet_features/ 215 27 7 features.mat
```
