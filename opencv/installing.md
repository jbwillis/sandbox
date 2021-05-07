  890  Apr 28 11:49:59 sudo apt install ccache cmake libopenblas-dev liblapacke-dev libjpeg-dev libtiff-dev libpng-dev libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libatlas-base-dev gfortran libhdf5-serial-dev libeigen3-dev libeigen-stl-containers-dev libavresample-dev libvtk7-dev libprotobuf-dev libgtkglext1-dev libdc1394-22-dev libtbb-dev libceres-dev libcaffe-cuda-dev libleptonica-dev libopenblas-dev coinor-libclp-dev libtesseract-dev tesseract-ocr libogre-1.9-dev ogre-1.9-tools ocl-icd-opencl-dev ocl-icd-libopencl1 opencl-headers clinfo ocl-icd-dev hdf5-tools pybind11-dev python-dev python3-dev python-pip python3-pip
  891  Apr 28 12:00:36 cd Do
  892  Apr 28 12:00:39 cd Downloads/
  893  Apr 28 12:01:38 cd software/
  894  Apr 28 12:12:21 unzip opencv-4.3.0.zip -d opencv-4.3.0
  895  Apr 28 12:12:29 mv opencv-4.3.0/ ../
  896  Apr 28 12:12:40 mv opencv-4.3.0/ ../ocvtmp
  897  Apr 28 12:13:09 mv opencv-4.3.0/ocvtmp/ ../
  898  Apr 28 12:13:11 rm opencv-4.3.0
  899  Apr 28 12:13:17 rm -r opencv-4.3.0
  900  Apr 28 12:13:21 mv ocvtmp/ opencv-4.3.0
  901  Apr 28 12:13:41 mv ../ocvtmp/ opencv-4.3.0
  902  Apr 28 12:13:43 cd opencv-4.3.0/
  903  Apr 28 12:17:04 sudo apt install tesseract
  904  Apr 28 12:17:22 sudo apt install libtesseract-dev tesseract-ocr
  905  Apr 28 12:17:48 sudo apt install libprotobuf-dev libgtkglext1-dev libdc1394-22-dev libtbb-dev libceres-dev libcaffe-cuda-dev libleptonica-dev libopenblas-dev coinor-libclp-dev libtesseract-dev tesseract-ocr libogre-1.9-dev ogre-1.9-tools ocl-icd-opencl-dev ocl-icd-libopencl1 opencl-headers clinfo ocl-icd-dev hdf5-tools pybind11-dev python-dev python3-dev python-pip python3-pip
  924  Apr 28 12:53:18 pip3 install --user ipython numpy scipy pybind11 pygame vtk matplotlib pyqt5 pyside2 pytesseract tesserocr jupyter gnupg
  925  Apr 28 12:53:24 pip3 install ipython numpy scipy pybind11 pygame vtk matplotlib pyqt5 pyside2 pytesseract tesserocr jupyter gnupg
  926  Apr 28 12:54:18 pip3 install pyopencl
  937  Apr 28 13:08:29 sudo apt install zlib1g
  938  Apr 28 13:10:54 sudo apt install libatlas3-base libatlas-base-dev liblapacke-dev 
  941  Apr 28 13:13:22 sudo apt install python3-vtk
  948  Apr 28 13:56:55 sudo apt install libopenjp2-tools 
  950  Apr 28 13:58:05 sudo apt install libopenjpip-viewer 
  960  Apr 28 14:10:01 sudo apt install libvtk6-jni libvtk6.3 libvtk6-dev libvtk6-java
  961  Apr 28 14:11:26 apt list | vtk
  962  Apr 28 14:11:44 sudo apt install python-pyvtk
  973  Apr 28 14:19:22 man update-alternatives 
  974  Apr 28 14:20:05 sudo update-alternatives --install /usr/bin/vtk vtk /usr/bin/vtk6 10
  975  Apr 28 14:20:32 cd ~/software/opencv-4.3.0/build/
  978  Apr 28 14:24:12 sudo apt install python-vtk
  979  Apr 28 14:24:15 sudo apt install python-vtk6
  980  Apr 28 14:24:43 cd /usr/lib/python3/dist-packages/
  981  Apr 28 14:24:48 cd vtk
  982  Apr 28 14:25:49 find . -name libvtkRenderingPythonTkWidgets 2>/dev/null
  983  Apr 28 14:26:30 cd software/opencv-4.3.0/build/
  984  Apr 28 14:28:06 cmake -DCMAKE_INSTALL_PREFIX=/usr/local/opencv              -DCMAKE_BUILD_TYPE=RELEASE              -DWITH_CUDA=ON              -DENABLE_FAST_MATH=1              -DCUDA_FAST_MATH=1              -DWITH_CUBLAS=1              -DINSTALL_PYTHON_EXAMPLES=OFF              -DENABLE_PRECOMPILED_HEADERS=OFF              -DWITH_OPENMP=ON              -DWITH_NVCUVID=ON              -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.3.0/modules              -DBUILD_opencv_cudacodec=OFF              -DPYTHON_DEFAULT_EXECUTABLE=$(which python3)              -DBUILD_USE_SYMLINKS=ON              -DBUILD_PERF_TESTS=OFF              -DBUILD_TESTS=OFF              -DBUILD_JAVA=OFF              -DBUILD_PROTOBUF=ON              -DBUILD_opencv_java_bindings_gen=OFF              -DBUILD_opencv_cnn_3dobj=OFF              -DWITH_GDAL=ON              -DWITH_CLP=ON              -DTesseract_INCLUDE_DIR=/usr/include/tesseract              -DTesseract_LIBRARY=/usr/lib/x86_64-linux-gnu/libtesseract.so              -DOpenBLAS_LIB=/usr/lib/x86_64-linux-gnu/openblas/libblas.so              -DWITH_OPENGL=ON              -DWITH_VULKAN=ON              -DPYTHON3_INCLUDE_DIR2=~/.local/include/python3.6m  -DENABLE_NONFREE=ON  -DWITH_TBB=ON  ..
  985  Apr 28 14:28:35 make -j8
  991  Apr 28 15:20:24 sudo make install
  992  Apr 28 15:21:09 sudo ldconfig
  993  Apr 28 15:21:36 cd /usr/local/opencv/bin/
 1009  Apr 28 15:33:08 vim ~/configs/.bashrc_custom 
 1011  Apr 28 15:33:19 . ~/configs/.bashrc_custom 
 1010  Apr 28 15:33:16 opencv_version 
