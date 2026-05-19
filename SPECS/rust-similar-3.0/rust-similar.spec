# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name similar
%global full_version 3.1.0
%global pkgname similar-3.0

Name:           rust-similar-3.0
Version:        3.1.0
Release:        %autorelease
Summary:        Rust crate "similar"
License:        Apache-2.0
URL:            https://github.com/mitsuhiko/similar
#!RemoteAsset:  sha256:04d93e861ede2e497b47833469b8ec9d5c07fa4c78ce7a00f6eb7dd8168b4b3f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/inline)
Provides:       crate(%{pkgname}/text)

%description
Source code for takopackized Rust crate "similar"

%package     -n %{name}+bstr
Summary:        Diff library for Rust - feature "bstr"
Requires:       crate(%{pkgname})
Requires:       crate(bstr-1.0) >= 1.5.0
Provides:       crate(%{pkgname}/bstr)

%description -n %{name}+bstr
This metapackage enables feature "bstr" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Diff library for Rust - feature "bytes"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bstr)
Requires:       crate(%{pkgname}/text)
Provides:       crate(%{pkgname}/bytes)

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Diff library for Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/text)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown
Summary:        Diff library for Rust - feature "hashbrown"
Requires:       crate(%{pkgname})
Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.0
Provides:       crate(%{pkgname}/hashbrown)

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Diff library for Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/alloc) >= 1.0.130
Requires:       crate(serde-1.0/derive) >= 1.0.130
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Diff library for Rust - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(bstr-1.0/std) >= 1.5.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Diff library for Rust - feature "unicode"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/text)
Requires:       crate(%{pkgname}/unicode-segmentation)
Requires:       crate(bstr-1.0/unicode) >= 1.5.0
Provides:       crate(%{pkgname}/unicode)

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-segmentation
Summary:        Diff library for Rust - feature "unicode-segmentation"
Requires:       crate(%{pkgname})
Requires:       crate(unicode-segmentation-1.0/default) >= 1.7.1
Provides:       crate(%{pkgname}/unicode-segmentation)

%description -n %{name}+unicode-segmentation
This metapackage enables feature "unicode-segmentation" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+web-time
Summary:        Diff library for Rust - feature "web-time" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(web-time-1.0/default) >= 1.1
Provides:       crate(%{pkgname}/wasm32-web-time)
Provides:       crate(%{pkgname}/web-time)

%description -n %{name}+web-time
This metapackage enables feature "web-time" for the Rust similar crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "wasm32_web_time" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
