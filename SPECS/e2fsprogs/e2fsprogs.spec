# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

# default without systemd
%bcond systemd 0

Name:           e2fsprogs
Version:        1.47.3
Release:        %autorelease
Summary:        Utilities for the Second Extended File System
License:        GPL-2.0-only
URL:            http://e2fsprogs.sourceforge.net
#!RemoteAsset
Source0:        http://www.kernel.org/pub/linux/kernel/people/tytso/e2fsprogs/v%{version}/e2fsprogs-%{version}.tar.xz
#!RemoteAsset
Source1:        https://thunk.org/tytso/tytso-key.asc#/%{name}.keyring
BuildSystem:    autotools

BuildOption(conf): --with-root-prefix=''
BuildOption(conf): --enable-elf-shlibs
BuildOption(conf): --disable-libblkid
BuildOption(conf): --disable-libuuid
BuildOption(conf): --disable-uuidd
BuildOption(conf): --disable-fsck
BuildOption(conf): --without-crond-dir

%if %{with systemd}
BuildOption(conf): --with-systemd-unit-dir=%{_unitdir}
%endif
BuildOption(build): CFLAGS="%{optflags}"

BuildRequires:  libarchive-devel util-linux-devel pkg-config xz texinfo
BuildRequires:  perl
%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%endif
Requires(post): /usr/bin/mkdir /usr/bin/touch
Requires:       libcom_err2
Requires:       libext2fs2
Suggests:       e2fsprogs-scrub

%description
Utilities needed to create and maintain ext2, ext3, and ext4 file systems.

%package -n e2fsprogs-scrub
Summary:        Ext2fs scrubbing scripts and service files
License:        GPL-2.0-only
%if %{with systemd}
%{?systemd_requires}
%endif
Requires:       e2fsprogs
Requires:       lvm2
Requires:       postfix
Requires:       util-linux

%description -n e2fsprogs-scrub
Scripts and systemd service files for background scrubbing of LVM volumes
with ext2, ext3, and ext4 filesystems.

%package -n libext2fs2
Summary:        Ext2fs library
License:        LGPL-2.0-only

%description -n libext2fs2
The basic Ext2fs shared library.

%package -n libext2fs-devel
Summary:        Development files for libext2fs
License:        LGPL-2.0-only
Requires:       libcom_err-devel
Requires:       libext2fs2 = %{version}

%description -n libext2fs-devel
Development files for libext2fs.

%package -n libcom_err2
Summary:        E2fsprogs error reporting library
License:        MIT

%description -n libcom_err2
com_err is an error message display library.

%package -n libcom_err-devel
Summary:        Development files for libcom_err
License:        MIT
Requires:       glibc-devel
Requires:       libcom_err2 = %{version}

%description -n libcom_err-devel
Development files for the com_err error message display library.

%build -a

# Guarantee that tranlations match the source messages
make -C po update-po

%install -a
find %{buildroot} -type f -name "*.a" -delete
rm -f %{buildroot}%{_libdir}/e2initrd_helper

%find_lang e2fsprogs

%if %{with systemd}
%pre -n e2fsprogs-scrub
%post -n e2fsprogs-scrub
%systemd_post e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%preun -n e2fsprogs-scrub
%systemd_preun e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%postun -n e2fsprogs-scrub
%systemd_postun e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%files -f e2fsprogs.lang
%doc doc/RelNotes/v%{version}.txt README
%license NOTICE
%config /etc/mke2fs.conf
%{_sbindir}/*
%{_bindir}/*
%{_infodir}/libext2fs.info.gz
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files -n e2fsprogs-scrub
%config /etc/e2scrub.conf
%{_sbindir}/e2scrub
%{_sbindir}/e2scrub_all
%if %{with systemd}
%{_libexecdir}/e2fsprogs/
%{_unitdir}/e2scrub@.service
%{_unitdir}/e2scrub_all.service
%{_unitdir}/e2scrub_all.timer
%{_unitdir}/e2scrub_fail@.service
%{_unitdir}/e2scrub_reap.service
%endif

%files -n libext2fs2
%{_libdir}/libext2fs.so.*
%{_libdir}/libe2p.so.*

%files -n libext2fs-devel
%{_libdir}/libext2fs.so
%{_libdir}/libe2p.so
/usr/include/ext2fs
/usr/include/e2p
%{_libdir}/pkgconfig/e2p.pc
%{_libdir}/pkgconfig/ext2fs.pc

%files -n libcom_err2
%{_libdir}/libcom_err.so.*
%{_libdir}/libss.so.*

%files -n libcom_err-devel
%{_bindir}/compile_et
%{_bindir}/mk_cmds
%{_libdir}/libcom_err.so
%{_libdir}/libss.so
%{_libdir}/pkgconfig/com_err.pc
%{_libdir}/pkgconfig/ss.pc
%{_includedir}/com_err.h
%{_includedir}/et
%{_includedir}/ss
%{_datadir}/et
%{_datadir}/ss
%{_mandir}/man1/compile_et.1.gz
%{_mandir}/man1/mk_cmds.1.gz
%{_mandir}/man3/com_err.3.gz

%changelog
%{?autochangelog}
