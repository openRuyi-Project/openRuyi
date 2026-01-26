# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmicrohttpd
Version:        1.0.2
Release:        %autorelease
Summary:        Small Embeddable HTTP Server Library
License:        LGPL-2.1-or-later AND GPL-3.0-or-later
URL:            https://www.gnu.org/software/libmicrohttpd/
VCS:            git:git://git.gnunet.org/libmicrohttpd2.git
#!RemoteAsset
Source:         https://ftpmirror.gnu.org/gnu/libmicrohttpd/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-bauth
BuildOption(conf):  --enable-dauth
BuildOption(conf):  --enable-epoll
BuildOption(conf):  --enable-messages
BuildOption(conf):  --enable-postprocessor
BuildOption(conf):  --enable-https
BuildOption(conf):  --enable-curl
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-examples

BuildRequires:  libtool
BuildRequires:  texinfo
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libcurl)

%description
GNU libmicrohttpd is a small C library that makes it easy to run an HTTP
server as part of another application. This package contains the runtime
shared libraries.

%package        devel
Summary:        Development files for libmicrohttpd
License:        LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       pkgconfig(gnutls)

%description    devel
This package contains the header files, pkg-config files, documentation,
and other files needed to develop applications that use libmicrohttpd.

%install -a
rm -v %{buildroot}%{_infodir}/%{name}_performance_data.png

%files
%license COPYING
%{_libdir}/libmicrohttpd.so.*

%files devel
%doc ChangeLog
%{_includedir}/microhttpd.h
%{_libdir}/libmicrohttpd.so
%{_libdir}/pkgconfig/libmicrohttpd.pc
%{_infodir}/libmicrohttpd*.info*
%{_mandir}/man3/libmicrohttpd.*

%changelog
%{?autochangelog}
