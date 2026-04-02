# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-odb
%global full_version 0.70.0
%global pkgname gix-odb-0.70

Name:           rust-gix-odb-0.70
Version:        0.70.0
Release:        %autorelease
Summary:        Rust crate "gix-odb"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:9c9d7af10fda9df0bb4f7f9bd507963560b3c66cb15a5b825caf752e0eb109ac
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arc-swap-1.0/default) >= 1.9.0
Requires:       crate(gix-date-0.10/default) >= 0.10.7
Requires:       crate(gix-features-0.43/crc32) >= 0.43.1
Requires:       crate(gix-features-0.43/default) >= 0.43.1
Requires:       crate(gix-features-0.43/walkdir) >= 0.43.1
Requires:       crate(gix-features-0.43/zlib) >= 0.43.1
Requires:       crate(gix-fs-0.16/default) >= 0.16.1
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-hashtable-0.9/default) >= 0.9.0
Requires:       crate(gix-object-0.50/default) >= 0.50.2
Requires:       crate(gix-pack-0.60) >= 0.60.0
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-quote-0.6/default) >= 0.6.2
Requires:       crate(parking-lot-0.12/default) >= 0.12.5
Requires:       crate(tempfile-3.0/default) >= 3.27.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-odb"

%package     -n %{name}+document-features
Summary:        Implements various git object databases - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-odb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Implements various git object databases - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(gix-hash-0.19/serde) >= 0.19.0
Requires:       crate(gix-object-0.50/serde) >= 0.50.2
Requires:       crate(gix-pack-0.60/serde) >= 0.60.0
Requires:       crate(serde-1.0/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-odb crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
