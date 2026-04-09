# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libimobiledevice
Version:        1.4.0
Release:        %autorelease
Summary:        Library for connecting to mobile devices
License:        LGPL-2.0-or-later
URL:            https://libimobiledevice.org/
VCS:            git:https://github.com/libimobiledevice/libimobiledevice
#!RemoteAsset:  sha256:99e042acc1513815c36816723de52e0d0892e081f36ec29672531ce99ed59ccd
Source0:        https://github.com/libimobiledevice/libimobiledevice/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-cython

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libimobiledevice-glue-1.0)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libusbmuxd-2.0)
BuildRequires:  pkgconfig(libtatsu-1.0)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(readline)

%description
libimobiledevice is a library for connecting to mobile devices including phones
and music players.

%package        devel
Summary:        Development package for libimobiledevice
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Files for development with libimobiledevice.

%prep -a
echo %{version} > .tarball-version

%conf -p
./autogen.sh

%files
%license COPYING.LESSER
%doc AUTHORS README.md
%{_libdir}/libimobiledevice-1.0.so.*
%{_bindir}/afcclient
%{_bindir}/idevice*
%{_mandir}/man1/afcclient.1*
%{_mandir}/man1/idevice*.1*

%files devel
%{_libdir}/pkgconfig/libimobiledevice-1.0.pc
%{_libdir}/libimobiledevice-1.0.so
%{_includedir}/libimobiledevice/

%changelog
%autochangelog
