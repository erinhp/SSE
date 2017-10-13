import lmdb
import leveldb
import feat_helper_pb2
import numpy as np
import scipy.io as sio
import time
import collections
def main(argv):
    leveldb_name = sys.argv[1]
    print "%s" % sys.argv[1]
    batch_num = int(sys.argv[2]);
    batch_size = int(sys.argv[3]);
    window_num = batch_num*batch_size;

    start = time.time()
    if 'db' not in locals().keys():
        db = leveldb.LevelDB(leveldb_name)
        datum = feat_helper_pb2.Datum()
    it = db.RangeIter()
    
    #ft = np.zeros((int(sys.argv[6]), int(sys.argv[4])))
    ft = np.zeros((window_num, int(sys.argv[4])))
    #featureFile=sys.argv[5]
    #output = open(featureFile, 'wb')
    print "%s" %it
    for key,value in it:
      #print "%d" %int(sys.argv[6])
      #if int(key)==int(sys.argv[6]):
      #  break
      datum.ParseFromString(db.Get(key))
      #if
      print "%s," %key
      print "%d" %len(datum.float_data)
      #str = ' '.join(str(i) for i in datum.float_data)
      #output.write(str)
      #output.write("\n")
      #print "%s" %value.size()
      ft[int(key), :] = datum.float_data
    
    #for im_idx in range(window_num):
      #datum.ParseFromString(db.Get(im_idx))
      #ft[im_idx, :] = datum.float_data
    #sort_features = collections.OrderedDict(sorted(ft.items()))
    #for k, arr  in sort_features.iteritems():
    

    print 'time 1: %f' %(time.time() - start)
    sio.savemat(sys.argv[5], {'feats':ft})
    print 'time 2: %f' %(time.time() - start)
    print 'done!'

    #leveldb.DestroyDB(leveldb_name)

if __name__ == '__main__':
    import sys
    main(sys.argv)
