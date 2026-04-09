# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           thrift
Version:        0.22.0
Release:        %autorelease
Summary:        Software framework for scalable cross-language services development
License:        Apache-2.0
URL:            https://thrift.apache.org
VCS:            git:https://github.com/apache/thrift
#!RemoteAsset
Source0:        https://github.com/apache/thrift/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DWITH_CPP:BOOL=ON
BuildOption(conf):  -DWITH_PYTHON:BOOL=OFF
BuildOption(conf):  -DWITH_JAVA:BOOL=OFF
BuildOption(conf):  -DWITH_JAVASCRIPT:BOOL=OFF
BuildOption(conf):  -DWITH_NODEJS:BOOL=OFF
BuildOption(conf):  -DWITH_C_GLIB:BOOL=OFF
BuildOption(conf):  -DWITH_AS3:BOOL=OFF
BuildOption(conf):  -DCMAKE_INSTALL_DIR:PATH=%{_lib}/cmake
BuildOption(conf):  -DPKGCONFIG_INSTALL_DIR:PATH=%{_lib}/pkgconfig
# Skip network-dependent tests that require localhost connections
# and locale tests that require de_DE locale (not installed in build env)
BuildOption(check):  --exclude-regex "TServerIntegrationTest|TInterruptTest|UnitTests|StressTestConcurrent|StressTestNonBlocking|SecurityTest|SecurityFromBufferTest"

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(openssl)

%description
Apache Thrift is a software framework for scalable cross-language services
development. It combines a software stack with a code generation engine to
build services that work efficiently and seamlessly between C++, Java, Python,
PHP, Ruby, Erlang, Perl, Haskell, C#, Cocoa, JavaScript, Node.js, Smalltalk,
OCaml and Delphi and other languages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and pkg-config files for Apache Thrift.

%files
%license LICENSE
%doc README.md
%{_libdir}/libthrift*.so.*
%{_bindir}/thrift

%files devel
%{_includedir}/thrift/
%{_libdir}/libthrift*.so
%{_libdir}/cmake/thrift/
%{_libdir}/pkgconfig/thrift.pc
%{_libdir}/pkgconfig/thrift-nb.pc
%{_libdir}/pkgconfig/thrift-z.pc

%changelog
%autochangelog
