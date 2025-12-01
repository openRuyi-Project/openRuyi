# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libeconf
Version:        0.7.8
Release:        %autorelease
Summary:        Enhanced config file parser library
License:        MIT
URL:            https://github.com/openSUSE/libeconf
#!RemoteAsset
Source:         https://github.com/openSUSE/libeconf/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Provides:       libeconf0
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pkgconfig

%description
Enhanced config file parser, which merges config files placed
in several locations into one. This package contains the runtime library.


%package        devel
Summary:        Development files for libeconf
Requires:       %{name} = %{version}

%description    devel
This package contains all necessary include files and libraries needed
to develop applications that use libeconf.

%package        static
Summary:        Static library for libeconf
Requires:       %{name}-devel = %{version}
Provides:       %{name}-devel-static = %{version}

%description    static
This package contains the libeconf.a static library.

%package        utils
Summary:        Command line interface for libeconf
Requires:       %{name} = %{version}

%description    utils
This package contains tools for handling configuration files.

%files
%license LICENSE
%{_libdir}/libeconf.so.0
%{_libdir}/libeconf.so.0.*

%files static
%{_libdir}/libeconf.a

%files devel
%{_includedir}/*.h
%{_libdir}/libeconf.so
%{_libdir}/pkgconfig/libeconf.pc
%{_mandir}/man3/*.3*

%files utils
%{_bindir}/econftool
%{_mandir}/man8/econftool.8*

%changelog
%{?autochangelog}
