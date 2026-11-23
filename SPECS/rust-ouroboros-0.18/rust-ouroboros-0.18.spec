# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ouroboros
%global full_version 0.18.5
%global pkgname ouroboros-0.18

Name:           rust-ouroboros-0.18
Version:        0.18.5
Release:        %autorelease
Summary:        Rust crate "ouroboros"
License:        MIT OR Apache-2.0
URL:            https://github.com/someguynamedjosh/ouroboros
#!RemoteAsset:  sha256:1e0f050db9c44b97a94723127e6be766ac5c340c48f2c4bb3ffa11713744be59
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aliasable-0.1/default) >= 0.1.3
Requires:       crate(ouroboros-macro-0.18/default) >= 0.18.5
Requires:       crate(static-assertions-1/default) >= 1.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ouroboros"

%package     -n %{name}+std
Summary:        Easy, safe self-referential struct generation - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ouroboros-macro-0.18/std) >= 0.18.5
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ouroboros crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
