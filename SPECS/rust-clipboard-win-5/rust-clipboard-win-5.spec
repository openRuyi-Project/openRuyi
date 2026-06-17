# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clipboard-win
%global full_version 5.4.1
%global pkgname clipboard-win-5

Name:           rust-clipboard-win-5
Version:        5.4.1
Release:        %autorelease
Summary:        Rust crate "clipboard-win"
License:        BSL-1.0
URL:            https://github.com/DoumanAsh/clipboard-win
#!RemoteAsset:  sha256:bde03770d3df201d4fb868f2c9c59e66a3e4e2bd06692a0fe701e7103c7e84d4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(error-code-3/default) >= 3.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "clipboard-win"

%package     -n %{name}+std
Summary:        Provides simple way to interact with Windows clipboard - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(error-code-3/std) >= 3.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust clipboard-win crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows-win
Summary:        Provides simple way to interact with Windows clipboard - feature "windows-win" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-win-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/monitor) = %{version}
Provides:       crate(%{pkgname}/windows-win) = %{version}

%description -n %{name}+windows-win
This metapackage enables feature "windows-win" for the Rust clipboard-win crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "monitor" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
