# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-tempfile
%global full_version 18.0.0
%global pkgname gix-tempfile-18.0

Name:           rust-gix-tempfile-18.0
Version:        18.0.0
Release:        %autorelease
Summary:        Rust crate "gix-tempfile"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:666c0041bcdedf5fa05e9bef663c897debab24b7dc1741605742412d1d47da57
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gix-fs-0.16/default) >= 0.16.1
Requires:       crate(libc-0.2) >= 0.2.184
Requires:       crate(once-cell-1.0/race) >= 1.21.4
Requires:       crate(once-cell-1.0/std) >= 1.21.4
Requires:       crate(parking-lot-0.12/default) >= 0.12.5
Requires:       crate(tempfile-3.0/default) >= 3.27.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "gix-tempfile"

%package     -n %{name}+document-features
Summary:        Tempfile implementation with a global registry to assure cleanup - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-tempfile crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hp-hashmap
Summary:        Tempfile implementation with a global registry to assure cleanup - feature "hp-hashmap" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(dashmap-6.0/default) >= 6.1.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/hp-hashmap)

%description -n %{name}+hp-hashmap
This metapackage enables feature "hp-hashmap" for the Rust gix-tempfile crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+signals
Summary:        Tempfile implementation with a global registry to assure cleanup - feature "signals"
Requires:       crate(%{pkgname})
Requires:       crate(signal-hook-0.3) >= 0.3.18
Requires:       crate(signal-hook-registry-1.0/default) >= 1.4.5
Provides:       crate(%{pkgname}/signals)

%description -n %{name}+signals
This metapackage enables feature "signals" for the Rust gix-tempfile crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
