# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hdrhistogram
%global full_version 7.5.4
%global pkgname hdrhistogram-7

Name:           rust-hdrhistogram-7
Version:        7.5.4
Release:        %autorelease
Summary:        Rust crate "hdrhistogram"
License:        MIT OR Apache-2.0
URL:            https://github.com/HdrHistogram/HdrHistogram_rust
#!RemoteAsset:  sha256:765c9198f173dd59ce26ff9f95ef0aafd0a0fe01fb9d72841bc5066a4c06511d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.0.0
Requires:       crate(num-traits-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bench-private) = %{version}

%description
Source code for takopackized Rust crate "hdrhistogram"

%package     -n %{name}+base64
Summary:        Port of HdrHistogram to Rust - feature "base64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.21/default) >= 0.21.0
Provides:       crate(%{pkgname}/base64) = %{version}

%description -n %{name}+base64
This metapackage enables feature "base64" for the Rust hdrhistogram crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossbeam-channel
Summary:        Port of HdrHistogram to Rust - feature "crossbeam-channel" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/crossbeam-channel) = %{version}
Provides:       crate(%{pkgname}/sync) = %{version}

%description -n %{name}+crossbeam-channel
This metapackage enables feature "crossbeam-channel" for the Rust hdrhistogram crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "sync" feature.

%package     -n %{name}+default
Summary:        Port of HdrHistogram to Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serialization) = %{version}
Requires:       crate(%{pkgname}/sync) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust hdrhistogram crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flate2
Summary:        Port of HdrHistogram to Rust - feature "flate2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/default) >= 1.0.3
Provides:       crate(%{pkgname}/flate2) = %{version}

%description -n %{name}+flate2
This metapackage enables feature "flate2" for the Rust hdrhistogram crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nom
Summary:        Port of HdrHistogram to Rust - feature "nom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nom-7/default) >= 7.0.0
Provides:       crate(%{pkgname}/nom) = %{version}

%description -n %{name}+nom
This metapackage enables feature "nom" for the Rust hdrhistogram crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialization
Summary:        Port of HdrHistogram to Rust - feature "serialization"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Requires:       crate(%{pkgname}/flate2) = %{version}
Requires:       crate(%{pkgname}/nom) = %{version}
Provides:       crate(%{pkgname}/serialization) = %{version}

%description -n %{name}+serialization
This metapackage enables feature "serialization" for the Rust hdrhistogram crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
