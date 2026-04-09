# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <zhengxingda@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           otf2bdf
Version:        3.1
Release:        %autorelease
Summary:        Utility for rasterizing OpenType fonts to BDF bitmap fonts
License:        MIT
# VCS: No VCS link available
# The upstream disappeared, used to be available at:
# http://www.math.nmsu.edu/~mleisher/Software/otf2bdf/
#!RemoteAsset
Source:         http://deb.debian.org/debian/pool/main/o/otf2bdf/otf2bdf_%{version}.orig.tar.gz
BuildSystem:    autotools

# The following patches are from Debian otf2bdf 3.1-4.1
Patch1:         mkinstalldirs.patch
Patch2:         args.patch
Patch3:         freetype2.patch
# Patch to add DESTDIR installing support to the hand-written Makefile.in
Patch4:         Makefile-Add-DESTDIR.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  pkgconfig(freetype2)

%description
This package provides a otf2bdf command, which utilizes FreeType library to
rasterize OpenType outline fonts to BDF-formatted bitmap fonts.

%conf -p
autoreconf -fiv

%install -p
# Fix permission of the patch-introduced mkinstalldirs script
chmod a+x mkinstalldirs

# No check
%check

%files
%doc README
%{_bindir}/otf2bdf
%{_mandir}/man1/otf2bdf.1*

%changelog
%autochangelog
