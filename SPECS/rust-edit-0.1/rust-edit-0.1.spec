# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name edit
%global full_version 0.1.5
%global pkgname edit-0.1

Name:           rust-edit-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "edit"
License:        CC0-1.0
URL:            https://github.com/milkey-mouse/edit
#!RemoteAsset:  sha256:f364860e764787163c8c8f58231003839be31276e821e2ad2092ddf496b1aa09
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(tempfile-3/default) >= 3.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "edit"

%package     -n %{name}+shell-words
Summary:        Open a file in the default text editor - feature "shell-words" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(shell-words-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/quoted-env) = %{version}
Provides:       crate(%{pkgname}/shell-words) = %{version}

%description -n %{name}+shell-words
This metapackage enables feature "shell-words" for the Rust edit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "quoted-env" feature.

%package     -n %{name}+which
Summary:        Open a file in the default text editor - feature "which" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(which-4) >= 4.0.0
Provides:       crate(%{pkgname}/better-path) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/which) = %{version}

%description -n %{name}+which
This metapackage enables feature "which" for the Rust edit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "better-path", and "default" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
