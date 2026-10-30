# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test
# SQLite Autosetup rejects the default Autotools --docdir option.
%define buildsystem_autotools_conf() %configure %*

# These are for SQLite sources
%define year 2026
%define download_version 3540100
# Doc version might be different
%define doc_version 3540100

Name:           sqlite
Version:        3.54.1
Release:        %autorelease
Summary:        Library that implements an embeddable SQL database engine
License:        LicenseRef-openRuyi-Public-Domain
URL:            https://www.sqlite.org/
VCS:            git:https://github.com/sqlite/sqlite.git
#!RemoteAsset:  sha256:387e7f6cad4797b17848c07d453dc6606917bb356a6cfe5a3abafd38c240c71b
Source0:        https://www.sqlite.org/%{year}/sqlite-src-%{download_version}.zip
#!RemoteAsset:  sha256:e9f634ac28a4c7b48f5c389e4b08c039654ec1487512092b330ccfcfdc0816e0
Source1:        https://www.sqlite.org/%{year}/sqlite-doc-%{doc_version}.zip
BuildSystem:    autotools

# Backport the JSON tree root key fix; https://github.com/sqlite/sqlite/commit/2023a2b37593073de0e789455b6a362ceeecd1d1.
Patch1000:      1000-json-tree.patch
# Find the installed Lemon template; https://gitlab.archlinux.org/archlinux/packaging/packages/sqlite/-/blob/4a8c4319f91e02fb521e058858fedcfaa6ff8f1b/sqlite-lemon-system-template.patch.
Patch2000:      2000-sqlite-lemon-system-template.patch

BuildOption(prep):  -a 1
BuildOption(conf):  --disable-rpath
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-fts3
BuildOption(conf):  --enable-fts4
BuildOption(conf):  --enable-fts5
BuildOption(conf):  --enable-session
BuildOption(conf):  --enable-column-metadata
BuildOption(conf):  --enable-dbstat
BuildOption(conf):  --enable-rtree
BuildOption(conf):  --enable-geopoly
BuildOption(conf):  --soname=legacy
# Skip ASAN fuzz tests under the worker data limit; https://clang.llvm.org/docs/AddressSanitizer.html#limitations.
BuildOption(check):  TSTRNNR_OPTS=~fuzzcheck-asan

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  glibc-devel
BuildRequires:  tcl-devel
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  unzip

Provides:       %{name}3 = %{version}-%{release}
Obsoletes:      %{name}-analyzer < %{version}-%{release}

%description
SQLite is a C library that provides an embedded SQL database engine.
Each database is stored in a single file. No separate server is required.

This build includes FTS3, FTS4, FTS5, R*Tree, Geopoly, dbstat, session
changesets, and resumable bulk updates. It provides column metadata
and unlock notifications. Secure deletion is enabled by default.

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
Summary:        A parser generator

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
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tcl
This package contains the tcl modules for %{name}.

%conf -p
%set_build_flags
export BUILD_CFLAGS="$CFLAGS $LDFLAGS"
export TCLLIBDIR=%{tcl_archdir}/sqlite%{version}
export CPPFLAGS="$CPPFLAGS \
 -DSQLITE_ENABLE_UNLOCK_NOTIFY \
 -DSQLITE_ENABLE_FTS3_TOKENIZER=1 \
 -DSQLITE_ENABLE_FTS3_PARENTHESIS \
 -DSQLITE_SECURE_DELETE \
 -DSQLITE_ENABLE_STMTVTAB \
 -DSQLITE_ENABLE_STAT4 \
 -DSQLITE_MAX_VARIABLE_NUMBER=250000 \
 -DSQLITE_MAX_EXPR_DEPTH=10000 \
 -DSQLITE_ENABLE_RBU"

%build -a
%make_build sqldiff

%check -p
trap 'status=$?
    if [ "$status" -ne 0 ]; then
        tclsh test/testrunner.tcl errors --verbose || :
    fi
    exit "$status"
' EXIT

%install -a
# Install lemon
install -D -m0755 lemon $RPM_BUILD_ROOT/%{_bindir}/lemon
install -D -m0644 tool/lempar.c $RPM_BUILD_ROOT/%{_datadir}/lemon/lempar.c
# Install tcl
# Fix up permissions to enable dep extraction
install -d $RPM_BUILD_ROOT/%{tcl_archdir}
chmod 0755 $RPM_BUILD_ROOT/%{tcl_archdir}/sqlite%{version}/*.so
# Install sqldiff
install -D -m0755 sqldiff $RPM_BUILD_ROOT/%{_bindir}/sqldiff

%files
%license LICENSE.md
%{_bindir}/sqlite3
%{_bindir}/sqldiff
%{_mandir}/man?/*
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.0

%files devel
%doc README.md
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/sqlite3.pc

%files doc
%doc sqlite-doc-%{doc_version}/*
%license LICENSE.md

%files -n lemon
%license LICENSE.md
%{_bindir}/lemon
%{_datadir}/lemon

%files tcl
%{tcl_archdir}/*

%changelog
%autochangelog
