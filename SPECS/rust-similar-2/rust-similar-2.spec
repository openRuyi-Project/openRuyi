# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name similar
%global full_version 2.7.0
%global pkgname similar-2

Name:           rust-similar-2
Version:        2.7.0
Release:        %autorelease
Summary:        Rust crate "similar"
License:        Apache-2.0
URL:            https://github.com/mitsuhiko/similar
#!RemoteAsset:  sha256:bbbb5d9659141646ae647b42fe094daf6c6192d1620870b449d9557f748b2daa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/inline) = %{version}
Provides:       crate(%{pkgname}/text) = %{version}

%description
Source code for takopackized Rust crate "similar"

%package     -n %{name}+bstr
Summary:        Diff library for Rust - feature "bstr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bstr-1) >= 1.5.0
Provides:       crate(%{pkgname}/bstr) = %{version}

%description -n %{name}+bstr
This metapackage enables feature "bstr" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Diff library for Rust - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bstr) = %{version}
Requires:       crate(%{pkgname}/text) = %{version}
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Diff library for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.130
Requires:       crate(serde-1/derive) >= 1.0.130
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Diff library for Rust - feature "unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/text) = %{version}
Requires:       crate(%{pkgname}/unicode-segmentation) = %{version}
Requires:       crate(bstr-1/std) >= 1.5.0
Requires:       crate(bstr-1/unicode) >= 1.5.0
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-segmentation
Summary:        Diff library for Rust - feature "unicode-segmentation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-segmentation-1/default) >= 1.7.1
Provides:       crate(%{pkgname}/unicode-segmentation) = %{version}

%description -n %{name}+unicode-segmentation
This metapackage enables feature "unicode-segmentation" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+web-time
Summary:        Diff library for Rust - feature "web-time" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(web-time-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/wasm32-web-time) = %{version}
Provides:       crate(%{pkgname}/web-time) = %{version}

%description -n %{name}+web-time
This metapackage enables feature "web-time" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "wasm32_web_time" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
