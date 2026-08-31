# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname imageio

Name:           python-%{srcname}
Version:        2.37.3
Release:        %autorelease
Summary:        Library for reading and writing a wide range of image formats
License:        BSD-2-Clause
URL:            https://imageio.readthedocs.io/
VCS:            git:https://github.com/imageio/imageio
#!RemoteAsset:  sha256:bbb37efbfc4c400fcd534b367b91fcd66d5da639aaa138034431a1c5e0a41451
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# https://github.com/imageio/imageio/commit/dfdc909c225662784c7c9469232bbe46ea983501
Patch1000:      1000-support-tifffile-axes-codes.patch

BuildOption(install):  -l imageio
# Skip tests: No module named 'SimpleITK'
# Wait for SimpleITK 3.0 release, it will switch from setuptools.build_meta to scikit-build-core.
BuildOption(check):  -e 'imageio.plugins.simpleitk'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(astropy)
BuildRequires:  python3dist(av)
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(gdal)
BuildRequires:  python3dist(imageio-ffmpeg)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(opencv)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(rawpy)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tifffile)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Imageio is a Python library that provides an easy interface to read and
write a wide range of image data, including animated images, volumetric
data, and scientific formats.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/imageio_download_bin
%{_bindir}/imageio_remove_bin

%changelog
%autochangelog
