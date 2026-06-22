# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name x11rb-protocol
%global full_version 0.13.2
%global pkgname x11rb-protocol-0.13

Name:           rust-x11rb-protocol-0.13
Version:        0.13.2
Release:        %autorelease
Summary:        Rust crate "x11rb-protocol"
License:        MIT OR Apache-2.0
URL:            https://github.com/psychon/x11rb
#!RemoteAsset:  sha256:ea6fc2961e4ef194dcbfe56bb845534d0dc8098940c7e5c012a258bfec6701bd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/dbe) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dpms) = %{version}
Provides:       crate(%{pkgname}/dri2) = %{version}
Provides:       crate(%{pkgname}/dri3) = %{version}
Provides:       crate(%{pkgname}/extra-traits) = %{version}
Provides:       crate(%{pkgname}/glx) = %{version}
Provides:       crate(%{pkgname}/randr) = %{version}
Provides:       crate(%{pkgname}/record) = %{version}
Provides:       crate(%{pkgname}/render) = %{version}
Provides:       crate(%{pkgname}/request-parsing) = %{version}
Provides:       crate(%{pkgname}/res) = %{version}
Provides:       crate(%{pkgname}/resource-manager) = %{version}
Provides:       crate(%{pkgname}/screensaver) = %{version}
Provides:       crate(%{pkgname}/shape) = %{version}
Provides:       crate(%{pkgname}/shm) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/sync) = %{version}
Provides:       crate(%{pkgname}/xevie) = %{version}
Provides:       crate(%{pkgname}/xf86dri) = %{version}
Provides:       crate(%{pkgname}/xf86vidmode) = %{version}
Provides:       crate(%{pkgname}/xinerama) = %{version}
Provides:       crate(%{pkgname}/xkb) = %{version}
Provides:       crate(%{pkgname}/xprint) = %{version}
Provides:       crate(%{pkgname}/xselinux) = %{version}
Provides:       crate(%{pkgname}/xtest) = %{version}
Provides:       crate(%{pkgname}/xv) = %{version}
Provides:       crate(%{pkgname}/xvmc) = %{version}

%description
Source code for takopackized Rust crate "x11rb-protocol"

%package     -n %{name}+all-extensions
Summary:        Rust bindings to X11 - feature "all-extensions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/composite) = %{version}
Requires:       crate(%{pkgname}/damage) = %{version}
Requires:       crate(%{pkgname}/dbe) = %{version}
Requires:       crate(%{pkgname}/dpms) = %{version}
Requires:       crate(%{pkgname}/dri2) = %{version}
Requires:       crate(%{pkgname}/dri3) = %{version}
Requires:       crate(%{pkgname}/glx) = %{version}
Requires:       crate(%{pkgname}/present) = %{version}
Requires:       crate(%{pkgname}/randr) = %{version}
Requires:       crate(%{pkgname}/record) = %{version}
Requires:       crate(%{pkgname}/render) = %{version}
Requires:       crate(%{pkgname}/res) = %{version}
Requires:       crate(%{pkgname}/screensaver) = %{version}
Requires:       crate(%{pkgname}/shape) = %{version}
Requires:       crate(%{pkgname}/shm) = %{version}
Requires:       crate(%{pkgname}/sync) = %{version}
Requires:       crate(%{pkgname}/xevie) = %{version}
Requires:       crate(%{pkgname}/xf86dri) = %{version}
Requires:       crate(%{pkgname}/xf86vidmode) = %{version}
Requires:       crate(%{pkgname}/xfixes) = %{version}
Requires:       crate(%{pkgname}/xinerama) = %{version}
Requires:       crate(%{pkgname}/xinput) = %{version}
Requires:       crate(%{pkgname}/xkb) = %{version}
Requires:       crate(%{pkgname}/xprint) = %{version}
Requires:       crate(%{pkgname}/xselinux) = %{version}
Requires:       crate(%{pkgname}/xtest) = %{version}
Requires:       crate(%{pkgname}/xv) = %{version}
Requires:       crate(%{pkgname}/xvmc) = %{version}
Provides:       crate(%{pkgname}/all-extensions) = %{version}

%description -n %{name}+all-extensions
This metapackage enables feature "all-extensions" for the Rust x11rb-protocol crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+present
Summary:        Rust bindings to X11 - feature "present"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dri3) = %{version}
Requires:       crate(%{pkgname}/randr) = %{version}
Requires:       crate(%{pkgname}/sync) = %{version}
Requires:       crate(%{pkgname}/xfixes) = %{version}
Provides:       crate(%{pkgname}/present) = %{version}

%description -n %{name}+present
This metapackage enables feature "present" for the Rust x11rb-protocol crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Rust bindings to X11 - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust x11rb-protocol crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xfixes
Summary:        Rust bindings to X11 - feature "xfixes" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/render) = %{version}
Requires:       crate(%{pkgname}/shape) = %{version}
Provides:       crate(%{pkgname}/composite) = %{version}
Provides:       crate(%{pkgname}/damage) = %{version}
Provides:       crate(%{pkgname}/xfixes) = %{version}
Provides:       crate(%{pkgname}/xinput) = %{version}

%description -n %{name}+xfixes
This metapackage enables feature "xfixes" for the Rust x11rb-protocol crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "composite", "damage", and "xinput" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
