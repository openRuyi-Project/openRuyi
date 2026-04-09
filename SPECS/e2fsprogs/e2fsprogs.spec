# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
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

BuildOption(conf):  --with-root-prefix=''
BuildOption(conf):  --enable-elf-shlibs
BuildOption(conf):  --disable-libblkid
BuildOption(conf):  --disable-libuuid
BuildOption(conf):  --disable-uuidd
BuildOption(conf):  --disable-fsck
BuildOption(conf):  --without-crond-dir
%if %{with systemd}
BuildOption(conf):  --with-systemd-unit-dir=%{_unitdir}
%endif
BuildOption(build):  CFLAGS="%{optflags}"

BuildRequires:  libarchive-devel
BuildRequires:  util-linux-devel
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  texinfo
BuildRequires:  perl
%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%endif
Requires(post): /usr/bin/mkdir /usr/bin/touch
Suggests:       e2fsprogs-scrub

%description
Utilities needed to create and maintain ext2, ext3, and ext4 file systems.

%package     -n e2fsprogs-scrub
Summary:        Ext2fs scrubbing scripts and service files
License:        GPL-2.0-only
%if %{with systemd}
%{?systemd_requires}
%endif
Recommends:     /usr/sbin/sendmail
Requires:       e2fsprogs
Requires:       lvm2
Requires:       util-linux

%description -n e2fsprogs-scrub
Scripts and systemd service files for background scrubbing of LVM volumes
with ext2, ext3, and ext4 filesystems.

%package        devel
Summary:        Development files for e2fsprogs
License:        LGPL-2.0-only
Requires:       pkgconfig(com_err)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and libraries needed to develop
applications that use the e2fsprogs libraries.

It mainly includes the libext2fs development files.

%package        libs
Summary:        Ext2fs shared library
License:        LGPL-2.0-only

%description    libs
This package contains the shared libraries needed to run applications
that use the e2fsprogs libraries.

It mainly includes the basic Ext2fs shared library.

%package     -n libcom_err
Summary:        E2fsprogs error reporting library
License:        MIT

%description -n libcom_err
com_err is an error message display library.

%package     -n libcom_err-devel
Summary:        Development files for libcom_err
License:        MIT
Requires:       glibc-devel
Requires:       libcom_err%{?_isa} = %{version}-%{release}

%description -n libcom_err-devel
Development files for the com_err error message display library.

%build -a

# Guarantee that tranlations match the source messages
make -C po update-po

%install -a
find %{buildroot} -type f -name "*.a" -delete
rm -f %{buildroot}%{_libdir}/e2initrd_helper

%find_lang e2fsprogs --generate-subpackages

%if %{with systemd}
%pre -n e2fsprogs-scrub
%post -n e2fsprogs-scrub
%systemd_post e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%preun -n e2fsprogs-scrub
%systemd_preun e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%postun -n e2fsprogs-scrub
%systemd_postun e2scrub@.service e2scrub_all.service e2scrub_all.timer e2scrub_fail@.service e2scrub_reap.service
%endif

%files
%doc doc/RelNotes/v%{version}.txt README
%license NOTICE
%config /etc/mke2fs.conf
%{_bindir}/*
%{_infodir}/libext2fs.info.gz
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%exclude %{_bindir}/compile_et
%exclude %{_bindir}/mk_cmds
%exclude %{_bindir}/e2scrub
%exclude %{_bindir}/e2scrub_all

%files -n e2fsprogs-scrub
%config /etc/e2scrub.conf
%{_bindir}/e2scrub
%{_bindir}/e2scrub_all
%if %{with systemd}
%{_libexecdir}/e2fsprogs/
%{_unitdir}/e2scrub@.service
%{_unitdir}/e2scrub_all.service
%{_unitdir}/e2scrub_all.timer
%{_unitdir}/e2scrub_fail@.service
%{_unitdir}/e2scrub_reap.service
%endif

%files libs
%{_libdir}/libext2fs.so.*
%{_libdir}/libe2p.so.*

%files devel
%{_libdir}/libext2fs.so
%{_libdir}/libe2p.so
%{_includedir}/ext2fs
%{_includedir}/e2p
%{_libdir}/pkgconfig/e2p.pc
%{_libdir}/pkgconfig/ext2fs.pc

%files -n libcom_err
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
%autochangelog
