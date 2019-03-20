# Overview
This project is to extract the key frames in a given video by distance distribution.  
Distance functions and the number of extracted frames are user-specified.  
The feature of frame is simply the down-sized original frame. Here I use the ratio 0.01.

# Installation
If you want to use the phash-hamming distance, the following library is needed.
```angular2html
pip install imagehash
```


# Extract the frames
```angular2html
python demo.py -f {video file path} -n {number of frames to extract} -d {distance}
```

# Example
```angular2html
python demo.py -f E:\video\RECORD21_0131.20190101010821_2.mp4 -n 100
```
```angular2html
Loading...
The video has 1800 frames!
Start extracting...
Extract frame id:
 [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 121, 130, 140, 152, 171, 213, 238, 258, 299, 330, 366, 412, 452, 471, 494, 543, 601, 656, 679, 712, 773, 828, 875, 898, 923, 968, 1018, 1068, 1107, 1129, 1165, 1206, 1246, 1291, 1324, 1341, 1358, 1371, 1382, 1393, 1404, 1416, 1428, 1440, 1450, 1460, 1470, 1479, 1488, 1497, 1506, 1514, 1522, 1530, 1538, 1545, 1552, 1559, 1566, 1573, 1580, 1587, 1594, 1601, 1609, 1617, 1625, 1634, 1644, 1653, 1661, 1669, 1678, 1689, 1701, 1713, 1724, 1735, 1745, 1753, 1761]
Finished! Cost 13.2 second to extract frames!
The extracted frames are saved at {video_file_dir}/{video_name}/extract_frame_manhattan
```
# Help
```angular2html
python demo.py -h
```
```angular2html
usage: demo.py [-h] --file FILE --frame_number FRAME_NUMBER
               [--distance DISTANCE]

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  video file path
  --frame_number FRAME_NUMBER, -n FRAME_NUMBER
                        number of frames to extract
  --distance DISTANCE, -d DISTANCE
                        distance function manhattan, euclidean, cosine,
                        phash_hamming
```
