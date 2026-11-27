# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sysbench
Version:        1.0.20
Release:        %autorelease
Summary:        System performance benchmark
License:        GPL-2.0-or-later
URL:            https://github.com/akopytov/sysbench
#!RemoteAsset:  sha256:e8ee79b1f399b2d167e6a90de52ccc90e52408f7ade1b9b7135727efe181347f
Source0:        https://github.com/akopytov/sysbench/archive/refs/tags/1.0.20.tar.gz
BuildSystem:    autotools

# use python3 to test.
Patch0:         0001-tests-use-python3.patch
# use grep -E rathan than egrep
Patch1:         0002-not-use-egrep.patch

BuildOption(conf):  --with-system-ck
BuildOption(conf):  --with-system-luajit
BuildOption(conf):  --without-gcc-arch
BuildOption(conf):  --with-mysql
BuildOption(conf):  --without-pgsql

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ck)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(libaio)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  libxslt
BuildRequires:  docbook-xsl
BuildRequires:  python3
BuildRequires:  python3dist(cram)

%description
SysBench is a modular, cross-platform and multi-threaded benchmark tool.

%package        tests
Summary:        Cram self-tests and helper scripts for sysbench
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python-cram
Requires:       python-unversioned-command

%description    tests
Cram cases, shell helpers and Lua test inputs for testing sysbench itself.
Database-dependent cases require configured MySQL or PostgreSQL test
instances and credentials. Tests must run from a writable copy of the
installed test directory. This is not the production benchmark suite.

%prep -a
rm -r third_party/luajit/luajit/
rm -r third_party/concurrency_kit/ck/
rm -r third_party/cram/

%conf -p
autoreconf -vif

%files
%exclude %{_datadir}/sysbench/tests/
%license COPYING
%doc ChangeLog README.md manual.html
%{_bindir}/*
%{_datadir}/sysbench/

%files tests
%{_datadir}/sysbench/tests/

%changelog
%autochangelog
