# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name textwrap
%global full_version 0.11.0
%global pkgname textwrap-0.11

Name:           rust-textwrap-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "textwrap"
License:        MIT
URL:            https://github.com/mgeisler/textwrap
#!RemoteAsset:  sha256:d326610f408c7a4eb6f51c37c330e496b08506c9457c9d34287ecc38809fb060
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-width-0.1/default) >= 0.1.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
You can use it to format strings (such as help and error messages) for display in commandline applications. It is designed to be efficient and handle Unicode characters correctly.
Source code for takopackized Rust crate "textwrap"

%package     -n %{name}+hyphenation
Summary:        Small library for word wrapping, indenting, and dedenting strings - feature "hyphenation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyphenation-0.7/default) >= 0.7.1
Requires:       crate(hyphenation-0.7/embed-all) >= 0.7.1
Provides:       crate(%{pkgname}/hyphenation) = %{version}

%description -n %{name}+hyphenation
You can use it to format strings (such as help and error messages) for display in commandline applications. It is designed to be efficient and handle Unicode characters correctly.
This metapackage enables feature "hyphenation" for the Rust textwrap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+term-size
Summary:        Small library for word wrapping, indenting, and dedenting strings - feature "term_size"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(term-size-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/term-size) = %{version}

%description -n %{name}+term-size
You can use it to format strings (such as help and error messages) for display in commandline applications. It is designed to be efficient and handle Unicode characters correctly.
This metapackage enables feature "term_size" for the Rust textwrap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
