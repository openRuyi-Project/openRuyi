# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xerces-c
Version:        3.3.0
Release:        %autorelease
Summary:        Validating XML Parser
License:        Apache-2.0
URL:            https://xerces.apache.org/xerces-c/
VCS:            git:https://github.com/apache/xerces-c
#!RemoteAsset:  sha256:0f28ea2d7a0a3824d326c8bc4be26a3bb01dde289663beb6f15b241f80cbd3ae
Source0:        https://github.com/apache/xerces-c/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  dos2unix

%description
Xerces-C is a validating XML parser written in a portable subset of C++.
Xerces-C makes it easy to give your application the ability to read and write
XML data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and development libraries for %{name}.

%files
%license LICENSE
%{_bindir}/*
%{_libdir}/libxerces-c-3.3.so
%{_docdir}/xerces-c/

%files devel
%{_includedir}/xercesc/
%{_libdir}/cmake/XercesC/
%{_libdir}/libxerces-c.so
%{_libdir}/pkgconfig/xerces-c.pc

%changelog
%autochangelog
