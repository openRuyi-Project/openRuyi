# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libxcvt
Version:        0.1.3
Release:        %autorelease
Summary:        VESA CVT standard timing modelines generator
License:        MIT AND HPND-sell-variant
URL:            https://gitlab.freedesktop.org/xorg/lib/libxcvt/
#!RemoteAsset
Source0:        https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc

%description
libxcvt is a library providing a standalone version of the X server
implementation of the VESA CVT standard timing modelines generator.
This package contains the shared library.

%package        devel
Summary:        Development package for libxcvt
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%doc COPYING
%{_libdir}/libxcvt.so.0*
%{_bindir}/cvt
%{_mandir}/man1/cvt.1*

%files devel
%{_libdir}/pkgconfig/libxcvt.pc
%{_includedir}/libxcvt/
%{_libdir}/libxcvt.so

%changelog
%autochangelog
