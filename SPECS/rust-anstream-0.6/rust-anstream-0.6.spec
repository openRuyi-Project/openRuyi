# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name anstream
%global full_version 0.6.21
%global pkgname anstream-0.6

Name:           rust-anstream-0.6
Version:        0.6.21
Release:        %autorelease
Summary:        Rust crate "anstream"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/anstyle.git
#!RemoteAsset:  sha256:43d5b281e737544384e969a5ccad3f1cdd24b48086a0fc1b2a5262a26b8f4f4a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1/default) >= 1.0.0
Requires:       crate(anstyle-parse-0.2/default) >= 0.2.0
Requires:       crate(colorchoice-1/default) >= 1.0.0
Requires:       crate(is-terminal-polyfill-1/default) >= 1.48.0
Requires:       crate(utf8parse-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/test) = %{version}

%description
Source code for takopackized Rust crate "anstream"

%package     -n %{name}+auto
Summary:        IO stream adapters for writing colored text that will gracefully degrade according to your terminal's capabilities - feature "auto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstyle-query-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/auto) = %{version}

%description -n %{name}+auto
This metapackage enables feature "auto" for the Rust anstream crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        IO stream adapters for writing colored text that will gracefully degrade according to your terminal's capabilities - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/auto) = %{version}
Requires:       crate(%{pkgname}/wincon) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust anstream crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wincon
Summary:        IO stream adapters for writing colored text that will gracefully degrade according to your terminal's capabilities - feature "wincon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstyle-wincon-3/default) >= 3.0.5
Provides:       crate(%{pkgname}/wincon) = %{version}

%description -n %{name}+wincon
This metapackage enables feature "wincon" for the Rust anstream crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
