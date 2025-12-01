# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tdb
Version:        1.4.14
Release:        %autorelease
Summary:        A Trivial Database library
License:        LGPL-3.0-or-later
URL:            https://tdb.samba.org/
# No VCS link available
#!RemoteAsset
Source:         https://samba.org/ftp/tdb/tdb-%{version}.tar.gz

BuildSystem:    autotools

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --bundled-libraries=NONE
BuildOption(conf):  --builtin-libraries=replace
BuildOption(conf):  --without-gettext

BuildRequires:  python3-devel

%description
The Tdb library implements a trivial database that is used by Samba and
other projects. It is extremely fast and designed for concurrent access.

%package        tools
Summary:        Command-line tools for managing Tdb databases
Requires:       %{name} = %{version}

%description    tools
This package contains tools to create, view, and manage Tdb database files,
such as tdbdump and tdbtool.

%package        devel
Summary:        Development files for the Tdb library
Requires:       %{name} = %{version}
Requires:       tdb-tools = %{version}

%description    devel
This package contains the header files, pkg-config file, and development
documentation needed to build applications that use the Tdb library.

%package     -n python-tdb
Summary:        Python 3 bindings for the Tdb library
Requires:       %{name} = %{version}
Provides:       python3-tdb
%python_provide python3-tdb

%description -n python-tdb
Python bindings for libtdb

%conf -p
# https://gitlab.com/ita1024/waf/-/issues/2472
export PYTHONARCHDIR=%{python3_sitearch}

%files
%license LICENSE
%{_libdir}/libtdb.so.*

%files tools
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbtool
%{_bindir}/tdbrestore
# Man pages disabled due to docbook dependency issues

%files devel
%{_includedir}/tdb.h
%{_libdir}/libtdb.so
%{_libdir}/pkgconfig/tdb.pc

%files -n python-tdb
%{python3_sitearch}/tdb.cpython*.so
%{python3_sitearch}/_tdb_text.py

%changelog
%{?autochangelog}
