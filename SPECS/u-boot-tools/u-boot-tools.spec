# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Hangfan Li <lihangfan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           u-boot-tools
Version:        2026.07
Release:        %autorelease
Summary:        Companion tools for Das U-Boot bootloader
License:        GPL-2.0-only
URL:            https://www.denx.de/project/u-boot/
#!RemoteAsset:  git+https://github.com/u-boot/u-boot.git#v%{version}
#!CreateArchive
Source:         u-boot-%{version}.tar.gz

BuildSystem:    autotools

BuildOption(build):  tools-only

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  make

%description
This package includes some programs from tools directory of u-boot source.

%conf
%{make_build} tools-only_defconfig

%install
install -D -m 755 ./tools/mkimage "%{buildroot}/%{_bindir}/mkimage"
install -D -m 755 ./tools/dumpimage "%{buildroot}/%{_bindir}/dumpimage"
install -D -m 755 ./tools/mkenvimage "%{buildroot}/%{_bindir}/mkenvimage"
install -D -m 755 ./tools/mkeficapsule "%{buildroot}/%{_bindir}/mkeficapsule"
install -D -m 755 ./tools/fdtgrep "%{buildroot}/%{_bindir}/fdtgrep"

# Disable all unrelated tests
%check

%files
%{_bindir}/mkimage
%{_bindir}/dumpimage
%{_bindir}/mkenvimage
%{_bindir}/mkeficapsule
%{_bindir}/fdtgrep

%changelog
%autochangelog
