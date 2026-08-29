# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_complete_command
%global full_version 0.6.1
%global pkgname clap-complete-command-0.6

Name:           rust-clap-complete-command-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "clap_complete_command"
License:        MIT
URL:            https://github.com/nihaals/clap-complete-command
#!RemoteAsset:  sha256:da8e198c052315686d36371e8a3c5778b7852fc75cc313e4e11eeb7a644a1b62
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-4/default) >= 4.0.0
Requires:       crate(clap-complete-4/default) >= 4.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "clap_complete_command"

%package     -n %{name}+carapace
Summary:        Reduces boilerplate for adding a shell completion command to Clap - feature "carapace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(carapace-spec-clap-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/carapace) = %{version}

%description -n %{name}+carapace
This metapackage enables feature "carapace" for the Rust clap_complete_command crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fig
Summary:        Reduces boilerplate for adding a shell completion command to Clap - feature "fig"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-complete-fig-4/default) >= 4.0.0
Provides:       crate(%{pkgname}/fig) = %{version}

%description -n %{name}+fig
This metapackage enables feature "fig" for the Rust clap_complete_command crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nushell
Summary:        Reduces boilerplate for adding a shell completion command to Clap - feature "nushell" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-complete-nushell-4/default) >= 4.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nushell) = %{version}

%description -n %{name}+nushell
This metapackage enables feature "nushell" for the Rust clap_complete_command crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
