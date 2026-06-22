# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name orbclient
%global full_version 0.3.55
%global pkgname orbclient-0.3

Name:           rust-orbclient-0.3
Version:        0.3.55
Release:        %autorelease
Summary:        Rust crate "orbclient"
License:        MIT
URL:            https://gitlab.redox-os.org/redox-os/orbclient
#!RemoteAsset:  sha256:5df339f526ea9a60e371768d50efc2f2508c7203290731565d1f7a6f71d21747
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(libredox-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unifont) = %{version}

%description
Source code for takopackized Rust crate "orbclient"

%package     -n %{name}+bundled
Summary:        Orbital Client Library - feature "bundled"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sdl) = %{version}
Requires:       crate(sdl2-0.38/bundled) >= 0.38.0
Requires:       crate(sdl2-0.38/static-link) >= 0.38.0
Provides:       crate(%{pkgname}/bundled) = %{version}

%description -n %{name}+bundled
This metapackage enables feature "bundled" for the Rust orbclient crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Orbital Client Library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sdl) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/unifont) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust orbclient crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+image
Summary:        Orbital Client Library - feature "image"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(image-0.21/default) >= 0.21.0
Requires:       crate(resize-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/image) = %{version}

%description -n %{name}+image
This metapackage enables feature "image" for the Rust orbclient crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+raw-window-handle
Summary:        Orbital Client Library - feature "raw-window-handle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(raw-window-handle-0.5/default) >= 0.5.2
Provides:       crate(%{pkgname}/raw-window-handle) = %{version}

%description -n %{name}+raw-window-handle
This metapackage enables feature "raw-window-handle" for the Rust orbclient crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sdl
Summary:        Orbital Client Library - feature "sdl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sdl2-0.38/default) >= 0.38.0
Provides:       crate(%{pkgname}/sdl) = %{version}

%description -n %{name}+sdl
This metapackage enables feature "sdl" for the Rust orbclient crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
