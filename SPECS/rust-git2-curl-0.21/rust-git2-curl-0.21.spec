# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name git2-curl
%global full_version 0.21.0
%global pkgname git2-curl-0.21

Name:           rust-git2-curl-0.21
Version:        0.21.0
Release:        %autorelease
Summary:        Rust crate "git2-curl"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/git2-rs
#!RemoteAsset:  sha256:be8dcabbc09ece4d30a9aa983d5804203b7e2f8054a171f792deff59b56d31fa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(curl-0.4/default) >= 0.4.33
Requires:       crate(git2-0.20) >= 0.20.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(url-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Intended to be used with the git2 crate.
Source code for takopackized Rust crate "git2-curl"

%package     -n %{name}+zlib-ng-compat
Summary:        Backend for an HTTP transport in libgit2 powered by libcurl - feature "zlib-ng-compat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(curl-0.4/zlib-ng-compat) >= 0.4.33
Requires:       crate(git2-0.20/zlib-ng-compat) >= 0.20.0
Provides:       crate(%{pkgname}/zlib-ng-compat) = %{version}

%description -n %{name}+zlib-ng-compat
Intended to be used with the git2 crate.
This metapackage enables feature "zlib-ng-compat" for the Rust git2-curl crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
