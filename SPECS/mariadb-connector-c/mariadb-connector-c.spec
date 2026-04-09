# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mariadb-connector-c
Version:        3.4.8
Release:        %autorelease
Summary:        The MariaDB Native Client library (C driver)
License:        LGPL-2.1-or-later
URL:            http://mariadb.org/
VCS:            git:https://github.com/mariadb-corporation/mariadb-connector-c.git
#!RemoteAsset
Source0:        https://archive.mariadb.org/connector-c-%{version}/mariadb-connector-c-%{version}-src.tar.gz
#!RemoteAsset
Source1:        https://archive.mariadb.org/connector-c-%{version}/mariadb-connector-c-%{version}-src.tar.gz.asc
BuildSystem:    cmake

BuildOption(prep):  -n %{name}-%{version}-src -p1
BuildOption(conf):  -DCMAKE_COMPILE_WARNING_AS_ERROR=0
BuildOption(conf):  -DMARIADB_UNIX_ADDR=%{_sharedstatedir}/mysql/mysql.sock
BuildOption(conf):  -DMARIADB_PORT=3306
BuildOption(conf):  -DWITH_EXTERNAL_ZLIB=YES
BuildOption(conf):  -DWITH_SSL=openssl
BuildOption(conf):  -DWITH_MYSQLCOMPAT=ON
BuildOption(conf):  -DINSTALL_LAYOUT=RPM
BuildOption(conf):  -DCMAKE_INSTALL_PREFIX="%{_prefix}"
BuildOption(conf):  -DINSTALL_BINDIR="bin"
BuildOption(conf):  -DINSTALL_LIBDIR="%{_lib}"
BuildOption(conf):  -DINSTALL_INCLUDEDIR="include/mysql"
BuildOption(conf):  -DINSTALL_PLUGINDIR="%{_lib}/mariadb/plugin"
BuildOption(conf):  -DINSTALL_PCDIR="%{_lib}/pkgconfig"
BuildOption(conf):  -DWITH_UNITTEST=ON

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)

%description
The MariaDB Native Client library (C driver) is used to connect applications
developed in C/C++ to MariaDB and MySQL databases.

%package        devel
Summary:        Development files for mariadb-connector-c
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(zlib)

%description    devel
This package provides development files for mariadb-connector-c

%install -a
# Remove static linked libraries and symlinks to them
rm %{buildroot}%{_libdir}/lib*.a

ln -s mariadb_config %{buildroot}%{_bindir}/mysql_config
ln -s mariadb_version.h %{buildroot}%{_includedir}/mysql/mysql_version.h

%files
%doc README
%license COPYING.LIB
%{_libdir}/libmariadb.so.*
%dir %{_libdir}/mariadb
%dir %{_libdir}/mariadb/plugin
%{_libdir}/mariadb/plugin/*

%files devel
%{_bindir}/mariadb_config
%{_bindir}/mysql_config
%dir %{_includedir}/mysql
%{_includedir}/mysql/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmariadb.pc
%{_mandir}/man3/{mariadb,mysql}_*.3*

%changelog
%autochangelog
