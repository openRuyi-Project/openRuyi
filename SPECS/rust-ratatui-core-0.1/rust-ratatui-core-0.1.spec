# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui-core
%global full_version 0.1.1
%global pkgname ratatui-core-0.1

Name:           rust-ratatui-core-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "ratatui-core"
License:        MIT
URL:            https://ratatui.rs
#!RemoteAsset:  sha256:42d3603f354bba8c595fa47860e60142d7372b7210c27044c6a7d0e1a4336b44
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.12.0
Requires:       crate(compact-str-0.9) >= 0.9.0
Requires:       crate(hashbrown-0.17/default) >= 0.17.0
Requires:       crate(indoc-2/default) >= 2.0.0
Requires:       crate(itertools-0.14/use-alloc) >= 0.14.0
Requires:       crate(kasuari-0.4) >= 0.4.0
Requires:       crate(lru-0.18/default) >= 0.18.0
Requires:       crate(strum-0.28/derive) >= 0.28.0
Requires:       crate(thiserror-2) >= 2.0.0
Requires:       crate(unicode-segmentation-1/default) >= 1.0.0
Requires:       crate(unicode-truncate-2) >= 2.0.0
Requires:       crate(unicode-width-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/scrolling-regions) = %{version}
Provides:       crate(%{pkgname}/underline-color) = %{version}

%description
Widget libraries should use this crate. Applications should use the main Ratatui crate.
Source code for takopackized Rust crate "ratatui-core"

%package     -n %{name}+anstyle
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "anstyle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstyle-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/anstyle) = %{version}

%description -n %{name}+anstyle
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "anstyle" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "document-features" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+layout-cache
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "layout-cache"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(critical-section-1/default) >= 1.2.0
Provides:       crate(%{pkgname}/layout-cache) = %{version}

%description -n %{name}+layout-cache
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "layout-cache" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+palette
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "palette"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(palette-0.7/libm) >= 0.7.6
Provides:       crate(%{pkgname}/palette) = %{version}

%description -n %{name}+palette
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "palette" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "portable-atomic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(kasuari-0.4/portable-atomic) >= 0.4.0
Provides:       crate(%{pkgname}/portable-atomic) = %{version}

%description -n %{name}+portable-atomic
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "portable-atomic" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/serde) >= 2.12.0
Requires:       crate(compact-str-0.9/serde) >= 0.9.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "serde" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.12.0
Requires:       crate(compact-str-0.9/std) >= 0.9.0
Requires:       crate(itertools-0.14/use-alloc) >= 0.14.0
Requires:       crate(itertools-0.14/use-std) >= 0.14.0
Requires:       crate(kasuari-0.4/std) >= 0.4.0
Requires:       crate(palette-0.7/libm) >= 0.7.6
Requires:       crate(palette-0.7/std) >= 0.7.6
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Requires:       crate(strum-0.28/derive) >= 0.28.0
Requires:       crate(strum-0.28/std) >= 0.28.0
Requires:       crate(thiserror-2/std) >= 2.0.0
Requires:       crate(unicode-truncate-2/std) >= 2.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "std" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
