# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mtools
Summary:        Programs for accessing MS-DOS disks without mounting the disks
Version:        4.0.49
Release:        %autorelease
License:        GPL-3.0-or-later
Url:            https://www.gnu.org/software/mtools/
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/mtools/mtools-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-floppyd

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  texinfo
BuildRequires:  autoconf
BuildRequires:  automake

%description
Mtools is a collection of utilities for accessing MS-DOS files.
Mtools allow you to read, write and move around MS-DOS filesystem
files (normally on MS-DOS floppy disks).  Mtools supports Windows95
style long file names, OS/2 XDF disks, and 2m disks

%conf -p
autoreconf -fiv

%install -a
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%files
%license COPYING
%doc README Release.notes
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/mtools.info*

%changelog
%autochangelog
