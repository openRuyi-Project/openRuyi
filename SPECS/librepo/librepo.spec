# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

# default use zchunk
%bcond zchunk 1

Name:           librepo
Version:        1.20.0
Release:        %autorelease
Summary:        Library for downloading repository metadata
License:        LGPL-2.0-or-later
URL:            https://github.com/rpm-software-management/librepo
#!RemoteAsset
Source:         %{url}/archive/%{version}/librepo-%{version}.tar.gz
BuildSystem:    cmake

# or,can't find glib.h
BuildOption(conf):  -DCMAKE_C_FLAGS="%{build_cflags} $(pkg-config --cflags glib-2.0)"
BuildOption(conf):  -DENABLE_PYTHON=OFF
BuildOption(conf):  -DENABLE_PYTHON_TESTS=OFF

%if %{with zchunk}
BuildOption(conf):  -DWITH_ZCHUNK=ON
%else
BuildOption(conf):  -DWITH_ZCHUNK=OFF
%endif

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  doxygen
# Tests
BuildRequires:  gnupg

%if %{with zchunk}
BuildRequires:  pkgconfig(zck)
%endif

%description
A library providing a C API for downloading repository metadata.

%package        devel
Summary:        Development files for librepo
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for librepo.

%build -p
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig:%{_datadir}/pkgconfig

%files
%license COPYING
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/librepo.pc
%{_includedir}/librepo/

%changelog
%{?autochangelog}
