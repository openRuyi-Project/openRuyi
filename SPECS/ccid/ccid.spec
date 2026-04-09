# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global dropdir %(pkg-config libpcsclite --variable usbdropdir 2>/dev/null || echo %{_libdir}/pcsc/drivers)
%global pcsc_lite_ver 1.8.9

Name:           ccid
Version:        1.7.0
Release:        %autorelease
Summary:        Generic USB CCID smart card reader driver
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://ccid.apdu.fr/
VCS:            git:https://salsa.debian.org/rousseau/CCID.git
#!RemoteAsset
Source0:        https://ccid.apdu.fr/files/ccid-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dserial=true

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd
BuildRequires:  flex
BuildRequires:  perl

Requires:       pcsc-lite >= %{pcsc_lite_ver}
%{?systemd_requires}

%description
Generic USB CCID (Chip/Smart Card Interface Devices) driver for use with the
PC/SC Lite daemon.

%install -a
cp -p src/openct/LICENSE LICENSE.openct

%files
%doc AUTHORS README.md
%license COPYING LICENSE.openct
%{dropdir}/ifd-ccid.bundle/
%{dropdir}/serial/
%config(noreplace) %{_sysconfdir}/reader.conf.d/libccidtwin
%{_udevrulesdir}/92_pcscd_ccid.rules

%changelog
%autochangelog
