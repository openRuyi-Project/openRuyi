# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gptfdisk
Version:        1.0.10
Release:        %autorelease
Summary:        An fdisk-like partitioning tool for GPT disks
License:        GPL-2.0-only
URL:            http://www.rodsbooks.com/gdisk/
VCS:            git:https://git.code.sf.net/p/gptfdisk/code
#!RemoteAsset
Source0:        http://downloads.sourceforge.net/gptfdisk/gptfdisk-%{version}.tar.gz
BuildSystem:    autotools

Patch0:         2000-fix-include-ncurses.h-unconditionally.patch

BuildOption(build):  CXXFLAGS="%{optflags}" LDFLAGS="%{build_ldflags} -ltinfo"

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(popt)

%description
An fdisk-like partitioning tool for GPT disks.

GPT fdisk features a command-line interface, fairly direct
manipulation of partition table structures, recovery tools to
help you deal with corrupt partition tables, and the ability
to convert MBR disks to GPT format.

# No configure
%conf

%install
for f in gdisk sgdisk cgdisk fixparts ; do
    install -D -p -m 0755 $f %{buildroot}%{_sbindir}/$f
    install -D -p -m 0644 $f.8 %{buildroot}%{_mandir}/man8/$f.8
done

%check
./gdisk_test.sh

%files
%doc NEWS README
%license COPYING
%{_sbindir}/cgdisk
%{_sbindir}/fixparts
%{_sbindir}/gdisk
%{_sbindir}/sgdisk
%{_mandir}/man8/cgdisk.8*
%{_mandir}/man8/fixparts.8*
%{_mandir}/man8/gdisk.8*
%{_mandir}/man8/sgdisk.8*

%changelog
%autochangelog
