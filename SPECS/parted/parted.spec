# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           parted
Version:        3.6
Release:        %autorelease
Summary:        The GNU disk partition manipulation program
License:        GPLv3+
URL:            https://www.gnu.org/software/parted/
VCS:            git:https://https.git.savannah.gnu.org/git/parted.git
#!RemoteAsset:  sha256:3b43dbe33cca0f9a18601ebab56b7852b128ec1a3df3a9b30ccde5e73359e612
Source0:        https://ftpmirror.gnu.org/gnu/parted/parted-%{version}.tar.xz
BuildSystem:    autotools

Patch0:         0001-fix-do_version-parameters.patch
# skip some tests need superuser.
Patch1:         0002-skip-some-tests.patch

BuildOption(conf):  --enable-shared
BuildOption(conf):  --disable-device-mapper
BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(readline)
BuildRequires:  gettext-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  texinfo
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  util-linux-devel

%description
The GNU Parted program allows you to create, destroy, resize, move,
and copy hard disk partitions. Parted can be used for creating space
for new operating systems, reorganizing disk usage, and copying data
to new hard disks.

%package        devel
Summary:        Files for developing apps which will manipulate disk partitions
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
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
%{_libdir}/pkgconfig/libparted-fs-resize.pc
%{_libdir}/pkgconfig/libparted.pc

%changelog
%autochangelog
