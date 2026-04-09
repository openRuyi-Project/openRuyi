# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libva
Version:        2.23.0
Release:        %autorelease
Summary:        Video Acceleration (VA) API for Linux
License:        MIT
URL:            https://github.com/intel/libva
#!RemoteAsset:  sha256:b10aceb30e93ddf13b2030eb70079574ba437be9b3b76065caf28a72c07e23e7
Source:         https://github.com/intel/libva/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)

%description
Libva is a library providing the VA API video acceleration API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%doc NEWS
%license COPYING
%ghost %{_sysconfdir}/libva.conf
%{_libdir}/libva.so.2*
%{_libdir}/libva-drm.so.2*
%{_libdir}/libva-wayland.so.2*
%{_libdir}/libva-x11.so.2*
%{_libdir}/libva-glx.so.2*

%files devel
%{_includedir}/va/
%{_libdir}/libva*.so
%{_libdir}/pkgconfig/libva*.pc

%changelog
%autochangelog
