# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lscolors
%global full_version 0.21.0
%global pkgname lscolors-0.21

Name:           rust-lscolors-0.21
Version:        0.21.0
Release:        %autorelease
Summary:        Rust crate "lscolors"
License:        MIT OR Apache-2.0
URL:            https://github.com/sharkdp/lscolors
#!RemoteAsset:  sha256:d60e266dfb1426eb2d24792602e041131fdc0236bb7007abc0e589acafd60929
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aho-corasick-1/default) >= 1.1.3

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "lscolors"

%package     -n %{name}+ansi-term
Summary:        Colorize paths using the LS_COLORS environment variable - feature "ansi_term"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ansi-term-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/ansi-term) = %{version}

%description -n %{name}+ansi-term
This metapackage enables feature "ansi_term" for the Rust lscolors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossterm
Summary:        Colorize paths using the LS_COLORS environment variable - feature "crossterm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossterm-0.29/default) >= 0.29.0
Provides:       crate(%{pkgname}/crossterm) = %{version}

%description -n %{name}+crossterm
This metapackage enables feature "crossterm" for the Rust lscolors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnu-legacy
Summary:        Colorize paths using the LS_COLORS environment variable - feature "gnu_legacy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nu-ansi-term-0.50/gnu-legacy) >= 0.50.0
Provides:       crate(%{pkgname}/gnu-legacy) = %{version}

%description -n %{name}+gnu-legacy
This metapackage enables feature "gnu_legacy" for the Rust lscolors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nu-ansi-term
Summary:        Colorize paths using the LS_COLORS environment variable - feature "nu-ansi-term" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nu-ansi-term-0.50/default) >= 0.50.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nu-ansi-term) = %{version}

%description -n %{name}+nu-ansi-term
This metapackage enables feature "nu-ansi-term" for the Rust lscolors crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+owo-colors
Summary:        Colorize paths using the LS_COLORS environment variable - feature "owo-colors"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(owo-colors-4/default) >= 4.0.0
Provides:       crate(%{pkgname}/owo-colors) = %{version}

%description -n %{name}+owo-colors
This metapackage enables feature "owo-colors" for the Rust lscolors crate, by pulling in any additional dependencies needed by that feature.

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
