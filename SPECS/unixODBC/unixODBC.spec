# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond   gui_related_parts 1

Name:            unixODBC
Version:         2.3.14
Release:         %autorelease
Summary:         A complete ODBC driver manager for Linux
License:         GPL-2.0-or-later AND LGPL-2.1-or-later
URL:             http://www.unixODBC.org/
#!RemoteAsset
Source0:         http://www.unixODBC.org/unixODBC-%{version}.tar.gz
Source1:         odbcinst.ini
BuildSystem:     autotools

BuildOption(conf): --with-gnu-ld=yes
BuildOption(conf): --enable-threads=yes
BuildOption(conf): --enable-drivers=no
%if %{with gui_related_parts}
BuildOption(conf): --enable-driver-config=yes
%else
BuildOption(conf): --enable-driver-config=no
%endif

BuildRequires: make automake autoconf libtool libtool-ltdl-devel bison flex
BuildRequires: readline-devel

%description
Install unixODBC if you want to access databases through ODBC.
You will also need the mariadb-connector-odbc package for MySQL/MariaDB,
and/or the postgresql-odbc package for PostgreSQL.

%package      devel
Summary: Development files for programs which will use the unixODBC library
Requires:     %{name} = %{version}

%description  devel
This package contains the libraries and header files needed to develop
applications that use the unixODBC driver manager.

%conf -p
autoreconf -fiv

%install -a
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/
mkdir -p %{buildroot}%{_libdir}/%{name}
find %{buildroot} -type f -name "*.a" -delete
find %{buildroot} -type f -name "*.la" -delete
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
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
%{?autochangelog}
