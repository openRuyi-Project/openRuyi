# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zfp
Version:        1.0.1
Release:        %autorelease
Summary:        Compressed numerical arrays library
License:        BSD-3-Clause
URL:            https://github.com/llnl/zfp
#!RemoteAsset:  sha256:4984db6a55bc919831966dd17ba5e47ca7ac58668f4fd278ebd98cd2200da66f
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake

%description
Zfp is a compressed format for multidimensional floating-point and integer
arrays.

%package        devel
Summary:        Development files for zfp
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and CMake metadata for developing applications with zfp.

%files
%license LICENSE
%{_bindir}/zfp
%{_libdir}/libzfp.so.*

%files devel
%{_includedir}/zfp/
%{_includedir}/zfp.h
%{_includedir}/zfp.hpp
%{_libdir}/cmake/zfp/
%{_libdir}/libzfp.so

%changelog
%autochangelog
