# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wezterm-blob-leases
%global full_version 0.1.1
%global pkgname wezterm-blob-leases-0.1

Name:           rust-wezterm-blob-leases-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "wezterm-blob-leases"
License:        MIT
URL:            https://github.com/wezterm/wezterm
#!RemoteAsset:  sha256:692daff6d93d94e29e4114544ef6d5c942a7ed998b37abdc19b17136ea428eb7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getrandom-0.3/default) >= 0.3.1
Requires:       crate(mac-address-1/default) >= 1.1.8
Requires:       crate(sha2-0.10/default) >= 0.10.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(uuid-1/default) >= 1.13.0
Requires:       crate(uuid-1/rng) >= 1.13.0
Requires:       crate(uuid-1/v1) >= 1.13.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wezterm-blob-leases"

%package     -n %{name}+serde
Summary:        Manage image blob caching/leasing for wezterm - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(uuid-1/rng) >= 1.13.0
Requires:       crate(uuid-1/serde) >= 1.13.0
Requires:       crate(uuid-1/v1) >= 1.13.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wezterm-blob-leases crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simple-tempdir
Summary:        Manage image blob caching/leasing for wezterm - feature "simple_tempdir"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tempfile-3/default) >= 3.16.0
Provides:       crate(%{pkgname}/simple-tempdir) = %{version}

%description -n %{name}+simple-tempdir
This metapackage enables feature "simple_tempdir" for the Rust wezterm-blob-leases crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
