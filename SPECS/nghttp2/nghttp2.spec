# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nghttp2
Version:        1.66.0
Release:        %autorelease
Summary:        Implementation of Hypertext Transfer Protocol version 2 in C
License:        MIT
URL:            https://nghttp2.org/
VCS:            git:https://github.com/nghttp2/nghttp2
#!RemoteAsset
Source0:        https://github.com/nghttp2/nghttp2/releases/download/v%{version}/nghttp2-%{version}.tar.xz
#!RemoteAsset
Source1:        https://github.com/nghttp2/nghttp2/releases/download/v%{version}/nghttp2-%{version}.tar.xz.asc
Source2:        nghttp2.keyring
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules
# Attention: for now,wo can only build shared library
BuildOption(conf):  --disable-app

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python3-rpm-macros
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(openssl)

%description
This is an implementation of Hypertext Transfer Protocol version 2.

The framing layer of HTTP/2 is implemented as a form of reusable C library.
On top of that, we have implemented HTTP/2 client, server and proxy. We
have also developed load test and benchmarking tool for HTTP/2.

HPACK encoder and decoder are available as public API.

%package        devel
Summary:        Development files for nghttp2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for usage with libnghttp2, which implements
Hypertext Transfer Protocol version 2.

%prep
%autosetup -p1 -n nghttp2-%{version}

%install -a
rm -rf %{buildroot}%{_mandir}/man1/
rm -f %{buildroot}%{_datadir}/nghttp2/fetch-ocsp-response
rm -f %{buildroot}%{_docdir}/nghttp2/README.rst

%files
%license COPYING
# The main package now only contains the library
%{_libdir}/libnghttp2.so.14
%{_libdir}/libnghttp2.so.14.*

%files devel
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/%{name}*.h
%{_libdir}/libnghttp2.so
%{_libdir}/pkgconfig/libnghttp2.pc

%changelog
%autochangelog
