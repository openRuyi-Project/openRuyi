# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dialoguer
%global full_version 0.12.0
%global pkgname dialoguer-0.12

Name:           rust-dialoguer-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "dialoguer"
License:        MIT
URL:            https://github.com/console-rs/dialoguer
#!RemoteAsset:  sha256:25f104b501bf2364e78d0d3974cbc774f738f5865306ed128e1e0d7499c0ad96
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(console-0.16/default) >= 0.16.0
Requires:       crate(shell-words-1/default) >= 1.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/completion) = %{version}
Provides:       crate(%{pkgname}/history) = %{version}

%description
Source code for takopackized Rust crate "dialoguer"

%package     -n %{name}+default
Summary:        Command line prompting library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/editor) = %{version}
Requires:       crate(%{pkgname}/password) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust dialoguer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fuzzy-matcher
Summary:        Command line prompting library - feature "fuzzy-matcher" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fuzzy-matcher-0.3/default) >= 0.3.7
Provides:       crate(%{pkgname}/fuzzy-matcher) = %{version}
Provides:       crate(%{pkgname}/fuzzy-select) = %{version}

%description -n %{name}+fuzzy-matcher
This metapackage enables feature "fuzzy-matcher" for the Rust dialoguer crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "fuzzy-select" feature.

%package     -n %{name}+tempfile
Summary:        Command line prompting library - feature "tempfile" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tempfile-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/editor) = %{version}
Provides:       crate(%{pkgname}/tempfile) = %{version}

%description -n %{name}+tempfile
This metapackage enables feature "tempfile" for the Rust dialoguer crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "editor" feature.

%package     -n %{name}+zeroize
Summary:        Command line prompting library - feature "zeroize" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1/default) >= 1.1.1
Provides:       crate(%{pkgname}/password) = %{version}
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust dialoguer crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "password" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
