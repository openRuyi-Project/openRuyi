# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui-widgets
%global full_version 0.3.1
%global pkgname ratatui-widgets-0.3

Name:           rust-ratatui-widgets-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "ratatui-widgets"
License:        MIT
URL:            https://ratatui.rs
#!RemoteAsset:  sha256:7ef4f17dd7ac3abf5adc2b920a03c61eee4bfe6a88fa5191936895525371d79c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.12.0
Requires:       crate(hashbrown-0.17/default) >= 0.17.0
Requires:       crate(indoc-2/default) >= 2.0.0
Requires:       crate(instability-0.3/default) >= 0.3.0
Requires:       crate(itertools-0.14/use-alloc) >= 0.14.0
Requires:       crate(line-clipping-0.3/default) >= 0.3.0
Requires:       crate(ratatui-core-0.1/default) >= 0.1.1
Requires:       crate(strum-0.28/derive) >= 0.28.0
Requires:       crate(unicode-segmentation-1/default) >= 1.0.0
Requires:       crate(unicode-width-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}
Provides:       crate(%{pkgname}/unstable-rendered-line-info) = %{version}

%description
Source code for takopackized Rust crate "ratatui-widgets"

%package     -n %{name}+calendar
Summary:        Collection of Ratatui widgets for building terminal user interfaces using Ratatui - feature "calendar" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3) >= 0.3.47
Provides:       crate(%{pkgname}/all-widgets) = %{version}
Provides:       crate(%{pkgname}/calendar) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+calendar
This metapackage enables feature "calendar" for the Rust ratatui-widgets crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "all-widgets", and "default" features.

%package     -n %{name}+document-features
Summary:        Collection of Ratatui widgets for building terminal user interfaces using Ratatui - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust ratatui-widgets crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Collection of Ratatui widgets for building terminal user interfaces using Ratatui - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ratatui-core-0.1/serde) >= 0.1.1
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ratatui-widgets crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Collection of Ratatui widgets for building terminal user interfaces using Ratatui - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Requires:       crate(time-0.3/local-offset) >= 0.3.47
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ratatui-widgets crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
