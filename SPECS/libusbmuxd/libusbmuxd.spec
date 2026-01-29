# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libusbmuxd
Version:        2.1.1
Release:        %autorelease
Summary:        Client library USB multiplex daemon for Apple's iOS devices
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/libimobiledevice/libusbmuxd
#!RemoteAsset:  sha256:bcc185615a0f4ba80b617696235a084c64b68a1bf546a1dedd85da6b62b8cfbe
Source0:        https://github.com/libimobiledevice/libusbmuxd/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libimobiledevice-glue-1.0)
BuildRequires:  pkgconfig(libplist-2.0)

%description
libusbmuxd is the client library used for communicating with Apple's iPod Touch,
iPhone, iPad and Apple TV devices.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Files for development with %{name}.

%prep -a
echo "%{version}" > .tarball-version

%conf -p
./autogen.sh

%files
%license COPYING
%doc README.md AUTHORS
%{_libdir}/libusbmuxd-2.0.so.*
%{_bindir}/iproxy
%{_bindir}/inetcat
%{_mandir}/man1/iproxy.1*
%{_mandir}/man1/inetcat.1*

%files devel
%{_includedir}/usbmuxd.h
%{_includedir}/usbmuxd-proto.h
%{_libdir}/libusbmuxd-2.0.so
%{_libdir}/pkgconfig/libusbmuxd-2.0.pc

%changelog
%{?autochangelog}
