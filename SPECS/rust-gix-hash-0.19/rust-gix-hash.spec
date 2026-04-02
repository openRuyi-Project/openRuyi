# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-hash
%global full_version 0.19.0
%global pkgname gix-hash-0.19

Name:           rust-gix-hash-0.19
Version:        0.19.0
Release:        %autorelease
Summary:        Rust crate "gix-hash"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:251fad79796a731a2a7664d9ea95ee29a9e99474de2769e152238d4fdb69d50e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(faster-hex-0.10/std) >= 0.10.0
Requires:       crate(gix-features-0.43/default) >= 0.43.1
Requires:       crate(gix-features-0.43/progress) >= 0.43.1
Requires:       crate(sha1-checked-0.10) >= 0.10.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-hash"

%package     -n %{name}+document-features
Summary:        Borrowed and owned git hash digests used to identify git objects - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-hash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Borrowed and owned git hash digests used to identify git objects - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(faster-hex-0.10/serde) >= 0.10.0
Requires:       crate(faster-hex-0.10/std) >= 0.10.0
Requires:       crate(serde-1.0/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-hash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
