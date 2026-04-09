# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           talloc
Version:        2.4.3
Release:        %autorelease
Summary:        A hierarchical memory allocator with destructors
License:        LGPL-3.0-or-later
URL:            https://talloc.samba.org/
VCS:            git:https://gitlab.com/samba-team/devel/samba.git
#!RemoteAsset
Source:         https://www.samba.org/ftp/talloc/talloc-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --disable-rpath-install
BuildOption(conf):  --bundled-libraries=NONE
BuildOption(conf):  --builtin-libraries=replace
BuildOption(conf):  --disable-silent-rules

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(python3)

%description
A library that implements a hierarchical, pool-based memory allocator with
destructors, which greatly simplifies memory management in complex C programs.

%package        devel
Summary:        Development files for the Talloc library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and development libraries needed to build applications that
link against the Talloc library.

%package     -n python-talloc
Summary:        Python bindings for the Talloc library
Provides:       python3-talloc = %{version}-%{release}
%python_provide python3-talloc
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-talloc
Python 3 bindings and libraries for using Talloc in Python applications.

%package     -n python3-talloc-devel
Summary:        Development files for python3-talloc
# I don't think we can use provides python3-xxx here - 251
Requires:       python3-talloc = %{version}-%{release}

%description -n python3-talloc-devel
Development files for the python3-talloc bindings.

%files
%license LICENSE
%{_libdir}/libtalloc.so.*

%files devel
%{_includedir}/talloc.h
%{_libdir}/libtalloc.so
%{_libdir}/pkgconfig/talloc.pc

%files -n python-talloc
%{_libdir}/libpytalloc-util.cpython*.so.*
%{python3_sitearch}/talloc.cpython*.so

%files -n python3-talloc-devel
%{_includedir}/pytalloc.h
%{_libdir}/pkgconfig/pytalloc-util.cpython-*.pc
%{_libdir}/libpytalloc-util.cpython*.so

%changelog
%autochangelog
