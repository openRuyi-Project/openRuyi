# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond   gui_related_parts 1

Name:           unixODBC
Version:        2.3.14
Release:        %autorelease
Summary:        A complete ODBC driver manager for Linux
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.unixODBC.org/
VCS:            git:https://github.com/lurcher/unixODBC.git
#!RemoteAsset:  sha256:4e2814de3e01fc30b0b9f75e83bb5aba91ab0384ee951286504bb70205524771
Source0:        https://www.unixODBC.org/unixODBC-%{version}.tar.gz
Source1:        odbcinst.ini
BuildSystem:    autotools

BuildOption(conf):  --with-gnu-ld=yes
BuildOption(conf):  --enable-threads=yes
BuildOption(conf):  --enable-drivers=no
%if %{with gui_related_parts}
BuildOption(conf):  --enable-driver-config=yes
%else
BuildOption(conf):  --enable-driver-config=no
%endif

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(readline)

%description
Install unixODBC if you want to access databases through ODBC.
You will also need the mariadb-connector-odbc package for MySQL/MariaDB,
and/or the postgresql-odbc package for PostgreSQL.

%package        devel
Summary:        Development files for programs which will use the unixODBC library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries and header files needed to develop
applications that use the unixODBC driver manager.

%conf -p
autoreconf -fiv

%install -a
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/
mkdir -p %{buildroot}%{_libdir}/%{name}
find %{buildroot} -type f -name "*.a" -delete
rm -f %{buildroot}%{_libdir}/libltdl.*
rm -rf %{buildroot}%{_datadir}/libtool

%files
%license COPYING
%doc README AUTHORS ChangeLog
%if %{with gui_related_parts}
%doc doc
%endif
%config(noreplace) %{_sysconfdir}/odbc*
%{_bindir}/odbcinst
%{_bindir}/isql
%{_bindir}/dltest
%{_bindir}/iusql
%{_bindir}/odbc_config
%{_bindir}/slencheck
%{_mandir}/man*/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/odbc.pc
%{_libdir}/pkgconfig/odbccr.pc
%{_libdir}/pkgconfig/odbcinst.pc
%{_libdir}/*.so

%changelog
%autochangelog
