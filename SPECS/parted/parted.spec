# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Summary:   The GNU disk partition manipulation program
Name:      parted
Version:   3.6
Release:   %autorelease
URL:       https://www.gnu.org/software/parted/
#!RemoteAsset
Source0:   https://ftpmirror.gnu.org/gnu/parted/parted-%{version}.tar.xz
Patch0:    0001-fix-do_version-parameters.patch
License:   GPLv3+

BuildRequires: readline-devel gettext-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: texinfo
BuildRequires: gcc
BuildRequires: make util-linux-devel

BuildSystem: autotools
BuildOption(conf): --enable-shared
BuildOption(conf): --disable-device-mapper
BuildOption(conf): --disable-static

%description
The GNU Parted program allows you to create, destroy, resize, move,
and copy hard disk partitions. Parted can be used for creating space
for new operating systems, reorganizing disk usage, and copying data
to new hard disks.

%package devel
Summary:  Files for developing apps which will manipulate disk partitions
Requires: %{name} = %{version}-%{release}
%description devel
The GNU Parted library is a set of routines for hard disk partition
manipulation. If you want to develop programs that manipulate disk
partitions and filesystems using the routines provided by the GNU
Parted library, you need to install this package.

%conf -p
autoreconf -fiv

%install -a
%{__rm} -rf %{buildroot}%{_infodir}/dir
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%doc README doc/API doc/FAT
%{_sbindir}/parted
%{_sbindir}/partprobe
%{_libdir}/libparted*.so.*
%{_mandir}/man8/parted.8.gz
%{_mandir}/man8/partprobe.8.gz
%{_infodir}/parted.info.gz

%files devel
%{_includedir}/parted
%{_libdir}/libparted*.so
%{_libdir}/pkgconfig/libparted*.pc

%changelog
%{?autochangelog}
