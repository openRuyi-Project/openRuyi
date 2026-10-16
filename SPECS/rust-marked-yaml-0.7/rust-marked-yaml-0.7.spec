# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name marked-yaml
%global full_version 0.7.2
%global pkgname marked-yaml-0.7

Name:           rust-marked-yaml-0.7
Version:        0.7.2
Release:        %autorelease
Summary:        Rust crate "marked-yaml"
License:        MIT
URL:            https://github.com/kinnison/marked-yaml/
#!RemoteAsset:  sha256:f2eb25a7ab146f4058d67a74dfea52e25c133c575f08ce5851da97d224e3ad8d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(doc-comment-0.3/default) >= 0.3.0
Requires:       crate(hashlink-0.9/default) >= 0.9.0
Requires:       crate(yaml-rust2-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "marked-yaml"

%package     -n %{name}+serde
Summary:        Simplified YAML structure with provenance spans - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.194
Requires:       crate(serde-1/derive) >= 1.0.194
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust marked-yaml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-path
Summary:        Simplified YAML structure with provenance spans - feature "serde-path"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(serde-path-to-error-0.1/default) >= 0.1.16
Provides:       crate(%{pkgname}/serde-path) = %{version}

%description -n %{name}+serde-path
This metapackage enables feature "serde-path" for the Rust marked-yaml crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
