# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wtmpdb
Version:        0.74.0
Release:        %autorelease
Summary:        Database for recording the last logged in users and system reboots
License:        BSD-2-Clause
URL:            https://github.com/thkukuk/wtmpdb
#!RemoteAsset
Source:         https://github.com/thkukuk/wtmpdb/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildSystem:    meson
BuildOption(conf): -Dman=enabled
BuildOption(conf): -Dcompat-symlink=true
BuildOption(conf): -Dwtmpdbd=enabled
BuildOption(check): --no-rebuild

BuildRequires:  docbook-xsl
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  /usr/bin/xsltproc

Provides:       util-linux:/usr/bin/last

%description
pam_wtmpdb and wtmpdb are Y2038-safe versions of wtmp and the last
utility. pam_wtmpdb collects all data in a sqlite3 database and the
wtmpdb utility creates boot and shutdown entries or formats and
prints the contents of the wtmp database.

%package devel
Summary:        Development files for libwtmpdb
Requires:       %{name} = %{version}

%description devel
This package contains all necessary include files and libraries
needed to develop applications that needs to read, write or modify
the wtmpdb database.

%install -a
mkdir -p %{buildroot}%{_mandir}/man1
ln -sf ../man8/wtmpdb.8 %{buildroot}%{_mandir}/man1/last.1

%preun
%systemd_preun wtmpdb-update-boot.service wtmpdb-rotate.timer wtmpdbd.socket

%post
%tmpfiles_create_package %{name} %{_tmpfilesdir}/wtmpdb.conf
%systemd_post wtmpdb-update-boot.service wtmpdb-rotate.timer wtmpdbd.socket

%postun
%systemd_postun wtmpdb-update-boot.service wtmpdb-rotate.timer wtmpdbd.socket

%files
%license LICENSE
%{_bindir}/last
%{_bindir}/wtmpdb
%{_libexecdir}/wtmpdbd
%{_unitdir}/wtmpdb-update-boot.service
%{_unitdir}/wtmpdb-rotate.service
%{_unitdir}/wtmpdb-rotate.timer
%{_unitdir}/wtmpdbd.service
%{_unitdir}/wtmpdbd.socket
%{_tmpfilesdir}/wtmpdb.conf
%{_pam_moduledir}/pam_wtmpdb.so
%{_libdir}/libwtmpdb.so.*
%ghost %{_localstatedir}/lib/wtmpdb
%{_mandir}/man1/last.1*
%{_mandir}/man8/wtmpdb.8*
%{_mandir}/man8/wtmpdbd.8*
%{_mandir}/man8/wtmpdbd.service.8*
%{_mandir}/man8/wtmpdbd.socket.8*
%{_mandir}/man8/pam_wtmpdb.8*

%files devel
%{_libdir}/libwtmpdb.so
%{_includedir}/wtmpdb.h
%{_libdir}/pkgconfig/libwtmpdb.pc

%changelog
%{?autochangelog}
