# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libvdpau
Version:        1.5
Release:        %autorelease
Summary:        Wrapper library for the Video Decode and Presentation API
License:        MIT
URL:            https://gitlab.freedesktop.org/vdpau/libvdpau
#!RemoteAsset
Source:         https://gitlab.freedesktop.org/vdpau/libvdpau/-/archive/%{version}/libvdpau-%{version}.tar.bz2
BuildSystem:    meson

Patch0:         0001-libvdpau-av1-trace.patch

BuildOption(conf):  -Ddocumentation=false

BuildRequires:  meson >= 0.41
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)

%description
VDPAU is the Video Decode and Presentation API for UNIX. It provides an
interface to video decode acceleration and presentation hardware present in
modern GPUs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(x11)

%description    devel
This package contains libraries, header files, and documentation for
developing applications that use %{name}.

%files
%doc AUTHORS
%license COPYING
%config(noreplace) %{_sysconfdir}/vdpau_wrapper.cfg
%{_libdir}/libvdpau.so.*
%dir %{_libdir}/vdpau/
%{_libdir}/vdpau/libvdpau_trace.so*

%files devel
%{_includedir}/vdpau/
%{_libdir}/libvdpau.so
%{_libdir}/pkgconfig/vdpau.pc

%changelog
%autochangelog
