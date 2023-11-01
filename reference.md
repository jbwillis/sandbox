# General Reference
This is an accumulation of things I have found useful in my use of different
linux tools. 
Hopefully it ends up being a reference that prevents me from googling the same thing multiple times.

## Box with Linux
Box doesn't provide a native synchronization application for Linux. Most of the search results for "box with linux" are quite old and suggest using a webDAV interface. I tried this and found it to perform miserably, I believe because it was re-reading my entire box filesystem every time I opened a directory. As an alternative, I found [`rclone`](https://rclone.org/). It took me an hour or so to set up and works beautifully. 
Here's some resources I found helpful for setting up `rclone`:
* [BYU office of research computing uses rclone for syncing to box from their supercomputers](https://rc.byu.edu/wiki/?id=Rclone)
* [A blog post on using box with linux](https://daniel.perez.sh/blog/2019/box-linux/)
	* This follows a slightly different set up proceedure than I did but it provides a good (brief) description of common commands.
* [Rclone's Documentation](https://rclone.org/docs/)

### Install
Here's the steps I followed:
1. Installation:
	* The rclone package in apt is out of date, but rclone makes it easy to install using a [provided install script](https://rclone.org/install/):
	* `curl https://rclone.org/install.sh | sudo bash`
2. Box set up:
	* This is the process I used with `rclone v1.51.0`, it might differ sligthly (some of the other guides I found had slightly different steps).
	* `rclone config`

```
No remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q> n
name> desired-remote-name
```
```
Type of storage to configure.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
Storage> box
```
```
Box App Client Id.
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_id> 
```
```
Box App Client Secret
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_secret> 
```
```
Box App config.json location
Leave blank normally.
Enter a string value. Press Enter for the default ("").
box_config_file> 
```
```
Enter a string value. Press Enter for the default ("user").
Choose a number from below, or type in your own value
 1 / Rclone should act on behalf of a user
   \ "user"
 2 / Rclone should act on behalf of a service account
   \ "enterprise"
box_sub_type> user
```
```
Edit advanced config? (y/n)
y) Yes
n) No (default)
y/n> n
Remote config
Use auto config?
 * Say Y if not sure
 * Say N if you are working on a remote or headless machine
y) Yes (default)
n) No
y/n> Y
```
At this point a browser window will open with a box login option.
If you're using a university box account, click the `sign in with sso` option below the username and password boxes. Enter the university email associated with the account, and sign in.

```
Waiting for code...
Got code
--------------------
[um-box]
type = box
token = ...
--------------------
y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d> 
```

**Done!**

### Usage
* To copy a file to the remote (box)
	* `rclone copy local_file desired-remote-name:path/to/desired/directory`
	* Note that the source (first path) can be a file or a directory, but the destination must be a directory.
* To check the differences between a local directory and a remote directory
	* `rclone check local_dir desired-remote-name:remote_dir`
* To synchronized changed files in a source directory to a destination directory (one way, this will overwrite changes in the destination)
	* `rclone sync source destination`

#### My typical workflow
I think I will follow a workflow similar to that with git. Many of the files I will be using with this are binary, so it is more important to make sure that changes are monitored. It will be hard (impossible) to merge two sets of changes into one file. Box maintains a version history of files and creates a new version each time rclone copies in a modified file with the same filename. This could be used, for example, to get changes made by two different people and merge them manually.
1. Check if there are differences between the remote and the local.
	* If there are differences, determine which to keep (essentially a merge)
2. Sync to keep the desired changes
3. Work on files
4. Sync local to remote

## Git
* To have git "forget" about a file that is tracked but is now in gitignore
	* `git rm --cached <file>`
	* This will delete the file when others pull the commit, but works fine for files that are generated on a build.

## Julia

* Convert meshcat frames to video
`ffmpeg -r 60 -i %07d.png -vcodec libx264 -pix_fmt yuv420p -preset slow -crf 18 output2.mp4`

## Jupyter
It seems that the modern Jupyter Notebook system is jupyterlab. This can be installed simply by running `pip3 install jupyterlab`.
I looked into using a Docker image to encapsulate the jupyterlab installation, but since I didn't use anaconda to set up my notebooks, it seems that it isn't actually that messy to just intall jupyterlab.

One feature that I really want in my jupyter notebooks is for them to be as similar to latex documents as possible. The following extension seems to acheive that [jupyter_latex_envs](https://github.com/jfbercher/jupyter_latex_envs). 

To install extensions it is necessary to install Node.js and npm (the nodejs package manager).
To do this I did the following (see https://github.com/nodesource/distributions#debinstall):
```
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Interesting Features
* C++ jupyter notebooks using xeus-cling (a nice description on Medium https://blog.jupyter.org/interactive-workflows-for-c-with-jupyter-fe9b54227d92)
* Vim keybinding
* nbviewer and binder for my git repos
* nbdime (diff tool for notebooks)
* Printing variables from code in markdown (https://data-dive.com/jupyterlab-markdown-cells-include-variables)
* Using either mkdocs-material or jupyterbooks to produce a nice webpage/blog interface for my notebooks

### Jupyter Notebooks vs Jupyter lab
It seems that while jupyterlab is the most modern system in the jupyter ecosystem, it doesn't have the number of extensions that jupyter notebooks do and is not compatible with jupyter notebook extensions. Frustrating, since this could mean that notebooks which take advantage of one type of extension won't work in the other environment. I have found, however that some of the most useful extensions (for me) aren't available in jupyterlab, so I am going to use jupyter notebooks instead.

#### Interesting Extensions
* jupyter_latex_envs (linked above)
* python-markdown/main
  * allows python variables to be printed in markdown

#### Installing Jupyter Notebook Extensions
* `pip3 install jupyter_contrib_nbextensions`
* `jupyter nbextensions_configurator enable`
* `jupyter contrib nbextension install --user`
* `pip3 install jupyter_latex_envs`
* `jupyter nbextension install --py latex_envs --user`
* `jupyter nbextension enable latex_envs --user --py`

## Matlab
* To add MATLAB to system path on mac
  * `ln -s /Applications/MATLAB_R2021b.app/bin/matlab /usr/local/bin/matlab`
* To open matlab without the GUI. This will still open GUIs for figures too.
	* `matlab -nodesktop`
* Debugging
	| Command | Action |
	|---------|--------|
	|`dbstop in myfile at ##` |Set a breakpoint in myfile on line ## | 
	| `dbstop in myprogram at 6 if n>=4` | Conditional breakpoint in myfile on line ## |
	| `dbstatus` | List breakpoints |
	| `dbcont` | Continue debugging |
	| `dbclear all` | Clear all breakpoints |
	| `dbclear in file at location` | removes the breakpoint set at the location in file |
	| `dbquit` | Terminates debug mode |


## Linux
* Spell check
	* `aspell` will spell check a text file. 
* Manually add internet connection
	* I tested this on a raspberry pi
	* `sudo vi /etc/wpa_supplicant/wpa_supplicant.conf`
		* Modify to add additional network
```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
        ssid="network 1"
        psk="password 1"
        priority=1
}
network={
        ssid="network 2"
        psk="password 2"
        priority=2
        key_mgmt=WPA-PSK
}
```
* Reconfigure wpa
	* ` wpa_cli -i wlan0 reconfigure`

## LaTeX
* To recompile live, use `latexmk`
  * `latexmk -pvc -pdf main.tex`
  * There needs to be a ~/.latexmkrc file containing the following:
```
$pdflatex = 'pdflatex -interaction=nonstopmode';
$pdf_previewer = '/usr/bin/evince';
```

## OpenCV

**ROS Melodic Already Installs OpenCV 3.2**. Until I need something else, I am going to stick with 3.2.

Installing opencv is quite a pain. The official [OpenCV installation tutorial](https://docs.opencv.org/4.2.0/d7/d9f/tutorial_linux_install.html) doesn't do a very good job explaining what dependencies need to be installed, and since the installation involves compiling from source, it won't automatically update the dependencies for you. While installing, I referenced the following tutorials:

* [The official OpenCV installation tutorial](https://docs.opencv.org/4.2.0/d7/d9f/tutorial_linux_install.html)
   * This tutorial gives the bare bones installation instructions. I think it gives the best overview of what needs to be done, which helps with understanding the longer processes described in the other tutorials.
* [PyImageSearch Tutorial](https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/)
   * This explains how to install OpenCV for python, which I think is essentially just installing OpenCV.
   * I didn't worry about the virtual environment stuff (though that's more laziness than anything on my part)
* [MAGICC OpenCV with Cuda](https://magiccvs.byu.edu/wiki/#!sw_guides/opencv.md)
   * This is focused on installing OpenCV with Cuda support, but many of the steps (and dependencies) are the same as without Cuda. 
   * It has multiple points where it reccomends a full reboot before continuing which the other tutorials did not have.

As I was doing the OpenCV install, I also installed the RealSense SDK, since it is likely I will be using it at some point. [There are instructions on the Real Sense Github](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md)

This is the set of packages I installed prior to building OpenCV
```
sudo apt install build-essential cmake libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev libtbb2 libtbb-dev libdc1394-22-dev libjpeg-dev libpng-dev libtiff-dev

sudo apt install libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libatlas-base-dev gfortran libhdf5-dev libeigen3-dev libeigen-stl-containers-dev libavresample-dev zlib1g libatlas3-base libatlas-base-dev liblapacke-dev libvtk7-jni libvtk7-dev libvtk7-java libopenjp2-tools libprotobuf-dev libgtkglext1-dev libtbb-dev libceres-dev libleptonica-dev coinor-libclp-dev libtesseract-dev tesseract-ocr libogre-1.12-dev ogre-1.12-tools ocl-icd-opencl-dev ocl-icd-libopencl1 opencl-headers clinfo ocl-icd-dev hdf5-tools pybind11-dev python3-dev

pip3 install ipython numpy scipy pybind11 pygame vtk matplotlib pyqt5 pyside2 pytesseract tesserocr jupyter gnupg pyopencl
```

This is the final cmake command I used on my laptop (no cuda). **Make sure to set the correct path to `opencv_contrib`**
```
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_CUDA=OFF -D INSTALL_PYTHON_EXAMPLES=ON -DOPENCV_EXTRA_MODULES_PATH=~/downloads/opencv_build/opencv_contrib-4.2.0/modules -D OPENCV_ENABLE_NONFREE=ON -D BUILD_EXAMPLES=ON -D PYTHON_DEFAULT_EXECUTABLE=$(which python3) -DBUILD_USE_SYMLINKS=ON -DBUILD_PERF_TESTS=OFF -DBUILD_JAVA=OFF \
-DBUILD_opencv_java_bindings_gen=OFF \
-DWITH_GDAL=ON \
-DWITH_CLP=ON \
-DTesseract_INCLUDE_DIR=/usr/include/tesseract \
-DTesseract_LIBRARY=/usr/lib/x86_64-linux-gnu/libtesseract.so \
-DOpenBLAS_LIB=/usr/lib/x86_64-linux-gnu/openblas/libblas.so \
-DWITH_OPENGL=ON \
-DWITH_VULKAN=ON \
-DWITH_LIBREALSENSE=On \
-DLIBREALSENSE_INCLUDE_DIR=/usr/include/librealsense2 \
..
```

## Pixhawk/PX4
The PX4 [install instructions](https://dev.px4.io/master/en/setup/dev_env_linux_ubuntu.html) only provide a script to download and install the necessary toolchain for building and running PX4. This is a real pain since it assumes it is being run on a clean Ubuntu install. I decided to just run it and cross my fingers that things would work out. The following are notes from this experience.

* `~/catkin_ws.sh` is used by the ROS install script. This is a commonly used directory for ROS tutorials and may get overwritten. Make sure you don't have anything there.
* I had to manually install `GeographicLib`:
	* `sudo apt install geographiclib-tools ros-melodic-geographic-msgs libgeographic-dev`
* I had to add the `future` module to my `python2` install
	* `python2 -m pip install future`

## PSOPT
Installing PSOPT is a bit of a rabbit hole. I installed PSOPT 5, which required updating my machine to Ubuntu 20 since it relied on some CMake features not available prior to CMake 3.12, and CMake 3.10 is bundled with Ubuntu 18. Because of the strong ties ROS has to CMake, I decided the best path forward would be to update to Ubuntu 20. So that's step 1.

PSOPT also relies on installing IPOPT as the optimizer. There's a [decent install guide for IPOPT](https://coin-or.github.io/Ipopt/INSTALL.html), but there are some important notes. 

### HSL
To install the HSL dependency using the `ThirdParty-HSL` repository you still need to get the HSL source by applying for an academic license. 
Additionally it is important to run `make` inside of the extracted `.zip` archive of HSL.

### MUMPS
PSOPT relies on the MUMPS solver to be installed with IPOPT. To do this, you can use the `ThirdParty-Mumps` repository provided by COIN-OR. But, I had to add the `--with-mumps-cflags="-I/usr/local/include/coin-or/mumps"` and the `--with-mumps-lflags="-lcoinmumps"` flags to the `../configure` command for configuring IPOPT.
```
../configure --with-mumps-cflags="-I/usr/local/include/coin-or/mumps" --with-mumps-lflags="-lcoinmumps"
```

**It is also necessary to update the linker using ldconfig before running any of the PSOPT programs**
```
$ sudo ldconfig
```

## Python
* To re-load a module that you have changed
  ```
  from importlib import reload
  import foo
  # time passes and foo gets changed
  foo = reload(foo)
  ```
* Shebang
	`#!/usr/bin/env python3`

## Tmux
* To re-load the configuration file
	* Ctrl-A then `:`
	* `:source ~/.tmux.conf`
* To rename a window
	* Ctrl-A then `:`
	* `:rename-window <name>`

## Vim
* To diff two buffers in vim:
	* Navigate to the buffer and then `:diffthis`
* Useful diff commands (from https://unix.stackexchange.com/questions/52754/whats-the-recommended-way-of-copying-changes-with-vimdiff)
```
]c               - advance to the next block with differences
[c               - reverse search for the previous block with differences
do (diff obtain) - bring changes from the other file to the current file
dp (diff put)    - send changes from the current file to the other file
zo               - unfold/unhide text
zc               - refold/rehide text
zr               - unfold both files completely
zm               - fold both files completely
```
* EasyAlign
	* (github.com/junegunn/vim-easy-align`)
	* To align to an '='
		* Select the text in visual mode
		* `ga=`
