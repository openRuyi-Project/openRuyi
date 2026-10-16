# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0


Name:           tdb
Version:        1.4.15
Release:        %autorelease
Summary:        A Trivial Database library
License:        LGPL-3.0-or-later
URL:            https://tdb.samba.org/
VCS:            git:https://git.samba.org/samba.git
#!RemoteAsset:  sha256:fba09d8df1f1b9072aeae8e78b2bd43c5afef20b2f6deefa633aa14a377a8dd2
Source:         https://samba.org/ftp/tdb/tdb-%{version}.tar.gz
BuildSystem:    waf

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --bundled-libraries=NONE
BuildOption(conf):  --builtin-libraries=replace
BuildOption(conf):  --without-gettext

BuildRequires:  libxslt
BuildRequires:  docbook-xsl
BuildRequires:  pkgconfig(python3)

%description
The Tdb library implements a trivial database that is used by Samba and
other projects. It is extremely fast and designed for concurrent access.

%package        tools
Summary:        Command-line tools for managing Tdb databases
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
This package contains tools to create, view, and manage Tdb database files,
such as tdbdump and tdbtool.

%package        devel
Summary:        Development files for the Tdb library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, pkg-config file, and development
documentation needed to build applications that use the Tdb library.

%package     -n python-tdb
Summary:        Python 3 bindings for the Tdb library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-tdb = %{version}-%{release}

%description -n python-tdb
Python bindings for libtdb


%files
%license LICENSE
%{_libdir}/libtdb.so.*

%files tools
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbtool
%{_bindir}/tdbrestore
%{_mandir}/man8/tdbbackup.8*
%{_mandir}/man8/tdbdump.8*
%{_mandir}/man8/tdbtool.8*
%{_mandir}/man8/tdbrestore.8*

%files devel
%doc docs/README
%{_includedir}/tdb.h
%{_libdir}/libtdb.so
%{_libdir}/pkgconfig/tdb.pc

%files -n python-tdb
%{python3_sitearch}/tdb.cpython*.so
%{python3_sitearch}/_tdb_text.py

%changelog
%autochangelog
