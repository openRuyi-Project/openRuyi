# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-packetline-blocking
%global full_version 0.19.3
%global pkgname gix-packetline-blocking-0.19

Name:           rust-gix-packetline-blocking-0.19
Version:        0.19.3
Release:        %autorelease
Summary:        Rust crate "gix-packetline-blocking"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:89c59c3ad41e68cb38547d849e9ef5ccfc0d00f282244ba1441ae856be54d001
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(faster-hex-0.10/std) >= 0.10.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/async-io)
Provides:       crate(%{pkgname}/blocking-io)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-packetline-blocking"

%package     -n %{name}+document-features
Summary:        Duplicate of `gix-packetline` with the `blocking-io` feature pre-selected - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-packetline-blocking crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Duplicate of `gix-packetline` with the `blocking-io` feature pre-selected - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(bstr-1.0/serde) >= 1.12.1
Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(faster-hex-0.10/serde) >= 0.10.0
Requires:       crate(faster-hex-0.10/std) >= 0.10.0
Requires:       crate(serde-1.0/derive) >= 1.0.114
Requires:       crate(serde-1.0/std) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-packetline-blocking crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
