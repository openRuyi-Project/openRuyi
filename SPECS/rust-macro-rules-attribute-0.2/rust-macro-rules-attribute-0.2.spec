# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name macro_rules_attribute
%global full_version 0.2.2
%global pkgname macro-rules-attribute-0.2

Name:           rust-macro-rules-attribute-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "macro_rules_attribute"
License:        Apache-2.0 OR MIT OR Zlib
URL:            https://crates.io/crates/macro_rules_attribute
#!RemoteAsset:  sha256:65049d7923698040cd0b1ddcced9b0eb14dd22c5f86ae59c3740eab64a676520
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(macro-rules-attribute-proc-macro-0.2/default) >= 0.2.2
Requires:       crate(paste-1/default) >= 1.0.7
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/better-docs) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "macro_rules_attribute"

%package     -n %{name}+verbose-expansions
Summary:        Use declarative macros in attribute or derive position - feature "verbose-expansions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(macro-rules-attribute-proc-macro-0.2/verbose-expansions) >= 0.2.2
Provides:       crate(%{pkgname}/verbose-expansions) = %{version}

%description -n %{name}+verbose-expansions
This metapackage enables feature "verbose-expansions" for the Rust macro_rules_attribute crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
