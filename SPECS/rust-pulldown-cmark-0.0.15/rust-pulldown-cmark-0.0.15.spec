# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pulldown-cmark
%global full_version 0.0.15
%global pkgname pulldown-cmark-0.0.15

Name:           rust-pulldown-cmark-0.0.15
Version:        0.0.15
Release:        %autorelease
Summary:        Rust crate "pulldown-cmark"
License:        MIT
URL:            https://github.com/google/pulldown-cmark
#!RemoteAsset:  sha256:378e941dbd392c101f2cb88097fa4d7167bc421d4b88de3ff7dbee503bc3233b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/gen-tests) = %{version}

%description
Source code for takopackized Rust crate "pulldown-cmark"

%package     -n %{name}+getopts
Summary:        Pull parser for CommonMark - feature "getopts" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getopts-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/getopts) = %{version}

%description -n %{name}+getopts
This metapackage enables feature "getopts" for the Rust pulldown-cmark crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
