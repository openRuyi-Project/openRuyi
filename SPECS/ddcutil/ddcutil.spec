# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ddcutil
Version:        2.2.6
Release:        %autorelease
Summary:        Query and update monitor settings
License:        GPL-2.0-or-later
URL:            https://github.com/rockowitz/ddcutil
#!RemoteAsset:  sha256:f61b87074eb839d70e947338d33cc4388e286437131e6c32564fbbb56f2046da
Source0:        https://github.com/rockowitz/ddcutil/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-lib=yes

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(jansson)

Requires:       hwdata
Requires:       i2c-tools

%description
ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.

%package        devel
Summary:        Development files for libddcutil
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for libddcutil.

%conf -p
NOCONFIGURE=1 ./autogen.sh

%files
%license COPYING
%doc AUTHORS NEWS.md README.md CHANGELOG.md
%{_bindir}/ddcutil
%{_datadir}/ddcutil/
%{_mandir}/man1/ddcutil.1*
%{_udevrulesdir}/60-ddcutil-i2c.rules
%{_modulesloaddir}/ddcutil.conf
%{_libdir}/libddcutil.so.*

%files devel
%{_libdir}/libddcutil.so
%{_includedir}/ddcutil*.h
%{_libdir}/cmake/ddcutil/
%{_libdir}/pkgconfig/ddcutil.pc

%changelog
%autochangelog
