# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libplist
Version:        2.7.0
Release:        %autorelease
Summary:        Library for manipulating Apple Binary and XML Property Lists
License:        LGPL-2.0-or-later
URL:            https://www.libimobiledevice.org/
VCS:            git:https://github.com/libimobiledevice/libplist
#!RemoteAsset:  sha256:7ac42301e896b1ebe3c654634780c82baa7cb70df8554e683ff89f7c2643eb8b
Source:         https://github.com/libimobiledevice/libplist/releases/download/%{version}/libplist-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc-c++
BuildRequires:  python3dist(cython)
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  make

%description
libplist is a library for manipulating Apple Binary and XML Property Lists

%package        devel
Summary:        Development package for libplist
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
%{name}, development headers and libraries.

%package     -n python-libplist
Summary:        Python bindings for libplist
Provides:       python3-%{name}
%python_provide python3-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3

%description -n python-libplist
%{name}, python libraries and bindings.

%conf -p
export PYTHON_VERSION="3"

%files
%license COPYING.LESSER
%doc AUTHORS README.md
%{_bindir}/plistutil
%{_libdir}/libplist-2.0.so.*
%{_libdir}/libplist++-2.0.so.*
%{_mandir}/man1/plistutil.*

%files devel
%{_libdir}/pkgconfig/libplist-2.0.pc
%{_libdir}/pkgconfig/libplist++-2.0.pc
%{_libdir}/libplist-*.so
%{_libdir}/libplist++-*.so
%{_includedir}/plist

%files -n python-libplist
%{python3_sitearch}/plist.so

%changelog
%autochangelog
