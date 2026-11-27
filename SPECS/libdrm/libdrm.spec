# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libdrm
Version:        2.4.134
Release:        %autorelease
License:        MIT
Summary:        Library for Direct Rendering Manager
URL:            https://dri.freedesktop.org
VCS:            git:https://gitlab.freedesktop.org/mesa/libdrm
#!RemoteAsset:  sha256:ac5e74d157830eb8bee44c6a6bf3ad49774ef0dd2a72bdad74a8f20308b52a95
Source0:        https://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dudev=true
BuildOption(conf):  -Dvalgrind=disabled
BuildOption(conf):  -Dman-pages=disabled
BuildOption(conf):  -Dtests=true
BuildOption(conf):  -Dcairo-tests=disabled

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  linux-headers
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atomic_ops)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(pciaccess)

%description
libdrm provides a user space library for accessing the DRM (Direct Rendering
Manager). It is a low-level library, typically used by graphics drivers such as
Mesa, X drivers, and libva.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       linux-headers

%description    devel
This package contains the header files and development libraries for libdrm.

%files
%{_libdir}/lib*.so.*
%dir %{_datadir}/libdrm
%{_datadir}/libdrm/*.ids

%files devel
%{_includedir}/*
%{_libdir}/libdrm.so
%{_libdir}/libdrm_*.so
%{_libdir}/pkgconfig/libdrm.pc
%{_libdir}/pkgconfig/libdrm_*.pc

%changelog
%autochangelog
