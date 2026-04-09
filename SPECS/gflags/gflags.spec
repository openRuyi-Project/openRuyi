# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gflags
Version:        2.2.2
Release:        %autorelease
Summary:        Library for commandline flag processing
License:        BSD-3-Clause
URL:            https://gflags.github.io/gflags/
VCS:            git:https://github.com/gflags/gflags
#!RemoteAsset
Source0:        https://github.com/gflags/gflags/archive/v%{version}/gflags-%{version}.tar.gz
BuildSystem:    cmake

Patch0:         0001-gflags-fix_pkgconfig.patch

BuildOption(conf):  -DBUILD_TESTING=ON
BuildOption(conf):  -DINSTALL_HEADERS=ON
BuildOption(conf):  -DREGISTER_BUILD_DIR=OFF
BuildOption(conf):  -DREGISTER_INSTALL_PREFIX=OFF
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
The gflags package contains a library that implements commandline
flags processing. As such it's a replacement for getopt(). It has
increased flexibility, including built-in support for C++ types like
string, and the ability to define flags in the source file in which
they're used.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%files
%license COPYING.txt
%doc AUTHORS.txt ChangeLog.txt README.md
%{_bindir}/gflags_completions.sh
%{_libdir}/libgflags.so.*
%{_libdir}/libgflags_nothreads.so.*

%files devel
%dir %{_includedir}/gflags
%{_includedir}/gflags/*.h
%{_libdir}/libgflags.so
%{_libdir}/pkgconfig/gflags.pc
%{_libdir}/libgflags_nothreads.so
%{_libdir}/cmake/gflags

%changelog
%autochangelog
