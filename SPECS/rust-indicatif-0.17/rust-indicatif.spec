# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name indicatif
%global full_version 0.17.11
%global pkgname indicatif-0.17

Name:           rust-indicatif-0.17
Version:        0.17.11
Release:        %autorelease
Summary:        Rust crate "indicatif"
License:        MIT
URL:            https://github.com/console-rs/indicatif
#!RemoteAsset:  sha256:183b3088984b400f4cfac3620d5e076c84da5364016b4f49473de574b2586235
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(console-0.15/ansi-parsing) >= 0.15.11
Requires:       crate(number-prefix-0.4/default) >= 0.4.0
Requires:       crate(portable-atomic-1.0/default) >= 1.13.0
Requires:       crate(web-time-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "indicatif"

%package     -n %{name}+default
Summary:        Progress bar and cli reporting library for Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/unicode-width)
Requires:       crate(console-0.15/ansi-parsing) >= 0.15.11
Requires:       crate(console-0.15/unicode-width) >= 0.15.11
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Progress bar and cli reporting library for Rust - feature "futures"
Requires:       crate(%{pkgname})
Requires:       crate(futures-core-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/futures)

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+improved-unicode
Summary:        Progress bar and cli reporting library for Rust - feature "improved_unicode"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/unicode-segmentation)
Requires:       crate(%{pkgname}/unicode-width)
Requires:       crate(console-0.15/ansi-parsing) >= 0.15.11
Requires:       crate(console-0.15/unicode-width) >= 0.15.11
Provides:       crate(%{pkgname}/improved-unicode)

%description -n %{name}+improved-unicode
This metapackage enables feature "improved_unicode" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Progress bar and cli reporting library for Rust - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.1
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Progress bar and cli reporting library for Rust - feature "tokio"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0/default) >= 1.0.0
Requires:       crate(tokio-1.0/io-util) >= 1.0.0
Provides:       crate(%{pkgname}/tokio)

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-segmentation
Summary:        Progress bar and cli reporting library for Rust - feature "unicode-segmentation"
Requires:       crate(%{pkgname})
Requires:       crate(unicode-segmentation-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/unicode-segmentation)

%description -n %{name}+unicode-segmentation
This metapackage enables feature "unicode-segmentation" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-width
Summary:        Progress bar and cli reporting library for Rust - feature "unicode-width"
Requires:       crate(%{pkgname})
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/unicode-width)

%description -n %{name}+unicode-width
This metapackage enables feature "unicode-width" for the Rust indicatif crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
