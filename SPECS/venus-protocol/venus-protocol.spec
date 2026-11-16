# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <zhengxingda@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           venus-protocol
Version:        1.1.3
Release:        %autorelease
Summary:        Protocol definition for Venus Vulkan command serialization
License:        MIT
URL:            https://gitlab.freedesktop.org/virgl/venus-protocol
VCS:            git:https://gitlab.freedesktop.org/virgl/venus-protocol
#!RemoteAsset:  git+https://gitlab.freedesktop.org/virgl/venus-protocol.git#v%{version}
#!CreateArchive
Source0:        venus-protocol-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  python3dist(mako)
BuildRequires:  pkg-config

%description
Venus is a protocol for passing Vulkan commands via Virtio-GPU interface.
This package contains the protocol definition and generated headers for Venus.

%install -a
# Move pkgconfig file to /usr/share for architecture-neutral headers
mkdir -p %{buildroot}%{_datarootdir}/pkgconfig
mv %{buildroot}%{_libdir}/pkgconfig/venus-protocol.pc %{buildroot}%{_datarootdir}/pkgconfig/

%files
%{_includedir}/venus-protocol/*
%{_datarootdir}/pkgconfig/venus-protocol.pc

%changelog
%autochangelog
