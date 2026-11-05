# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sane-backends
Version:        1.4.0
Release:        %autorelease
Summary:        Scanner access library, device backends and command line tools
License:        GPL-2.0-or-later AND (GPL-2.0-or-later WITH SANE-exception) AND IJG AND MIT
URL:            https://www.sane-project.org/
VCS:            git:https://gitlab.com/sane-project/backends.git
#!RemoteAsset:  git+https://gitlab.com/sane-project/backends.git#c7e4b5e35e3d614d2b1181d760a717bfc395a203
#!CreateArchive
Source0:        %{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-usb

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  patch
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libjpeg)

%description
SANE provides scanner access through a common C interface. Device
backends support local scanners and scanners shared over the network.
The scanimage command acquires images using the same interface.

%package        devel
Summary:        Development files for the SANE scanner interface
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and build metadata for programs that acquire
images from a SANE device.

%prep -a
# Generate the release build system using the upstream bootstrap script.
./autogen.sh
sed -n '/Copyright (C) 1996 by Scott Laird/,/\*\//p' backend/qcam.h > QCAM-LICENSE.txt

%install -a
# Generate scanner identification for systemd's desktop device-access rules.
tools/sane-desc -m udev+hwdb -s doc/descriptions:doc/descriptions-external > 65-sane.rules
tools/sane-desc -m hwdb -s doc/descriptions:doc/descriptions-external > 20-sane.hwdb
install -Dpm 0644 65-sane.rules %{buildroot}%{_udevrulesdir}/65-sane.rules
install -Dpm 0644 20-sane.hwdb %{buildroot}%{_udevhwdbdir}/20-sane.hwdb
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc %{_docdir}/sane-backends/
%license COPYING LICENSE README.djpeg QCAM-LICENSE.txt
%{_bindir}/gamma4scanimage
%{_bindir}/sane-find-scanner
%{_bindir}/scanimage
%{_bindir}/umax_pp
%{_sbindir}/saned
%{_libdir}/libsane.so.*
%{_libdir}/sane/
%config(noreplace) %{_sysconfdir}/sane.d/
%{_datadir}/sane/
%{_udevrulesdir}/65-sane.rules
%{_udevhwdbdir}/20-sane.hwdb
%{_mandir}/man1/gamma4scanimage.1*
%{_mandir}/man1/sane-find-scanner.1*
%{_mandir}/man1/scanimage.1*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_mandir}/man8/*

%files devel
%{_bindir}/sane-config
%{_mandir}/man1/sane-config.1*
%{_includedir}/sane/
%{_libdir}/libsane.so
%{_libdir}/pkgconfig/sane-backends.pc

%changelog
%autochangelog
