# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define version_date 20260627

Name:           json-c
Version:        0.19
Release:        %autorelease
Summary:        JSON implementation in C
License:        MIT
URL:            https://github.com/json-c/json-c
#!RemoteAsset:  sha256:f17a6d7d265cf840dfd8f0f46a606d98c6b5b26dc7cfe27275d1546a213086c8
Source0:        https://github.com/json-c/json-c/archive/json-c-%{version}-%{version_date}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_INSTALL_PREFIX=%{_prefix}
BuildOption(conf):  -DENABLE_THREADING=ON
BuildOption(conf):  -DENABLE_RDRAND=ON
BuildOption(conf):  -DBUILD_STATIC_LIBS=ON
BuildOption(conf):  -DBUILD_SHARED_LIBS=ON

BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  xxd

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects. This package contains the runtime library
and documentation.

%package        devel
Summary:        Development headers and libraries for json-c
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package includes header files, static libraries, and other files
needed for developing applications that use the json-c library.

%prep
%autosetup -p1 -n json-c-json-c-%{version}-%{version_date}

%check -p
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}-build/%{_lib}

%install -a
(cd %{buildroot}%{_libdir}/pkgconfig && ln -s json-c.pc json.pc)
mkdir -p "%{buildroot}%{_docdir}/%{name}"
cp -R doc/html "%{buildroot}%{_docdir}/%{name}/"

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_docdir}/json-c/html/
%{_libdir}/libjson-c.so.*

%files devel
%{_libdir}/libjson-c.so
%{_includedir}/json-c
%{_libdir}/pkgconfig/json-c.pc
%{_libdir}/pkgconfig/json.pc
%dir %{_libdir}/cmake/json-c
%{_libdir}/cmake/json-c/json-c-config.cmake
%{_libdir}/cmake/json-c/json-c-targets-*.cmake
%{_libdir}/cmake/json-c/json-c-targets.cmake
%{_libdir}/libjson-c.a

%changelog
%autochangelog
