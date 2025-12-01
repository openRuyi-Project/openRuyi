# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libwebsockets
Version:        4.3.3
Release:        %autorelease
Summary:        A lightweight C library for Websockets
License:        LGPL-2.1-or-later and Public-Domain and BSD-3-Clause and MIT and Zlib
URL:            https://libwebsockets.org
#!RemoteAsset
Source0:        https://github.com/warmcat/libwebsockets/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf): -DLWS_WITH_HTTP2:BOOL=ON
BuildOption(conf): -DLWS_IPV6:BOOL=ON
BuildOption(conf): -DLWS_WITH_ZIP_FOPS:BOOL=ON
BuildOption(conf): -DLWS_WITH_SOCKS5:BOOL=ON
BuildOption(conf): -DLWS_WITH_RANGES:BOOL=ON
BuildOption(conf): -DLWS_WITH_ACME:BOOL=ON
BuildOption(conf): -DLWS_WITH_LIBUV:BOOL=OFF
BuildOption(conf): -DLWS_WITH_LIBEV:BOOL=OFF
BuildOption(conf): -DLWS_WITH_LIBEVENT:BOOL=OFF
BuildOption(conf): -DLWS_WITH_FTS:BOOL=ON
BuildOption(conf): -DLWS_WITH_THREADPOOL:BOOL=ON
BuildOption(conf): -DLWS_UNIX_SOCK:BOOL=ON
BuildOption(conf): -DLWS_WITH_HTTP_PROXY:BOOL=ON
BuildOption(conf): -DLWS_WITH_DISKCACHE:BOOL=ON
BuildOption(conf): -DLWS_WITH_LWSAC:BOOL=ON
BuildOption(conf): -DLWS_LINK_TESTAPPS_DYNAMIC:BOOL=ON
BuildOption(conf): -DLWS_WITHOUT_BUILTIN_GETIFADDRS:BOOL=ON
BuildOption(conf): -DLWS_USE_BUNDLED_ZLIB:BOOL=OFF
BuildOption(conf): -DLWS_WITHOUT_BUILTIN_SHA1:BOOL=ON
BuildOption(conf): -DLWS_WITH_STATIC:BOOL=OFF
BuildOption(conf): -DLWS_WITHOUT_CLIENT:BOOL=OFF
BuildOption(conf): -DLWS_WITHOUT_SERVER:BOOL=OFF
BuildOption(conf): -DLWS_WITHOUT_TESTAPPS:BOOL=ON
BuildOption(conf): -DLWS_WITHOUT_TEST_SERVER:BOOL=ON
BuildOption(conf): -DLWS_WITHOUT_TEST_SERVER_EXTPOLL:BOOL=ON
BuildOption(conf): -DLWS_WITHOUT_TEST_PING:BOOL=ON
BuildOption(conf): -DLWS_WITHOUT_TEST_CLIENT:BOOL=ON
BuildOption(conf): -DLWS_WITHOUT_EXTENSIONS:BOOL=OFF
# add -DCMAKE_POLICY_VERSION_MINIMUM=3.5 to try configuring anyway.
BuildOption(conf): -DCMAKE_POLICY_VERSION_MINIMUM:STRING=3.5

BuildRequires:  cmake openssl-devel zlib-devel libev-devel gcc gcc-c++

%description
Libwebsockets (LWS) is a flexible, lightweight pure C library for implementing modern
network protocols easily with a tiny footprint, using a nonblocking event loop.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
This package contains the header files and development libraries needed to
develop applications that use libwebsockets.

%files
%license LICENSE
%doc README.md READMEs/
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/*.h
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/libwebsockets/

%changelog
%{?autochangelog}
