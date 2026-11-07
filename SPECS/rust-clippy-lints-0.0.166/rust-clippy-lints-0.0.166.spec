# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clippy_lints
%global full_version 0.0.166
%global pkgname clippy-lints-0.0.166

Name:           rust-clippy-lints-0.0.166
Version:        0.0.166
Release:        %autorelease
Summary:        Rust crate "clippy_lints"
License:        MPL-2.0
URL:            https://github.com/rust-lang-nursery/rust-clippy
#!RemoteAsset:  sha256:cbde64e1942d299a8ebe242d54567654db22aa06bdaae7aa3eb392db275172e0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itertools-0.6/default) >= 0.6.0
Requires:       crate(lazy-static-0.2/default) >= 0.2.8
Requires:       crate(matches-0.1/default) >= 0.1.2
Requires:       crate(pulldown-cmark-0.0.15/default) >= 0.0.15
Requires:       crate(quine-mc-cluskey-0.2/default) >= 0.2.2
Requires:       crate(regex-syntax-0.4/default) >= 0.4.0
Requires:       crate(semver-0.6/default) >= 0.6.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-derive-1/default) >= 1.0.0
Requires:       crate(toml-0.4/default) >= 0.4.0
Requires:       crate(unicode-normalization-0.1/default) >= 0.1.0
Requires:       crate(url-1/default) >= 1.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debugging) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "clippy_lints"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
