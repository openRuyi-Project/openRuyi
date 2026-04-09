# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tinyxml2
Version:        11.0.0
Release:        %autorelease
Summary:        Small XML parser for C++
License:        ZLIB
URL:            https://leethomason.github.io/tinyxml2/
VCS:            git:https://github.com/leethomason/tinyxml2
#!RemoteAsset
Source0:        https://github.com/leethomason/tinyxml2/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  gcc-c++
BuildRequires:  meson

%description
TinyXML2 is a small and simple XML parsing library for the
C++ programming language.

%package        devel
Summary:        Development files for the tinyxml2 library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the C++ header files, libraries, and build system files
needed to develop applications that use the tinyxml2 library.

%files
%license LICENSE.txt
%doc readme.md
%{_libdir}/libtinyxml2.so.*

%files devel
%{_includedir}/tinyxml2.h
%{_libdir}/libtinyxml2.so
%{_libdir}/pkgconfig/tinyxml2.pc

%changelog
%autochangelog
