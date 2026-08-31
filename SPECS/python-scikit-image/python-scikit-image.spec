# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname scikit-image
%global pypi_name scikit_image

Name:           python-%{srcname}
Version:        0.26.0
Release:        %autorelease
Summary:        Image processing in Python
License:        BSD-3-Clause
URL:            https://scikit-image.org
VCS:            git:https://github.com/scikit-image/scikit-image
#!RemoteAsset:  sha256:f5f970ab04efad85c24714321fcc91613fcb64ef2a892a13167df2f3e59199fa
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

# fix python not found
Patch2000:         2000-use-python3-for-cythoner.patch

BuildOption(install):  skimage skimage2

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(av)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(imageio)
BuildRequires:  python3dist(imageio-ffmpeg)
BuildRequires:  python3dist(lazy-loader)
BuildRequires:  python3dist(meson-python)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pythran)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(tifffile)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
scikit-image is a collection of algorithms for image processing in Python.
It is designed to interoperate with NumPy and SciPy.

%generate_buildrequires
%pyproject_buildrequires -p

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
