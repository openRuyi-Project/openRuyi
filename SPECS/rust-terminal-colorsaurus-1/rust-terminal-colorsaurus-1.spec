# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name terminal-colorsaurus
%global full_version 1.0.3
%global pkgname terminal-colorsaurus-1

Name:           rust-terminal-colorsaurus-1
Version:        1.0.3
Release:        %autorelease
Summary:        Rust crate "terminal-colorsaurus"
License:        MIT OR Apache-2.0
URL:            https://github.com/tautropfli/terminal-colorsaurus
#!RemoteAsset:  sha256:7a46bb5364467da040298c573c8a95dbf9a512efc039630409a03126e3703e90
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.151
Requires:       crate(memchr-2/default) >= 2.7.1
Requires:       crate(mio-1/os-ext) >= 1.1.0
Requires:       crate(terminal-trx-0.2/default) >= 0.2.6
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.0
Requires:       crate(xterm-color-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
It answers the question «Is this terminal dark or light?».
Source code for takopackized Rust crate "terminal-colorsaurus"

%package     -n %{name}+anstyle
Summary:        Cross-platform library for determining the terminal's background and foreground color - feature "anstyle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstyle-1/default) >= 1.0.7
Provides:       crate(%{pkgname}/anstyle) = %{version}

%description -n %{name}+anstyle
It answers the question «Is this terminal dark or light?».
This metapackage enables feature "anstyle" for the Rust terminal-colorsaurus crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rgb
Summary:        Cross-platform library for determining the terminal's background and foreground color - feature "rgb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rgb-0.8/default) >= 0.8.37
Provides:       crate(%{pkgname}/rgb) = %{version}

%description -n %{name}+rgb
It answers the question «Is this terminal dark or light?».
This metapackage enables feature "rgb" for the Rust terminal-colorsaurus crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
