# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond test 0

Name:           ccache
Version:        4.13.1
Release:        %autorelease
Summary:        A Fast C/C++ Compiler Cache
License:        GPL-3.0-or-later
URL:            https://ccache.dev/
VCS:            git:https://github.com/ccache/ccache
#!RemoteAsset:  sha256:5923c712764b80dd45ed261da4bd8d3908a553615fb5d7ec2512c0c46ed1e9c3
Source:         https://github.com/ccache/ccache/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON
%if %{without test}
BuildOption(conf):  -DENABLE_TESTING:BOOL=OFF
%endif
BuildOption(conf):  -DREDIS_STORAGE_BACKEND:BOOL=OFF
BuildOption(conf):  -DENABLE_DOCUMENTATION:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  pkgconfig(fmt)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxxhash)
%if %{with test}
BuildRequires:  doctest-devel
%endif

Provides:       distcc:%{_bindir}/ccache

%description
ccache is a compiler cache. It speeds up recompilation by caching the
result of previous compilations and detecting when the same compilation is
being done again.

%install -a
# create the compat symlinks into /usr/libdir/ccache
mkdir -p %{buildroot}/%{_libdir}/ccache
cd %{buildroot}/%{_libdir}/ccache
ln -sf ../../bin/ccache gcc
ln -sf ../../bin/ccache g++
# do the same for clang
ln -sf ../../bin/ccache clang
ln -sf ../../bin/ccache clang++
# and regular cc
ln -sf ../../bin/ccache cc
ln -sf ../../bin/ccache c++
# and for nvidia cuda
ln -sf ../../bin/ccache nvcc

%files
%license LICENSE.* GPL-3.0.txt
%doc README.*
%{_bindir}/ccache
%{_libdir}/ccache

%changelog
%autochangelog
