# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           kdsoap
Version:        2.2.0
Release:        %autorelease
Summary:        A Qt-based client-side and server-side SOAP component
License:        MIT
URL:            https://github.com/KDAB/KDSoap
#!RemoteAsset:  sha256:d9ef11948442197c9fa44bd6fbadc842b7280a60dfc40577af66fded637af356
Source0:        https://github.com/KDAB/KDSoap/releases/download/kdsoap-%{version}/kdsoap-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DKDSoap_EXAMPLES=FALSE
BuildOption(conf):  -DKDSoap_QT6=ON

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  qt6-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Xml)
# for doc generation
# BuildRequires:  doxygen
# BuildRequires:  cmake(Qt6ToolsTools)
# we don't have it yet.
# BuildRequires:  qt6-doc-devel

%description
KDSoap can be used to create client applications for web services
and also provides the means to create web services without the need
for any further component such as a dedicated web server.

%package        devel
Summary:        Development files for kdsoap6
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains header files and associated tools and libraries to
develop programs which need to access web services using the SOAP protocol.

%files
%doc README.md
%license LICENSES/MIT.txt
%{_docdir}/KDSoap-qt6/
%{_libdir}/libkdsoap-server-qt6.so.*
%{_libdir}/libkdsoap-qt6.so.*

%files devel
%doc kdsoap.pri kdwsdl2cpp.pri
%{_libdir}/libkdsoap-server-qt6.so
%{_libdir}/libkdsoap-qt6.so
%{_bindir}/kdwsdl2cpp-qt6
%{_libdir}/cmake/KDSoap-qt6/
%{_libdir}/qt6/mkspecs/modules/*
%{_includedir}/KDSoapClient-Qt6/
%{_includedir}/KDSoapServer-Qt6/

%changelog
%autochangelog
