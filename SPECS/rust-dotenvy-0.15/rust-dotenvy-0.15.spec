# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dotenvy
%global full_version 0.15.7
%global pkgname dotenvy-0.15

Name:           rust-dotenvy-0.15
Version:        0.15.7
Release:        %autorelease
Summary:        Rust crate "dotenvy"
License:        MIT
URL:            https://github.com/allan2/dotenvy
#!RemoteAsset:  sha256:1aaf95b3e5c8f23aa320147307562d361db0ae0d51242340f558153b4eb2439b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dotenvy"

%package     -n %{name}+clap
Summary:        Well-maintained fork of the dotenv crate - feature "clap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-3/default) >= 3.2.0
Provides:       crate(%{pkgname}/clap) = %{version}
Provides:       crate(%{pkgname}/cli) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust dotenvy crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "cli" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
