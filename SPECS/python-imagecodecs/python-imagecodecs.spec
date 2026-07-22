# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname imagecodecs

Name:           python-%{srcname}
Version:        2026.6.26
Release:        %autorelease
Summary:        Image transformation and compression codecs
License:        BSD-3-Clause
URL:            https://github.com/cgohlke/imagecodecs
#!RemoteAsset:  sha256:da95b145f6b4f746acc9e0b8707b164eefc6a36ade3b6e70f74d102e9affad8c
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l imagecodecs

BuildRequires:  pkgconfig(Lerc)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libdeflate)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxr)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(numcodecs)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(zarr)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Imagecodecs provides block-oriented image transformation, compression, and
decompression codecs for scientific image I/O libraries.

%files -f %{pyproject_files}
%doc CHANGES.rst
%doc README.rst
%license LICENSE
%{_bindir}/imagecodecs

%changelog
%autochangelog
