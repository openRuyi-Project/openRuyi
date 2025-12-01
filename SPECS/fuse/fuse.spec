# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fuse
Version:        2.9.9
Release:        %autorelease
Summary:        Filesystem in Userspace (FUSE) utilities and libraries
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/libfuse/libfuse
#!RemoteAsset
Source0:        https://github.com/libfuse/libfuse/releases/download/fuse-%{version}/fuse-%{version}.tar.gz
Source1:        fuse.conf
Patch0:         0001-fuse-install-fix.patch
Patch1:         0002-fusermount-compile-as-pie.patch
Patch2:         0003-closefrom.patch
BuildSystem:    autotools

BuildOption(conf): --with-pkgconfigdir=%{_libdir}/pkgconfig
BuildOption(conf): --enable-lib
BuildOption(conf): --enable-util
BuildOption(conf): --enable-example

BuildOption(build): CFLAGS="%{optflags} -g -fno-strict-aliasing"

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires(pre):  group(trusted)
Requires:       util-linux >= 2.18
Supplements:    filesystem(fuse)

%description
FUSE (Filesystem in Userspace) is an interface by the Linux kernel
for userspace programs to export a filesystem to the kernel.
This package contains helper programs and runtime libraries for using FUSE mounts.

%package devel
Summary:        Development files for FUSE (userspace filesystem)
Requires:       %{name} = %{version}
Requires:       glibc-devel

%description devel
This package contains all include files, libraries, and configuration
files needed to develop programs that use the FUSE library.


%conf -p
export MOUNT_FUSE_PATH=%{_sbindir}
autoreconf -fi -I%{_datadir}/gettext/m4

%install -a
rm -rf %{buildroot}/%{_sysconfdir}/init.d
install -m644 -D %{SOURCE1} %{buildroot}/%{_sysconfdir}/fuse.conf
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}/%{_libdir}/libfuse.a
rm -f %{buildroot}/%{_libdir}/libulockmgr.a

(cd example && make clean)
rm -rf example/.deps example/Makefile.am example/Makefile.in
rm -rf doc/Makefile.am doc/Makefile.in doc/Makefile

%files
%license COPYING*
%doc AUTHORS ChangeLog NEWS README* example doc
%verify(not mode) %attr(4750,root,trusted) %{_bindir}/fusermount
%{_sbindir}/mount.fuse
%config %{_sysconfdir}/fuse.conf
%{_bindir}/ulockmgr_server
%{_mandir}/man1/fusermount.1%{?ext_man}
%{_mandir}/man1/ulockmgr_server.1%{?ext_man}
%{_mandir}/man8/mount.fuse.8%{?ext_man}
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/libfuse.so
%{_libdir}/libulockmgr.so
%{_includedir}/fuse.h
%{_includedir}/fuse
%{_libdir}/pkgconfig/*.pc
%{_includedir}/ulockmgr.h

%changelog
%{?autochangelog}
