# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ansi_colours
%global full_version 1.2.3
%global pkgname ansi-colours-1

Name:           rust-ansi-colours-1
Version:        1.2.3
Release:        %autorelease
Summary:        Rust crate "ansi_colours"
License:        LGPL-3.0-or-later
URL:            https://github.com/mina86/ansi_colours
#!RemoteAsset:  sha256:14eec43e0298190790f41679fe69ef7a829d2a2ddd78c8c00339e84710e435fe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ansi_colours"

%package     -n %{name}+ansi-term
Summary:        True-colour ↔ ANSI terminal palette converter - feature "ansi_term"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ansi-term-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/ansi-term) = %{version}

%description -n %{name}+ansi-term
This metapackage enables feature "ansi_term" for the Rust ansi_colours crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+anstyle
Summary:        True-colour ↔ ANSI terminal palette converter - feature "anstyle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstyle-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/anstyle) = %{version}

%description -n %{name}+anstyle
This metapackage enables feature "anstyle" for the Rust ansi_colours crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rgb
Summary:        True-colour ↔ ANSI terminal palette converter - feature "rgb" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rgb-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rgb) = %{version}

%description -n %{name}+rgb
This metapackage enables feature "rgb" for the Rust ansi_colours crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+termcolor
Summary:        True-colour ↔ ANSI terminal palette converter - feature "termcolor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(termcolor-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/termcolor) = %{version}

%description -n %{name}+termcolor
This metapackage enables feature "termcolor" for the Rust ansi_colours crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
