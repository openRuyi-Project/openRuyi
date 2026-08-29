# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name udev
%global full_version 0.9.3
%global pkgname udev-0.9

Name:           rust-udev-0.9
Version:        0.9.3
Release:        %autorelease
Summary:        Rust crate "udev"
License:        MIT
URL:            https://github.com/Smithay/udev-rs
#!RemoteAsset:  sha256:af4e37e9ea4401fc841ff54b9ddfc9be1079b1e89434c1a6a865dd68980f7e9f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(io-lifetimes-1/default) >= 1.0.3
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(libudev-sys-0.1/default) >= 0.1.4
Requires:       crate(pkg-config-0.3) >= 0.3.3
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/hwdb) = %{version}
Provides:       crate(%{pkgname}/send) = %{version}
Provides:       crate(%{pkgname}/sync) = %{version}

%description
Source code for takopackized Rust crate "udev"

%package     -n %{name}+mio06
Summary:        Libudev bindings for Rust - feature "mio06"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mio-0.6/default) >= 0.6.21
Provides:       crate(%{pkgname}/mio06) = %{version}

%description -n %{name}+mio06
This metapackage enables feature "mio06" for the Rust udev crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mio07
Summary:        Libudev bindings for Rust - feature "mio07"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mio-0.7/default) >= 0.7.0
Requires:       crate(mio-0.7/os-ext) >= 0.7.0
Provides:       crate(%{pkgname}/mio07) = %{version}

%description -n %{name}+mio07
This metapackage enables feature "mio07" for the Rust udev crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mio08
Summary:        Libudev bindings for Rust - feature "mio08"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mio-0.8/default) >= 0.8.0
Requires:       crate(mio-0.8/os-ext) >= 0.8.0
Provides:       crate(%{pkgname}/mio08) = %{version}

%description -n %{name}+mio08
This metapackage enables feature "mio08" for the Rust udev crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mio10
Summary:        Libudev bindings for Rust - feature "mio10" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mio-1/default) >= 1.0.0
Requires:       crate(mio-1/os-ext) >= 1.0.0
Provides:       crate(%{pkgname}/mio) = %{version}
Provides:       crate(%{pkgname}/mio10) = %{version}

%description -n %{name}+mio10
This metapackage enables feature "mio10" for the Rust udev crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "mio" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
