# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hashbrown
%global full_version 0.15.5
%global pkgname hashbrown-0.15

Name:           rust-hashbrown-0.15
Version:        0.15.5
Release:        %autorelease
Summary:        Rust crate "hashbrown"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/hashbrown
#!RemoteAsset:  sha256:9229cfe53dfd69f0609a49f65461bd93001ea1ef889cd5529dd176593f5338a1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/inline-more)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/raw-entry)
Provides:       crate(%{pkgname}/rustc-internal-api)

%description
Source code for takopackized Rust crate "hashbrown"

%package     -n %{name}+alloc
Summary:        Rust port of Google's SwissTable hash map - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-alloc-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+allocator-api2
Summary:        Rust port of Google's SwissTable hash map - feature "allocator-api2"
Requires:       crate(%{pkgname})
Requires:       crate(allocator-api2-0.2/alloc) >= 0.2.9
Provides:       crate(%{pkgname}/allocator-api2)

%description -n %{name}+allocator-api2
This metapackage enables feature "allocator-api2" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        Rust port of Google's SwissTable hash map - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rust port of Google's SwissTable hash map - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/allocator-api2)
Requires:       crate(%{pkgname}/default-hasher)
Requires:       crate(%{pkgname}/equivalent)
Requires:       crate(%{pkgname}/inline-more)
Requires:       crate(%{pkgname}/raw-entry)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default-hasher
Summary:        Rust port of Google's SwissTable hash map - feature "default-hasher"
Requires:       crate(%{pkgname})
Requires:       crate(foldhash-0.1) >= 0.1.5
Provides:       crate(%{pkgname}/default-hasher)

%description -n %{name}+default-hasher
This metapackage enables feature "default-hasher" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+equivalent
Summary:        Rust port of Google's SwissTable hash map - feature "equivalent"
Requires:       crate(%{pkgname})
Requires:       crate(equivalent-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/equivalent)

%description -n %{name}+equivalent
This metapackage enables feature "equivalent" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Rust port of Google's SwissTable hash map - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.2
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Rust port of Google's SwissTable hash map - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/core)
Requires:       crate(%{pkgname}/nightly)
Requires:       crate(%{pkgname}/rustc-internal-api)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Rust port of Google's SwissTable hash map - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.25
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
