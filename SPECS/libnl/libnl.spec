# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond python   0

Name:           libnl
Version:        3.11.0
Release:        %autorelease
Summary:        A suite of libraries for interacting with Linux Netlink sockets
License:        LGPL-2.1-only
URL:            https://github.com/thom311/libnl
#!RemoteAsset
Source0:        https://github.com/thom311/libnl/archive/refs/tags/%{name}3_11_0.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  libtool
%if %{with python}
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools
BuildRequires:  swig
%endif

%description
The libnl suite is a collection of libraries providing APIs to the Netlink
protocol, which is the primary IPC mechanism for interacting with the Linux
kernel networking subsystems. This package contains all the runtime libraries.

%package        cli
Summary:        Command-line interface utilities for libnl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    cli
This package provides command-line utilities (like nl-link-list, nl-route-list)
and their specific support libraries for inspecting and manipulating Netlink
from the shell.

%if %{with python}
%package -n python-%{name}
Summary:        Python bindings for libnl
Provides:       python3-%{name} = %{version}-%{release}
%python_provide python3-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-%{name}
This package contains the Python bindings for the libnl3 library suite.
%endif

%package        devel
Summary:        Development files for the libnl library suite
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-cli%{?_isa} = %{version}-%{release}

%description    devel
This package provides all the header files, pkg-config files, and unversioned
libraries needed to develop applications that use the libnl suite.

%conf -p
autoreconf -fiv

%build -a
%if %{with python}
pushd python
%pyproject_wheel
popd
%endif

%install -a
%if %{with python}
pushd python
%pyproject_install
popd
%endif

%files
%license COPYING
# The main package owns all non-cli libraries.
%exclude %{_libdir}/libnl-cli-3.so.*
%{_libdir}/libnl-*.so.*

%files cli
%config(noreplace) %{_sysconfdir}/libnl/
%dir %{_libdir}/libnl/
%{_libdir}/libnl/cli
%{_libdir}/libnl-cli-3.so.*
%{_bindir}/*
%{_mandir}/man8/*

%if %{with python}
%files -n python-%{name}
%{python3_sitearch}/netlink/
%{python3_sitearch}/netlink-*.dist-info
%endif

%files devel
%{_includedir}/libnl3/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnl-3.0.pc
%{_libdir}/pkgconfig/libnl-cli-3.0.pc
%{_libdir}/pkgconfig/libnl-genl-3.0.pc
%{_libdir}/pkgconfig/libnl-idiag-3.0.pc
%{_libdir}/pkgconfig/libnl-nf-3.0.pc
%{_libdir}/pkgconfig/libnl-route-3.0.pc
%{_libdir}/pkgconfig/libnl-xfrm-3.0.pc

%changelog
%{?autochangelog}
