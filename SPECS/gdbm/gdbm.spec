# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define lname   libgdbm6
%define lcompat libgdbm_compat4
Name:           gdbm
Version:        1.26
Release:        %autorelease
Summary:        GNU dbm key/data database
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/gdbm/
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Patch1:         gdbm-no-build-date.patch
BuildRequires:  libtool
BuildRequires:  texinfo
BuildRequires:  readline-devel

BuildSystem: autotools
BuildOption(conf): --disable-static
BuildOption(conf): --disable-silent-rules
BuildOption(conf): --enable-libgdbm-compat
BuildOption(conf): --enable-nls
BuildOption(conf): --with-readline

%description
GNU dbm is a library of database functions that use extensible
hashing and work similar to the standard UNIX dbm. These routines are
provided to a programmer needing to create and manipulate a hashed
database.

The basic use of GDBM is to store key/data pairs in a data file. Each
key must be unique and each key is paired with only one data item.

The library provides primitives for storing key/data pairs, searching
and retrieving the data by its key and deleting a key along with its
data. It also supports sequential iteration over all key/data pairs in
a database.

%package -n %{lname}
Summary:        GNU dbm key/data database
# O/P added in 12.2
License:        GPL-3.0-or-later
Obsoletes:      gdbm < %{version}-%{release}
Provides:       gdbm = %{version}-%{release}
Provides:       %{name} = %{version}

%description -n %{lname}
GNU dbm is a library of database functions that use extensible
hashing and work similar to the standard UNIX dbm. These routines are
provided to a programmer needing to create and manipulate a hashed
database.

The basic use of GDBM is to store key/data pairs in a data file. Each
key must be unique and each key is paired with only one data item.

The library provides primitives for storing key/data pairs, searching
and retrieving the data by its key and deleting a key along with its
data. It also supports sequential iteration over all key/data pairs in
a database.

%package -n %{lcompat}
Summary:        GNU dbm key/data database compat wrapper
# Was provided in older sonames
License:        GPL-3.0-or-later
Conflicts:      libgdbm4

%description -n %{lcompat}
GNU dbm is a library of database functions that use extensible
hashing and work similar to the standard UNIX dbm. These routines are
provided to a programmer needing to create and manipulate a hashed
database.

This library is providing compatibility wrappers.

%package devel
Summary:        Development files for the dbm key/data database library
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Requires:       %{lcompat} = %{version}
Requires:       %{lname} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%check
%make_build check

%install -a
echo "/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
GROUP ( %{_libdir}/libgdbm.so %{_libdir}/libgdbm_compat.so )" > %{buildroot}/%{_libdir}/libndbm.so
%find_lang %{name} --generate-subpackages

%files -n %{lname}
%license COPYING
%{_libdir}/libgdbm.so.*

%files -n %{lcompat}
%license COPYING
%{_libdir}/libgdbm_compat.so.*

%files devel
%doc README NEWS
%{_bindir}/*
%{_includedir}/dbm.h
%{_includedir}/gdbm.h
%{_includedir}/ndbm.h
%{_infodir}/gdbm.info%{?ext_info}
%{_libdir}/libgdbm.so
%{_libdir}/libgdbm_compat.so
%{_libdir}/libndbm.so
%{_mandir}/man1/*%{ext_man}
%{_mandir}/man3/gdbm.3%{?ext_man}

%changelog
%{?autochangelog}
