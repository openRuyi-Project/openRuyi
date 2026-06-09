# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname opencv-python-headless

Name:           python-%{srcname}
Version:        5.0.0
Release:        %autorelease
Summary:        Headless Python bindings for OpenCV
License:        Apache-2.0
URL:            https://opencv.org
VCS:            git:https://github.com/opencv/opencv.git
#!RemoteAsset:  sha256:b0528f5a1d379d59d4701cb28c36e22214cc51cf64594e5b56f2d3e6c0233095
Source0:        https://github.com/opencv/opencv/archive/%{version}/opencv-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_BUILD_TYPE=Release
BuildOption(conf):  -DCMAKE_SKIP_INSTALL_RPATH=ON
BuildOption(conf):  -DENABLE_PRECOMPILED_HEADERS=OFF
# Use system libraries instead of bundled 3rdparty
BuildOption(conf):  -DBUILD_ZLIB=OFF
BuildOption(conf):  -DBUILD_TIFF=OFF
BuildOption(conf):  -DBUILD_OPENJPEG=OFF
BuildOption(conf):  -DBUILD_JASPER=OFF
BuildOption(conf):  -DBUILD_JPEG=OFF
BuildOption(conf):  -DBUILD_PNG=OFF
BuildOption(conf):  -DBUILD_OPENEXR=OFF
BuildOption(conf):  -DBUILD_WEBP=OFF
BuildOption(conf):  -DBUILD_TBB=OFF
BuildOption(conf):  -DBUILD_PROTOBUF=ON
# Build options
BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DBUILD_TESTS=OFF
BuildOption(conf):  -DBUILD_PERF_TESTS=OFF
BuildOption(conf):  -DBUILD_DOCS=OFF
BuildOption(conf):  -DBUILD_EXAMPLES=OFF
BuildOption(conf):  -DBUILD_opencv_apps=OFF
BuildOption(conf):  -DBUILD_JAVA=OFF
# Enable pkgconfig generation
BuildOption(conf):  -DOPENCV_GENERATE_PKGCONFIG=OFF
# Library features
BuildOption(conf):  -DWITH_EIGEN=ON
BuildOption(conf):  -DWITH_FFMPEG=ON
BuildOption(conf):  -DWITH_GSTREAMER=ON
BuildOption(conf):  -DWITH_GTK=OFF
BuildOption(conf):  -DWITH_JASPER=ON
BuildOption(conf):  -DWITH_JPEG=ON
BuildOption(conf):  -DWITH_OPENJPEG=ON
BuildOption(conf):  -DWITH_OPENEXR=ON
BuildOption(conf):  -DWITH_PNG=ON
BuildOption(conf):  -DWITH_TIFF=ON
BuildOption(conf):  -DWITH_WEBP=ON
BuildOption(conf):  -DWITH_TBB=ON
BuildOption(conf):  -DWITH_V4L=ON
BuildOption(conf):  -DWITH_LAPACK=ON
BuildOption(conf):  -DWITH_PROTOBUF=ON
BuildOption(conf):  -DWITH_FLATBUFFERS=ON
BuildOption(conf):  -DWITH_OPENCL=ON
# Disable features not available or not needed
BuildOption(conf):  -DWITH_CUDA=OFF
BuildOption(conf):  -DWITH_VTK=OFF
BuildOption(conf):  -DWITH_IPP=OFF
BuildOption(conf):  -DWITH_HALIDE=OFF
BuildOption(conf):  -DWITH_VULKAN=OFF
BuildOption(conf):  -DWITH_QT=OFF
BuildOption(conf):  -DWITH_OPENGL=OFF
BuildOption(conf):  -DWITH_OPENVINO=OFF
BuildOption(conf):  -DWITH_1394=OFF
BuildOption(conf):  -DWITH_AVIF=OFF
# Disable setup_vars script generation
BuildOption(conf):  -DOPENCV_GENERATE_SETUPVARS=OFF
# Enable Python 3 bindings
BuildOption(conf):  -DBUILD_opencv_python2=OFF
BuildOption(conf):  -DBUILD_opencv_python3=ON

BuildRequires:  cmake
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(numpy)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-riff-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  jasper-devel
BuildRequires:  openblas-devel

Requires:       python3dist(numpy)
Requires:       opencv%{?_isa} >= %{version}
Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}
Conflicts:      python-opencv-python
Conflicts:      python3-opencv-python
Conflicts:      python3dist(opencv-python)

%description
OpenCV (Open Source Computer Vision Library) is an open-source computer vision
and machine learning software library. OpenCV was built to provide a common
infrastructure for computer vision applications and to accelerate the use of
machine perception in the commercial products.

%generate_buildrequires
cd modules/python/package
%pyproject_buildrequires

%build -a
cd %{__cmake_builddir}/python_loader/
%pyproject_wheel

%install
DESTDIR=%{buildroot} cmake --install %{__cmake_builddir} --component python
cd %{__cmake_builddir}/python_loader/
%pyproject_install
%pyproject_save_files cv2

%files
%{python3_sitelib}/opencv*.dist-info
%{python3_sitelib}/cv2
%doc README.md
%license LICENSE

%changelog
%autochangelog
