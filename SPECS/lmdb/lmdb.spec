# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           lmdb
Version:        0.9.33
Release:        %autorelease
Summary:        Memory-mapped key-value database
License:        OLDAP-2.8
URL:            https://www.symas.com/lmdb
VCS:            git:https://git.openldap.org/openldap/openldap
#!RemoteAsset
Source0:        https://git.openldap.org/openldap/openldap/-/archive/LMDB_%{version}/openldap-LMDB_%{version}.tar.gz
Source1:        lmdb.pc.in
BuildSystem:    autotools

BuildOption(build): -C libraries/liblmdb SOVERSION=%{version} CFLAGS="%{optflags}"
BuildOption(install): -C libraries/liblmdb
BuildOption(install): SOVERSION=%{version} bindir=%{_bindir} libdir=%{_libdir}
BuildOption(install): mandir=%{_mandir} includedir=%{_includedir} datarootdir=%{_datadir}
BuildOption(check): -C libraries/liblmdb

# Build and link to shared library
Patch0:         0001-lmdb-make.patch

BuildRequires:  make

%description
LMDB is an ultra-fast, ultra-compact key-value embedded data
store developed by Symas for the OpenLDAP Project. By using memory-mapped files,
it provides the read performance of a pure in-memory database while still
offering the persistence of standard disk-based databases, and is only limited
to the size of the virtual address space.

%package        libs
Summary:        Shared libraries for %{name}

%description    libs
The %{name}-libs package contains shared libraries necessary for running
applications that use the %{name} embedded database.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n openldap-LMDB_%{version} -p1

%conf
# No conf

%install -a
# Install pkgconfig file
sed -e 's:@PREFIX@:%{_prefix}:g' \
    -e 's:@EXEC_PREFIX@:%{_exec_prefix}:g' \
    -e 's:@LIBDIR@:%{_libdir}:g' \
    -e 's:@INCLUDEDIR@:%{_includedir}:g' \
    -e 's:@PACKAGE_VERSION@:%{version}:g' \
    %{SOURCE1} >lmdb.pc
install -Dpm 0644 -t %{buildroot}%{_libdir}/pkgconfig lmdb.pc

# TODO: Fix tests
%check
:

%files
%doc libraries/liblmdb/COPYRIGHT
%doc libraries/liblmdb/CHANGES
%doc %{_mandir}/man1/*.1.gz
%license libraries/liblmdb/LICENSE
%{_bindir}/*

%files libs
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%{?autochangelog}
