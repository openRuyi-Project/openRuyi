# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname torchvision

%bcond test 0
%bcond rocm 0

Name:           python-%{srcname}
Version:        0.25.0
Release:        %autorelease
Summary:        Image and video datasets for torch deep learning
License:        BSD-3-Clause AND BSD-2-Clause AND MIT
URL:            https://github.com/pytorch/vision
#!RemoteAsset:  sha256:a7ac1b3ab489d71f6e27edfad1e27616e4b8a9b1517e60fce4a950600d3510e8
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    pyproject

Patch0:         0001-python-torchvision-ffmpeg8.patch
Patch2000:      2000-Add-HIP-detect-logic.patch

BuildOption(install):  %{srcname}

BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pybind11)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(wheel)
%if %{with rocm}
BuildRequires:  cmake(hipblas)
BuildRequires:  cmake(hipblaslt)
BuildRequires:  cmake(hipsolver)
BuildRequires:  cmake(hipsparse)
BuildRequires:  cmake(rocm-core)
BuildRequires:  cmake(rocprim)
BuildRequires:  cmake(rocthrust)
%endif

Requires:       python3dist(numpy)
Requires:       python3dist(pillow)
Requires:       python3dist(requests)
Requires:       python3dist(torch)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The torchvision package consists of popular datasets, model architectures,
and common image transformations for computer vision.

%prep -a
# Need some debug info
sed -i -e 's@extra_compile_args["cxx"].append("-g0")@extra_compile_args["cxx"].append("-g")@' setup.py
# Find ffmpeg on fedora
sed -i -e 's@ffmpeg_include_dir = os.path.join(ffmpeg_root, "include")@ffmpeg_include_dir = os.path.join(ffmpeg_root, "include/ffmpeg")@' setup.py
sed -i -e 's@ffmpeg_library_dir = os.path.join(ffmpeg_root, "lib")@ffmpeg_library_dir = os.path.join(ffmpeg_root, "lib64")@'              setup.py

%generate_buildrequires
%pyproject_buildrequires

%build -p
export ROCM_HOME=/usr
export TORCHVISION_USE_WEBP=1

%install -a
# exec permission
for f in `find %{buildroot}%{python3_sitearch} -name '*.py'`; do
    if [ ! -x $f ]; then
        sed -i '1{\@^#!/usr/bin@d}' $f
    fi
done

%check
# torchvision.image is a torch operator .so, not a Python extension module; skip import check
%pyproject_check_import -e torchvision.image
%if %{with test}
%pytest
%endif

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
