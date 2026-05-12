# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name anstream
%global full_version 1.0.0
%global pkgname anstream-1.0

Name:           rust-anstream-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "anstream"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/anstyle.git
#!RemoteAsset:  sha256:824a212faf96e9acacdbd09febd34438f8f711fb84e09a8916013cd7815ca28d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1.0/default) >= 1.0.14
Requires:       crate(anstyle-parse-1.0/default) >= 1.0.0
Requires:       crate(colorchoice-1.0/default) >= 1.0.5
Requires:       crate(is-terminal-polyfill-1.0/default) >= 1.70.2
Requires:       crate(utf8parse-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/test)

%description
Source code for takopackized Rust crate "anstream"

%package     -n %{name}+auto
Summary:        IO stream adapters for writing colored text that will gracefully degrade according to your terminal's capabilities - feature "auto"
Requires:       crate(%{pkgname})
Requires:       crate(anstyle-query-1.0/default) >= 1.1.5
Provides:       crate(%{pkgname}/auto)

%description -n %{name}+auto
This metapackage enables feature "auto" for the Rust anstream crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        IO stream adapters for writing colored text that will gracefully degrade according to your terminal's capabilities - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/auto)
Requires:       crate(%{pkgname}/wincon)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust anstream crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wincon
Summary:        IO stream adapters for writing colored text that will gracefully degrade according to your terminal's capabilities - feature "wincon"
Requires:       crate(%{pkgname})
Requires:       crate(anstyle-wincon-3.0/default) >= 3.0.11
Provides:       crate(%{pkgname}/wincon)

%description -n %{name}+wincon
This metapackage enables feature "wincon" for the Rust anstream crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
