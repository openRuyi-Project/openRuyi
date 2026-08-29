# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           parted
Version:        3.7
Release:        %autorelease
Summary:        The GNU disk partition manipulation program
License:        GPLv3+
URL:            https://www.gnu.org/software/parted/
VCS:            git:https://https.git.savannah.gnu.org/git/parted.git
#!RemoteAsset:  sha256:008de57561a4f3c25a0648e66ed11e7b30be493889b64334a6d70f2c1951ef7b
Source0:        https://ftpmirror.gnu.org/gnu/parted/parted-%{version}.tar.xz
BuildSystem:    autotools

# skip some tests need superuser.
Patch2000:      2000-skip-some-tests.patch

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
# t4002-sun-badlabel test helper is a Python script
BuildRequires:  python3
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

%install -a
%{__rm} -rf %{buildroot}%{_infodir}/dir
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%doc README doc/FAT
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
