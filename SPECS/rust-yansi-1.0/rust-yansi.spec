# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yansi
%global full_version 1.0.1
%global pkgname yansi-1.0

Name:           rust-yansi-1.0
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "yansi"
License:        MIT OR Apache-2.0
URL:            https://github.com/SergioBenitez/yansi
#!RemoteAsset:  sha256:cfe53a6657fd280eaa890a3bc59152892ffa3e30101319d168b781ed6529b049
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/detect-env)
Provides:       crate(%{pkgname}/hyperlink)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "yansi"

%package     -n %{name}+detect-tty
Summary:        Dead simple ANSI terminal color painting library - feature "detect-tty"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/is-terminal)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/detect-tty)

%description -n %{name}+detect-tty
This metapackage enables feature "detect-tty" for the Rust yansi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+is-terminal
Summary:        Dead simple ANSI terminal color painting library - feature "is-terminal"
Requires:       crate(%{pkgname})
Requires:       crate(is-terminal-0.4/default) >= 0.4.11
Provides:       crate(%{pkgname}/is-terminal)

%description -n %{name}+is-terminal
This metapackage enables feature "is-terminal" for the Rust yansi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
