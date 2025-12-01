# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           btrfs-progs
Version:        6.17
Release:        %autorelease
Summary:        Userspace programs for btrfs
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://btrfs.wiki.kernel.org/index.php/Main_Page
#!RemoteAsset
Source:         https://www.kernel.org/pub/linux/kernel/people/kdave/btrfs-progs/btrfs-progs-v%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf): --disable-documentation
BuildOption(conf): CFLAGS="%{optflags} -fno-strict-aliasing"
BuildOption(conf): --with-crypto=libgcrypt

BuildOption(install): mandir=%{_mandir} bindir=%{_sbindir} libdir=%{_libdir} incdir=%{_includedir}

BuildRequires:  gcc autoconf automake make
BuildRequires:  pkgconfig(ext2fs) pkgconfig(libacl) lzo-devel
BuildRequires:  util-linux-devel pkgconfig(zlib) pkgconfig(libudev)
BuildRequires:  pkgconfig(libgcrypt) >= 1.8.0
BuildRequires:  pkgconfig(libzstd) >= 1.0.0
BuildRequires:  python3-devel >= 3.4
BuildRequires:  python3-setuptools python3-pip

%description
The btrfs-progs package provides userspace programs needed to create,
check, and manage btrfs filesystems.

%package -n     libbtrfs
Summary:        btrfs filesystem-specific runtime library
License:        GPL-2.0-only

%description -n libbtrfs
This package contains the main library used by btrfs programs.

%package -n     libbtrfsutil
Summary:        btrfs filesystem-specific runtime utility library
License:        LGPL-2.1-or-later

%description -n libbtrfsutil
This package contains an alternative utility library for btrfs programs.

%package        devel
Summary:        btrfs filesystem-specific libraries and headers
Requires:       btrfs-progs = %{version}
Requires:       libbtrfs = %{version}
Requires:       libbtrfsutil = %{version}

%description    devel
This package contains the libraries and header files needed to
develop btrfs filesystem-specific programs.

%package -n     python3-btrfsutil
Summary:        Python 3 bindings for libbtrfsutil
Requires:       libbtrfsutil = %{version}

%description -n python3-btrfsutil
This package contains Python 3 bindings to the libbtrfsutil library.

%conf -p
./autogen.sh

%build -a
cd libbtrfsutil/python
%pyproject_wheel

%install -a
install -Dpm0644 btrfs-completion %{buildroot}%{_datadir}/bash-completion/completions/btrfs
# Nuke the static lib
rm -v %{buildroot}%{_libdir}/*.a

cd libbtrfsutil/python
%pyproject_install
%pyproject_save_files -L btrfsutil

%files
%license COPYING
%{_sbindir}/btrfsck
%{_sbindir}/fsck.btrfs
%{_sbindir}/mkfs.btrfs
%{_sbindir}/btrfs-image
%{_sbindir}/btrfs-convert
%{_sbindir}/btrfs-select-super
%{_sbindir}/btrfstune
%{_sbindir}/btrfs
%{_sbindir}/btrfs-map-logical
%{_sbindir}/btrfs-find-root
%{_udevrulesdir}/64-btrfs-dm.rules
%{_udevrulesdir}/64-btrfs-zoned.rules
%{_datadir}/bash-completion/completions/btrfs

%files -n libbtrfs
%license COPYING
%{_libdir}/libbtrfs.so.0*

%files -n libbtrfsutil
%license libbtrfsutil/COPYING
%{_libdir}/libbtrfsutil.so.1*

%files devel
%{_includedir}/btrfs/
%{_includedir}/btrfsutil.h
%{_libdir}/libbtrfs.so
%{_libdir}/libbtrfsutil.so
%{_libdir}/pkgconfig/libbtrfsutil.pc

%files -n python3-btrfsutil -f %{pyproject_files}
%license libbtrfsutil/COPYING

%changelog
%{?autochangelog}
