# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name botan
%global full_version 0.10.7
%global pkgname botan-0.10

Name:           rust-botan-0.10
Version:        0.10.7
Release:        %autorelease
Summary:        Rust crate "botan"
License:        MIT
URL:            https://botan.randombit.net/
#!RemoteAsset:  sha256:350081af1a3c6883f8a1f863ac553bfe6922589aad60008a70947765ed57c53e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(botan-sys-0.10/default) >= 0.10.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "botan"

%package     -n %{name}+botan3
Summary:        Rust wrapper for Botan cryptography library - feature "botan3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(botan-sys-0.10/botan3) >= 0.10.5
Provides:       crate(%{pkgname}/botan3) = %{version}

%description -n %{name}+botan3
This metapackage enables feature "botan3" for the Rust botan crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-std
Summary:        Rust wrapper for Botan cryptography library - feature "no-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(botan-sys-0.10/no-std) >= 0.10.5
Provides:       crate(%{pkgname}/no-std) = %{version}

%description -n %{name}+no-std
This metapackage enables feature "no-std" for the Rust botan crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored
Summary:        Rust wrapper for Botan cryptography library - feature "vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(botan-sys-0.10/vendored) >= 0.10.5
Provides:       crate(%{pkgname}/vendored) = %{version}

%description -n %{name}+vendored
This metapackage enables feature "vendored" for the Rust botan crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
