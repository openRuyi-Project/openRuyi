# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libepoxy
Version:        1.5.10
Release:        %autorelease
Summary:        OpenGL function pointer management library
License:        MIT
URL:            https://github.com/anholt/libepoxy
#!RemoteAsset
Source:         https://github.com/anholt/libepoxy/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Ddocs=false
BuildOption(conf):  -Dglx=yes
BuildOption(conf):  -Degl=yes
BuildOption(conf):  -Dx11=true
BuildOption(conf):  -Dtests=false

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  python3

%description
Epoxy is a library for handling OpenGL function pointer management.
This package contains the shared libraries.

%package        devel
Summary:        Development files for libepoxy
Requires:       %{name}%{?_isa} = %{version}
Requires:       pkgconfig(egl)
Requires:       pkgconfig(x11)

%description    devel
This package contains the libraries and header files needed for
development with libepoxy.

%files
%license COPYING
%{_libdir}/libepoxy.so.0*

%files devel
%doc README.md
%{_libdir}/libepoxy.so
%{_libdir}/pkgconfig/epoxy.pc
%{_includedir}/epoxy/

%changelog
%{?autochangelog}
