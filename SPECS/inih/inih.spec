# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           inih
Version:        61
Release:        %autorelease
Summary:        Simple INI file parser library
License:        BSD-3-Clause
URL:            https://github.com/benhoyt/inih
#!RemoteAsset
Source0:        https://github.com/benhoyt/inih/archive/refs/tags/r%{version}.tar.gz#/%{name}-r%{version}.tar.gz

BuildSystem:    meson
BuildOption:    -Ddefault_library=shared
BuildOption:    -Ddistro_install=true

BuildRequires:  gcc
BuildRequires:  meson

%description
The inih package provides a simple INI file parser which is only a couple
of pages of code. It was designed to be small and simple, so it's good for
embedded systems. This package contains the runtime shared libraries.

%package devel
Summary:        Development files for the inih library
Requires:       %{name} = %{version}

%description devel
This package contains header files, pkg-config files, and development
symlinks for the inih library.

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/ini.h
%{_includedir}/INIReader.h
%{_libdir}/lib%{name}.so
%{_libdir}/libINIReader.so
%{_libdir}/pkgconfig/inih.pc
%{_libdir}/pkgconfig/INIReader.pc

%changelog
%{?autochangelog}
