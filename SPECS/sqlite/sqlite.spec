# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# These are for SQLite sources
%define year 2025
%define download_version 3500400
# Doc version might be different
%define doc_version 3500400

Name:           sqlite
Version:        3.50.4
Release:        %autorelease
Summary:        Library that implements an embeddable SQL database engine
License:        GPL-3.0-or-later
URL:            https://www.sqlite.org/
#!RemoteAsset
Source0:        http://www.sqlite.org/%{year}/%{name}-src-%{download_version}.zip
#!RemoteAsset
Source1:        http://www.sqlite.org/%{year}/%{name}-doc-%{doc_version}.zip
BuildSystem:    autotools

# Support system-wide template (located at /usr/share/lemon/lempar.c) in lemon.
Patch0:         0001-sqlite-lemon-system-template.patch
Patch1:         0002-add-missing-quote.patch

BuildOption(prep):  -a 1

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  glibc-devel
BuildRequires:  tcl-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  unzip

Provides:       %{name}3 = %{version}-%{release}

%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server. Version 2 and version 3 binaries
are named to permit each to be installed on a single host

SQLite is built with some non-default settings:
- Additional APIs for table's and query's metadata are enabled
  (SQLITE_ENABLE_COLUMN_METADATA)
- Directory syncs are disabled (SQLITE_DISABLE_DIRSYNC)
- `secure_delete` defaults to 'on', so deleted content is overwritten
  with zeros (SQLITE_SECURE_DELETE)
- `sqlite3_unlock_notify()` is enabled - this feature allows to register a
  callback that's invoked when lock is removed (SQLITE_ENABLE_UNLOCK_NOTIFY)
- `dbstat` virtual table with disk space usage is enabled
- `dbpage` virtual table providing direct access to underlying database file
  is enabled (SQLITE_ENABLE_DBPAGE_VTAB)
- Threadsafe mode is set to 1 - Serialized, so it is safe to use in a
  multithreaded environment (SQLITE_THREADSAFE=1)
- FTS3, FTS4 and FTS5 are enabled so versions 3 to 5 of the full-text search
  engine are available (SQLITE_ENABLE_FTS3, SQLITE_ENABLE_FTS4,
  SQLITE_ENABLE_FTS5)
- Pattern parser in FTS3 extension supports nested parenthesis and operators
  `AND`, `OR` (SQLITE_ENABLE_FTS3_PARENTHESIS)
- R*Tree index extension is enabled (SQLITE_ENABLE_RTREE)
- Extension loading is enabled
- Sessions (sqlite-session feature) is enabled
- Preupdate hook is enabled

It is also important to note that shell has some extensions as its dependencies,
so some extensions are enabled by default in SQLite shell, but not in the system
libraries. Only the aforementioned extensions are available in the libraries:
FTS3, FTS4, FTS5, R*Tree

%package        devel
Summary:        Development tools for the sqlite3 embeddable SQL database engine
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files and development documentation
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel.

%package        doc
Summary:        Documentation for sqlite
BuildArch:      noarch

%description    doc
This package contains most of the static HTML files that comprise the
www.sqlite.org website, including all of the SQL Syntax and the
C/C++ interface specs and other miscellaneous documentation.

%package     -n lemon
Summary: A parser generator

%description -n lemon
Lemon is an LALR(1) parser generator for C or C++. It does the same
job as bison and yacc. But lemon is not another bison or yacc
clone. It uses a different grammar syntax which is designed to reduce
the number of coding errors. Lemon also uses a more sophisticated
parsing engine that is faster than yacc and bison and which is both
reentrant and thread-safe. Furthermore, Lemon implements features
that can be used to eliminate resource leaks, making is suitable for
use in long-running programs such as graphical user interfaces or
embedded controllers.

%package        tcl
Summary:        Tcl module for the sqlite3 embeddable SQL database engine
Requires:       %{name} = %{version}-%{release}

%description    tcl
This package contains the tcl modules for %{name}.

%package        analyzer
Summary:        An analysis program for sqlite3 database files
Requires:       %{name} = %{version}-%{release}

%description    analyzer
This package contains the analysis program for %{name}.

%prep -a
# Remove backup-file
rm -f %{name}-doc-%{docver}/sqlite.css~ || :

%conf
# These are needed otherwise configure will fail
export CC=gcc
export CC_FOR_BUILD=gcc
export TCLLIBDIR=%{tcl_archdir}/sqlite%{version}
export CFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS \
        -DSQLITE_ENABLE_COLUMN_METADATA=1 \
        -DSQLITE_ENABLE_UNLOCK_NOTIFY \
        -DSQLITE_ENABLE_DBSTAT_VTAB=1 \
        -DSQLITE_ENABLE_FTS3_TOKENIZER=1 \
        -DSQLITE_ENABLE_FTS3_PARENTHESIS \
        -DSQLITE_SECURE_DELETE \
        -DSQLITE_ENABLE_STMTVTAB \
        -DSQLITE_ENABLE_STAT4 \
        -DSQLITE_MAX_VARIABLE_NUMBER=250000 \
        -DSQLITE_MAX_EXPR_DEPTH=10000 \
        -DSQLITE_ENABLE_MATH_FUNCTIONS"
# By default, we use disable-rpath, which will
# cause failure here, so we overwrite the conf here
%configure                      \
    --disable-silent-rules      \
    --disable-static            \
    --enable-fts3               \
    --enable-fts4               \
    --enable-fts5               \
    --enable-rtree              \
    --soname=legacy

%build -a
# We also need to build tcl & sqldiff
%make_build sqlite3_analyzer
%make_build sqldiff

%install -a
# Install lemon
install -D -m0644 sqlite3.1 $RPM_BUILD_ROOT/%{_mandir}/man1/sqlite3.1
install -D -m0755 lemon $RPM_BUILD_ROOT/%{_bindir}/lemon
install -D -m0644 tool/lempar.c $RPM_BUILD_ROOT/%{_datadir}/lemon/lempar.c
# Install tcl
# Fix up permissions to enable dep extraction
install -d $RPM_BUILD_ROOT/%{tcl_archdir}
chmod 0755 $RPM_BUILD_ROOT/%{tcl_archdir}/sqlite%{version}/*.so
# Install sqlite3_analyzer
install -D -m0755 sqlite3_analyzer $RPM_BUILD_ROOT/%{_bindir}/sqlite3_analyzer
# Install sqldiff
install -D -m0755 sqldiff $RPM_BUILD_ROOT/%{_bindir}/sqldiff

%files
%{_bindir}/sqlite3
%{_bindir}/sqldiff
%{_mandir}/man?/*
%{_libdir}/*.so.%{version}

%files devel
%doc README.md
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.so.0
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{name}-doc-%{doc_version}/*

%files -n lemon
%{_bindir}/lemon
%{_datadir}/lemon

%files tcl
%{tcl_archdir}/*

%files analyzer
%{_bindir}/sqlite3_analyzer

%changelog
%{?autochangelog}
