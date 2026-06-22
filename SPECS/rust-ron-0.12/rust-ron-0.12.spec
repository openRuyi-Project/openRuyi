# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ron
%global full_version 0.12.1
%global pkgname ron-0.12

Name:           rust-ron-0.12
Version:        0.12.1
Release:        %autorelease
Summary:        Rust crate "ron"
License:        MIT OR Apache-2.0
URL:            https://github.com/ron-rs/ron
#!RemoteAsset:  sha256:4147b952f3f819eca0e99527022f7d6a8d05f111aeb0a62960c74eb283bec8fc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/serde) >= 2.1.0
Requires:       crate(once-cell-1/alloc) >= 1.20.0
Requires:       crate(once-cell-1/race) >= 1.20.0
Requires:       crate(serde-1/alloc) >= 1.0.181
Requires:       crate(serde-derive-1) >= 1.0.181
Requires:       crate(typeid-1) >= 1.0.1
Requires:       crate(unicode-ident-1) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/integer128) = %{version}

%description
Source code for takopackized Rust crate "ron"

%package     -n %{name}+indexmap
Summary:        Rusty Object Notation - feature "indexmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(indexmap-2/serde) >= 2.0.0
Provides:       crate(%{pkgname}/indexmap) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust ron crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Rusty Object Notation - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.181
Requires:       crate(serde-1/std) >= 1.0.181
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ron crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+unicode-segmentation
Summary:        Rusty Object Notation - feature "unicode-segmentation" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-segmentation-1) >= 1.12.0
Provides:       crate(%{pkgname}/internal-span-substring-test) = %{version}
Provides:       crate(%{pkgname}/unicode-segmentation) = %{version}

%description -n %{name}+unicode-segmentation
This metapackage enables feature "unicode-segmentation" for the Rust ron crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "internal-span-substring-test" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
