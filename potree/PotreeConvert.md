** LAStools编译 Linux **
```
cd ~/dev/workspaces/lastools
git clone https://github.com/m-schuetz/LAStools.git master
cd master/LASzip
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release  -DCMAKE_CXX_COMPILER=/usr/local/bin/g++ ..
make
```

** PotreeConvert 编译 Linux **
```
cd ~/dev/workspaces/PotreeConverter
git clone https://github.com/potree/PotreeConverter.git master
cd master
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DLASZIP_INCLUDE_DIRS=~/dev/workspaces/lastools/master/LASzip/dll -DLASZIP_LIBRARY=~/dev/workspaces/lastools/master/LASzip/build/src/liblaszip.so  -DCMAKE_CXX_COMPILER=/usr/local/bin/g++ ..
make

# copy ./PotreeConverter/resources/page_template to your binary working directory.
```

若报错：
```
error: invalid initialization of non-const reference of type ‘Potree::Point&’ from an rvalue of type ‘Potree::Point’ writer->write(reader->getPoint()); ~~~~~~~~~~~~~~~~^~
```

```
文件：PotreeConverter/PotreeConverter/src/PotreeWriter.cpp

writer->write(reader->getPoint());
修改为：
Potree::Point point = reader->getPoint();
writer->write(point);
```