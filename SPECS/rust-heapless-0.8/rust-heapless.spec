# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name heapless
%global full_version 0.8.0
%global pkgname heapless-0.8

Name:           rust-heapless-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "heapless"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-embedded/heapless
#!RemoteAsset:  sha256:0bfb9eb618601c89945a70e254898da93b13be0388091d42117462b265bb3fad
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hash32-0.3/default) >= 0.3.1
Requires:       crate(stable-deref-trait-1.0) >= 1.2.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/mpmc-large)

%description
Source code for takopackized Rust crate "heapless"

%package     -n %{name}+defmt-03
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "defmt-03"
Requires:       crate(%{pkgname})
Requires:       crate(defmt-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/defmt-03)

%description -n %{name}+defmt-03
This metapackage enables feature "defmt-03" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "portable-atomic"
Requires:       crate(%{pkgname})
Requires:       crate(portable-atomic-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/portable-atomic)

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic-critical-section
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "portable-atomic-critical-section"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/portable-atomic)
Requires:       crate(portable-atomic-1.0/critical-section) >= 1.0.0
Requires:       crate(portable-atomic-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/portable-atomic-critical-section)

%description -n %{name}+portable-atomic-critical-section
This metapackage enables feature "portable-atomic-critical-section" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic-unsafe-assume-single-core
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "portable-atomic-unsafe-assume-single-core"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/portable-atomic)
Requires:       crate(portable-atomic-1.0/default) >= 1.0.0
Requires:       crate(portable-atomic-1.0/unsafe-assume-single-core) >= 1.0.0
Provides:       crate(%{pkgname}/portable-atomic-unsafe-assume-single-core)

%description -n %{name}+portable-atomic-unsafe-assume-single-core
This metapackage enables feature "portable-atomic-unsafe-assume-single-core" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ufmt
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "ufmt"
Requires:       crate(%{pkgname})
Requires:       crate(ufmt-write-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/ufmt)

%description -n %{name}+ufmt
This metapackage enables feature "ufmt" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
