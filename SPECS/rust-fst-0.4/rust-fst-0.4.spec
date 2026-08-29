# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fst
%global full_version 0.4.7
%global pkgname fst-0.4

Name:           rust-fst-0.4
Version:        0.4.7
Release:        %autorelease
Summary:        Rust crate "fst"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/fst
#!RemoteAsset:  sha256:7ab85b9b05e3978cc9a9cf8fea7f01b494e1a09ed3037e16ba39edc7a29eb61a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fst"

%package     -n %{name}+utf8-ranges
Summary:        Use finite state transducers to compactly represents sets or maps of many strings (> 1 billion is possible) - feature "utf8-ranges" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(utf8-ranges-1/default) >= 1.0.4
Provides:       crate(%{pkgname}/levenshtein) = %{version}
Provides:       crate(%{pkgname}/utf8-ranges) = %{version}

%description -n %{name}+utf8-ranges
This metapackage enables feature "utf8-ranges" for the Rust fst crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "levenshtein" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
