# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-commitgraph
%global full_version 0.29.0
%global pkgname gix-commitgraph-0.29

Name:           rust-gix-commitgraph-0.29
Version:        0.29.0
Release:        %autorelease
Summary:        Rust crate "gix-commitgraph"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:6bb23121e952f43a5b07e3e80890336cb847297467a410475036242732980d06
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-chunk-0.4/default) >= 0.4.12
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(memmap2-0.9/default) >= 0.9.10
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-commitgraph"

%package     -n %{name}+document-features
Summary:        Read-only access to the git commitgraph file format - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-commitgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Read-only access to the git commitgraph file format - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(bstr-1.0/serde) >= 1.12.1
Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(gix-hash-0.19/serde) >= 0.19.0
Requires:       crate(serde-1.0/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-commitgraph crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
