# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-tempfile
%global full_version 18.0.0
%global pkgname gix-tempfile-18

Name:           rust-gix-tempfile-18
Version:        18.0.0
Release:        %autorelease
Summary:        Rust crate "gix-tempfile"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:666c0041bcdedf5fa05e9bef663c897debab24b7dc1741605742412d1d47da57
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gix-fs-0.16/default) >= 0.16.0
Requires:       crate(libc-0.2) >= 0.2.174
Requires:       crate(once-cell-1/race) >= 1.21.3
Requires:       crate(once-cell-1/std) >= 1.21.3
Requires:       crate(parking-lot-0.12/default) >= 0.12.4
Requires:       crate(tempfile-3/default) >= 3.20.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "gix-tempfile"

%package     -n %{name}+document-features
Summary:        Tempfile implementation with a global registry to assure cleanup - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-tempfile crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hp-hashmap
Summary:        Tempfile implementation with a global registry to assure cleanup - feature "hp-hashmap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dashmap-6/default) >= 6.0.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/hp-hashmap) = %{version}

%description -n %{name}+hp-hashmap
This metapackage enables feature "hp-hashmap" for the Rust gix-tempfile crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+signals
Summary:        Tempfile implementation with a global registry to assure cleanup - feature "signals"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signal-hook-0.3) >= 0.3.18
Requires:       crate(signal-hook-registry-1/default) >= 1.4.5
Provides:       crate(%{pkgname}/signals) = %{version}

%description -n %{name}+signals
This metapackage enables feature "signals" for the Rust gix-tempfile crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
