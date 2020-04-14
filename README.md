# Tiny-imageNet dataset for CAFFE

> ### Download Tiny-imageNet dataset

link : https://tiny-imagenet.herokuapp.com/


> ### Prepare Tiny-imageNet data set as ILSVRC2012 format of CAFFE

```
Original file list

test/		---   ## we will not use this directory ##
train/
val/
wnids.txt	---	  ## train filename list ##
words.txt	---	  ## wordnet dictionary ##
```

1. Copy all files in list in to the root directory(i.e. **tiny-imagenet-200/**).

   ```
   data_label_annotaion.py
   move_all_files_to_upper_folder.py
   make_dic_from_wdnet.py
   ```

   

2. Move **train/$number/images/$images** to **train/$number/$images** 
   And execute python script **move_all_files_to_upper_folder.py** in root dir.

   ```
   python move_all_files_to_upper_folder.py
   ```

   

3. Parse our train dataset dictionary from wordnet dictionary.

   ```
   python make_dic_from_wdnet.py
   ```

   dic_from_words.txt will be generated



4. Annotate our train, val dataset label as CAFFE format(they used).

   ```
   python data_label_annotation.py
   ```

   You should get **train.txt**, and **val.txt** which are same formats in **$CAFFE_DIR/data/ilsvrc12/**.



※ Keep order in running script ※