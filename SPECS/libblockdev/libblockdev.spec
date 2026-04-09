# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond gtk_doc 0

Name:           libblockdev
Version:        3.4.0
Release:        %autorelease
Summary:        A library for low-level manipulation with block devices
License:        LGPL-2.1-or-later
URL:            https://github.com/storaged-project/libblockdev
#!RemoteAsset
Source0:        https://github.com/storaged-project/libblockdev/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-python3
BuildOption(conf):  --enable-introspection
BuildOption(conf):  --with-btrfs
BuildOption(conf):  --with-crypto
BuildOption(conf):  --with-dm
BuildOption(conf):  --with-loop
BuildOption(conf):  --with-lvm
BuildOption(conf):  --with-lvm_dbus
BuildOption(conf):  --with-mdraid
BuildOption(conf):  --with-mpath
BuildOption(conf):  --with-swap
BuildOption(conf):  --with-part
BuildOption(conf):  --with-fs
BuildOption(conf):  --with-tools
BuildOption(conf):  --with-nvme
BuildOption(conf):  --with-smart
BuildOption(conf):  --with-smartmontools
BuildOption(conf):  --with-nvdimm
BuildOption(conf):  --with-escrow
%if %{with gtk_doc}
BuildOption(conf):  --enable-gtk-doc
%else
BuildOption(conf):  --disable-gtk-doc
%endif

BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(e2p)
BuildRequires:  pkgconfig(bytesize)
BuildRequires:  pkgconfig(libparted)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libcryptsetup)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  e2fsprogs
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(libnvme)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(fdisk)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libatasmart)
BuildRequires:  pkgconfig(libndctl)
BuildRequires:  volume_key-devel
BuildRequires:  pkgconfig(nss)
%if %{with gtk_doc}
BuildRequires:  gtk-doc
%endif

%description
The libblockdev is a C library for doing low-level operations with block devices.

%package        devel
Summary:        Development files for libblockdev
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(glib-2.0)

%description    devel
Development files for libblockdev.

%package     -n python-blockdev
Summary:        Python3 bindings for libblockdev
Requires:       %{name} = %{version}-%{release}
Provides:       python3-blockdev
%python_provide python3-blockdev

%description -n python-blockdev
Python3 bindings for libblockdev.

%conf -p
./autogen.sh

%files
%license LICENSE
%{_libdir}/libblockdev.so.*
%{_libdir}/girepository*/BlockDev*.typelib
%dir %{_sysconfdir}/libblockdev
%dir %{_sysconfdir}/libblockdev/3/conf.d
%config %{_sysconfdir}/libblockdev/3/conf.d/00-default.cfg
%{_libdir}/libbd_utils.so.*
%{_libdir}/libbd_btrfs.so.*
%{_libdir}/libbd_crypto.so.*
%{_libdir}/libbd_dm.so.*
%{_libdir}/libbd_fs.so.*
%{_libdir}/libbd_loop.so.*
%{_libdir}/libbd_lvm.so.*
%{_libdir}/libbd_lvm-dbus.so.*
%config %{_sysconfdir}/libblockdev/3/conf.d/10-lvm-dbus.cfg
%{_libdir}/libbd_mdraid.so.*
%{_libdir}/libbd_swap.so.*
%{_libdir}/libbd_smart.so.*
%{_libdir}/libbd_part.so.*
%{_libdir}/libbd_mpath.so.*
%{_libdir}/libbd_nvdimm.so.*
%{_libdir}/libbd_nvme.so.*
%{_libdir}/libbd_smartmontools.so.*
%{_bindir}/lvm-cache-stats
%{_bindir}/vfat-resize

%files devel
%{_libdir}/libblockdev.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/blockdev.h
%{_includedir}/blockdev/plugins.h
%{_libdir}/pkgconfig/blockdev.pc
%{_datadir}/gir*/BlockDev*.gir
%if %{with gtk_doc}
%{_datadir}/gtk-doc/html/libblockdev
%endif
%{_libdir}/libbd_utils.so
%{_libdir}/pkgconfig/blockdev-utils.pc
%{_includedir}/blockdev/utils.h
%{_includedir}/blockdev/sizes.h
%{_includedir}/blockdev/exec.h
%{_includedir}/blockdev/extra_arg.h
%{_includedir}/blockdev/dev_utils.h
%{_includedir}/blockdev/module.h
%{_includedir}/blockdev/dbus.h
%{_includedir}/blockdev/logging.h
%{_libdir}/libbd_btrfs.so
%{_includedir}/blockdev/btrfs.h
%{_libdir}/libbd_crypto.so
%{_includedir}/blockdev/crypto.h
%{_libdir}/libbd_dm.so
%{_includedir}/blockdev/dm.h
%{_libdir}/libbd_fs.so
%dir %{_includedir}/blockdev/fs
%{_includedir}/blockdev/fs.h
%{_includedir}/blockdev/fs/*.h
%{_libdir}/libbd_loop.so
%{_includedir}/blockdev/loop.h
%{_libdir}/libbd_lvm.so
%{_libdir}/libbd_lvm-dbus.so
%{_includedir}/blockdev/lvm.h
%{_libdir}/libbd_mdraid.so
%{_includedir}/blockdev/mdraid.h
%{_libdir}/libbd_mpath.so
%{_includedir}/blockdev/mpath.h
%{_libdir}/libbd_nvdimm.so
%{_includedir}/blockdev/nvdimm.h
%{_libdir}/libbd_nvme.so
%{_includedir}/blockdev/nvme.h
%{_libdir}/libbd_part.so
%{_includedir}/blockdev/part.h
%{_libdir}/libbd_smart.so
%{_libdir}/libbd_smartmontools.so
%{_includedir}/blockdev/smart.h
%{_libdir}/libbd_swap.so
%{_includedir}/blockdev/swap.h

%files -n python-blockdev
%{python3_sitearch}/gi/overrides/BlockDev*

%changelog
%autochangelog
