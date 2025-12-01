# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libdrm
Version:        2.4.125
Release:        %autorelease
License:        MIT
Summary:        Library for Direct Rendering Manager
URL:            https://dri.freedesktop.org
#!RemoteAsset
Source0:        https://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.xz
Source1:        91-drm-modeset.rules
BuildSystem:    meson

BuildOption(conf): -Dudev=true
BuildOption(conf): -Dvalgrind=disabled
BuildOption(conf): -Dman-pages=disabled
BuildOption(conf): -Dtests=false
BuildOption(conf): -Dcairo-tests=disabled

BuildRequires:  meson gcc linux-headers pixman-devel
BuildRequires:  pkgconfig libatomic_ops-devel
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(pciaccess)

%description
libdrm provides a user space library for accessing the DRM (Direct Rendering
Manager). It is a low-level library, typically used by graphics drivers such as
Mesa, X drivers, and libva.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       linux-headers

%description      devel
This package contains the header files and development libraries for libdrm.

%install -a
install -D -m0644 -t %{buildroot}%{_udevrulesdir} %{SOURCE1}

%files
%{_libdir}/lib*.so.*
%{_udevrulesdir}/91-drm-modeset.rules
%dir %{_datadir}/libdrm
%{_datadir}/libdrm/*.ids

%files devel
%{_includedir}/*
%{_libdir}/libdrm.so
%{_libdir}/libdrm_*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%{?autochangelog}
