# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-bidi
%global full_version 0.3.18
%global pkgname unicode-bidi-0.3

Name:           rust-unicode-bidi-0.3
Version:        0.3.18
Release:        %autorelease
Summary:        Rust crate "unicode-bidi"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/unicode-bidi
#!RemoteAsset:  sha256:5c1cb5db39152898a79168971543b1cb5020dff7fe43c8dc468b0885f5e29df5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bench-it) = %{version}
Provides:       crate(%{pkgname}/hardcoded-data) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "unicode-bidi"

%package     -n %{name}+default
Summary:        The Unicode Bidirectional Algorithm - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hardcoded-data) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust unicode-bidi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flame
Summary:        The Unicode Bidirectional Algorithm - feature "flame"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flame-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/flame) = %{version}

%description -n %{name}+flame
This metapackage enables feature "flame" for the Rust unicode-bidi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flame-it
Summary:        The Unicode Bidirectional Algorithm - feature "flame_it"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/flame) = %{version}
Requires:       crate(%{pkgname}/flamer) = %{version}
Provides:       crate(%{pkgname}/flame-it) = %{version}

%description -n %{name}+flame-it
This metapackage enables feature "flame_it" for the Rust unicode-bidi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flamer
Summary:        The Unicode Bidirectional Algorithm - feature "flamer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flamer-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/flamer) = %{version}

%description -n %{name}+flamer
This metapackage enables feature "flamer" for the Rust unicode-bidi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The Unicode Bidirectional Algorithm - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-0.8/derive) >= 0.8.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/with-serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust unicode-bidi crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with_serde" feature.

%package     -n %{name}+smallvec
Summary:        The Unicode Bidirectional Algorithm - feature "smallvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1/default) >= 1.13.0
Requires:       crate(smallvec-1/union) >= 1.13.0
Provides:       crate(%{pkgname}/smallvec) = %{version}

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust unicode-bidi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
