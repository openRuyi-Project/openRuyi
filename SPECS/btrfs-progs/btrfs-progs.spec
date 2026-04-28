# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           btrfs-progs
Version:        6.19.1
Release:        %autorelease
Summary:        Userspace programs for btrfs
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://btrfs.wiki.kernel.org/index.php/Main_Page
VCS:            git:https://github.com/kdave/btrfs-progs
#!RemoteAsset:  sha256:bb27e1ec54e7c3c0b7b2e596f853a73c07a3d72f21bc94042073c24dbf045796
Source:         https://www.kernel.org/pub/linux/kernel/people/kdave/btrfs-progs/btrfs-progs-v%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-documentation
BuildOption(conf):  CFLAGS="%{optflags} -fno-strict-aliasing"
BuildOption(conf):  --with-crypto=libgcrypt
BuildOption(install):  mandir=%{_mandir}
BuildOption(install):  bindir=%{_sbindir}
BuildOption(install):  libdir=%{_libdir}
BuildOption(install):  incdir=%{_includedir}

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  lzo-devel
BuildRequires:  util-linux-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libgcrypt) >= 1.8.0
BuildRequires:  pkgconfig(libzstd) >= 1.0.0
BuildRequires:  python3-devel >= 3.4
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

%description
The btrfs-progs package provides userspace programs needed to create,
check, and manage btrfs filesystems.

%package     -n libbtrfs
Summary:        btrfs filesystem-specific runtime library
License:        GPL-2.0-only

%description -n libbtrfs
This package contains the main library used by btrfs programs.

%package     -n libbtrfsutil
Summary:        btrfs filesystem-specific runtime utility library
License:        LGPL-2.1-or-later

%description -n libbtrfsutil
This package contains an alternative utility library for btrfs programs.

%package        devel
Summary:        btrfs filesystem-specific libraries and headers
Requires:       btrfs-progs%{?_isa} = %{version}-%{release}
Requires:       libbtrfs%{?_isa} = %{version}-%{release}
Requires:       libbtrfsutil%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries and header files needed to
develop btrfs filesystem-specific programs.

%package     -n python-btrfsutil
Summary:        Python bindings for libbtrfsutil
Requires:       libbtrfsutil%{?_isa} = %{version}-%{release}
Provides:       python3-btrfsutil
%python_provide python3-btrfsutil

%description -n python-btrfsutil
This package contains Python bindings to the libbtrfsutil library.

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

%files -n python-btrfsutil -f %{pyproject_files}
%license libbtrfsutil/COPYING

%changelog
%autochangelog
