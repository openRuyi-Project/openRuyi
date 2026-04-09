# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jsoncpp
Version:        1.9.6
Release:        %autorelease
Summary:        A C++ library for manipulating JSON values
License:        MIT
URL:            https://github.com/open-source-parsers/jsoncpp
#!RemoteAsset
Source0:        https://github.com/open-source-parsers/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig

%description
JsonCpp is a C++ library that allows manipulating JSON values. This package
contains the runtime shared library.

%package        devel
Summary:        Development files for the jsoncpp library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, and CMake files needed to
develop applications that use the JsonCpp library.

%files
%license LICENSE
%{_libdir}/libjsoncpp.so.*

%files devel
%license LICENSE
%doc AUTHORS README.md
%dir %{_libdir}/cmake/jsoncpp/
%dir %{_libdir}/cmake
%{_libdir}/pkgconfig/jsoncpp.pc
%{_libdir}/cmake/jsoncpp/jsoncppConfig.cmake
%{_libdir}/cmake/jsoncpp/jsoncpp-namespaced-targets.cmake
%{_libdir}/libjsoncpp.so
%{_includedir}/json/

%changelog
%autochangelog
