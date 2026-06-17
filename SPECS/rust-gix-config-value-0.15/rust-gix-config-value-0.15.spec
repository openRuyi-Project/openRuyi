# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-config-value
%global full_version 0.15.3
%global pkgname gix-config-value-0.15

Name:           rust-gix-config-value-0.15
Version:        0.15.3
Release:        %autorelease
Summary:        Rust crate "gix-config-value"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:2c489abb061c74b0c3ad790e24a606ef968cebab48ec673d6a891ece7d5aef64
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(gix-path-0.10/default) >= 0.10.21
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(thiserror-2/default) >= 2.0.17
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-config-value"

%package     -n %{name}+document-features
Summary:        The gitoxide project providing git-config value parsing - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-config-value crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The gitoxide project providing git-config value parsing - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bstr-1/serde) >= 1.12.0
Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(serde-1/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-config-value crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
