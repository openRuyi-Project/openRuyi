# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name heapless
%global full_version 0.7.17
%global pkgname heapless-0.7

Name:           rust-heapless-0.7
Version:        0.7.17
Release:        %autorelease
Summary:        Rust crate "heapless"
License:        MIT OR Apache-2.0
URL:            https://github.com/japaric/heapless
#!RemoteAsset:  sha256:cdc6457c0eb62c71aac4bc17216026d8410337c4126773b9c5daba343f17964f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atomic-polyfill-1/default) >= 1.0.0
Requires:       crate(hash32-0.2/default) >= 0.2.1
Requires:       crate(rustc-version-0.4) >= 0.4.0
Requires:       crate(spin-0.9/default) >= 0.9.2
Requires:       crate(stable-deref-trait-1) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/mpmc-large) = %{version}
Provides:       crate(%{pkgname}/trybuild) = %{version}
Provides:       crate(%{pkgname}/x86-sync-pool) = %{version}

%description
Source code for takopackized Rust crate "heapless"

%package     -n %{name}+atomic-polyfill
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "atomic-polyfill" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atomic-polyfill-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/atomic-polyfill) = %{version}
Provides:       crate(%{pkgname}/cas) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+atomic-polyfill
This metapackage enables feature "atomic-polyfill" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "cas", and "default" features.

%package     -n %{name}+defmt
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "defmt" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/defmt) = %{version}
Provides:       crate(%{pkgname}/defmt-impl) = %{version}

%description -n %{name}+defmt
This metapackage enables feature "defmt" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "defmt-impl" feature.

%package     -n %{name}+serde
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ufmt-write
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "ufmt-write" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ufmt-write-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/ufmt-impl) = %{version}
Provides:       crate(%{pkgname}/ufmt-write) = %{version}

%description -n %{name}+ufmt-write
This metapackage enables feature "ufmt-write" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ufmt-impl" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
