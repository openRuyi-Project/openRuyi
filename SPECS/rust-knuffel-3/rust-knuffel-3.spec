# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name knuffel
%global full_version 3.2.0
%global pkgname knuffel-3

Name:           rust-knuffel-3
Version:        3.2.0
Release:        %autorelease
Summary:        Rust crate "knuffel"
License:        MIT OR Apache-2.0
URL:            https://github.com/tailhook/knuffel
#!RemoteAsset:  sha256:04bee6ddc6071011314b1ce4f7705fef6c009401dba4fd22cb0009db6a177413
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(chumsky-0.9) >= 0.9.2
Requires:       crate(miette-5/default) >= 5.1.1
Requires:       crate(thiserror-1/default) >= 1.0.31
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "knuffel"

%package     -n %{name}+base64
Summary:        Another KDL language implementation - feature "base64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.21/default) >= 0.21.0
Provides:       crate(%{pkgname}/base64) = %{version}

%description -n %{name}+base64
This metapackage enables feature "base64" for the Rust knuffel crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Another KDL language implementation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/line-numbers) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust knuffel crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+knuffel-derive
Summary:        Another KDL language implementation - feature "knuffel-derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(knuffel-derive-3/default) >= 3.2.0
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/knuffel-derive) = %{version}

%description -n %{name}+knuffel-derive
This metapackage enables feature "knuffel-derive" for the Rust knuffel crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%package     -n %{name}+minicbor
Summary:        Another KDL language implementation - feature "minicbor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(minicbor-0.19/default) >= 0.19.1
Requires:       crate(minicbor-0.19/derive) >= 0.19.1
Requires:       crate(minicbor-0.19/std) >= 0.19.1
Provides:       crate(%{pkgname}/minicbor) = %{version}

%description -n %{name}+minicbor
This metapackage enables feature "minicbor" for the Rust knuffel crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-width
Summary:        Another KDL language implementation - feature "unicode-width" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-width-0.1/default) >= 0.1.9
Provides:       crate(%{pkgname}/line-numbers) = %{version}
Provides:       crate(%{pkgname}/unicode-width) = %{version}

%description -n %{name}+unicode-width
This metapackage enables feature "unicode-width" for the Rust knuffel crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "line-numbers" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
