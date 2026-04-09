# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libyang
Version:        4.2.2
Release:        %autorelease
Summary:        YANG data modeling language library
License:        BSD-3-Clause
URL:            https://github.com/CESNET/libyang
#!RemoteAsset
Source:         https://github.com/CESNET/libyang/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_BUILD_TYPE:STRING=Release
BuildOption(conf):  -DENABLE_LYD_PRIV:BOOL=ON
BuildOption(conf):  -DGEN_LANGUAGE_BINDINGS:BOOL=ON
BuildOption(conf):  -DENABLE_VALGRIND_TESTS:BOOL=OFF
BuildOption(conf):  -DGEN_DOXYGEN_DOCS:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  swig
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(python3)
BuildRequires:  flex
BuildRequires:  bison

%description
Libyang is a YANG data modeling language parser and toolkit written (and
providing API) in C. This package contains the core C library and command-line
tools.

%package        devel
Summary:        Development files for libyang
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libpcre2-posix)

%description    devel
Headers, pkg-config, and other development files for the libyang library.
This package also contains the API documentation.

%files
%license LICENSE
%{_bindir}/yanglint
%{_bindir}/yangre
%{_mandir}/man1/yanglint.1.gz
%{_mandir}/man1/yangre.1.gz
%{_libdir}/libyang.so.*
%dir %{_datadir}/yang
%dir %{_datadir}/yang/modules
%dir %{_datadir}/yang/modules/libyang
%{_datadir}/yang/modules/libyang/*.yang

%files devel
%doc doc/
%{_libdir}/libyang.so
%{_libdir}/pkgconfig/libyang.pc
%dir %{_includedir}/libyang
%{_includedir}/libyang/*.h

%changelog
%autochangelog
