# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           socket_wrapper
Version:        1.5.0
Release:        %autorelease
Summary:        A library passing all socket communications through Unix sockets
License:        BSD-3-Clause
URL:            http://cwrap.org/
#!RemoteAsset
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
BuildSystem:    cmake

# Fix tests
Patch0:         0001-swrap-fix-tests.patch

BuildOption(conf):  -DUNIT_TESTING=ON

BuildRequires:  cmake
BuildRequires:  cmocka-cmake

Recommends:     cmake
Recommends:     pkgconfig

%description
socket_wrapper aims to help client/server software development teams willing to
gain full functional test coverage. It makes it possible to run several
instances of the full software stack on the same machine and perform locally
functional testing of complex network configurations.

To use it set the following environment variables:

LD_PRELOAD=libsocket_wrapper.so
SOCKET_WRAPPER_DIR=/path/to/swrap_dir

This package doesn't have a devel package because this project is for
development/testing.

%package  -n    libsocket_wrapper_noop
Summary:        A library providing dummies for socket_wrapper

%description -n libsocket_wrapper_noop
Applications with the need to call socket_wrapper_enabled() should link against
-lsocket_wrapper_noop in order to resolve the symbol at link time.

%package -n     libsocket_wrapper_noop-devel
Summary:        Development headers for libsocket_wrapper_noop
Requires:       libsocket_wrapper_noop = %{version}-%{release}

%description -n libsocket_wrapper_noop-devel
Development headers for applications with the need to call
socket_wrapper_enabled().

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libsocket_wrapper.so*
%dir %{_libdir}/cmake/socket_wrapper
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config-version.cmake
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config.cmake
%{_libdir}/pkgconfig/socket_wrapper.pc
%{_mandir}/man1/socket_wrapper.1*

%files -n libsocket_wrapper_noop
%{_libdir}/libsocket_wrapper_noop.so.*

%files -n libsocket_wrapper_noop-devel
%{_includedir}/socket_wrapper.h
%{_libdir}/libsocket_wrapper_noop.so
%{_libdir}/cmake/socket_wrapper/socket_wrapper_noop-config*.cmake
%{_libdir}/pkgconfig/socket_wrapper_noop.pc

%changelog
%{?autochangelog}
