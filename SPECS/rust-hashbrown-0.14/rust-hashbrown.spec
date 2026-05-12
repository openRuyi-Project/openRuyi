# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hashbrown
%global full_version 0.14.5
%global pkgname hashbrown-0.14

Name:           rust-hashbrown-0.14
Version:        0.14.5
Release:        %autorelease
Summary:        Rust crate "hashbrown"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/hashbrown
#!RemoteAsset:  sha256:e5274423e17b7c9fc20b6e7e208532f9b19825d82dfd615708b70edd83df41f1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/inline-more)
Provides:       crate(%{pkgname}/raw)
Provides:       crate(%{pkgname}/rustc-internal-api)

%description
Source code for takopackized Rust crate "hashbrown"

%package     -n %{name}+ahash
Summary:        Rust port of Google's SwissTable hash map - feature "ahash"
Requires:       crate(%{pkgname})
Requires:       crate(ahash-0.8) >= 0.8.7
Provides:       crate(%{pkgname}/ahash)

%description -n %{name}+ahash
This metapackage enables feature "ahash" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

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

%package     -n %{name}+compiler-builtins
Summary:        Rust port of Google's SwissTable hash map - feature "compiler_builtins"
Requires:       crate(%{pkgname})
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.2
Provides:       crate(%{pkgname}/compiler-builtins)

%description -n %{name}+compiler-builtins
This metapackage enables feature "compiler_builtins" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

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
Requires:       crate(%{pkgname}/ahash)
Requires:       crate(%{pkgname}/allocator-api2)
Requires:       crate(%{pkgname}/inline-more)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+equivalent
Summary:        Rust port of Google's SwissTable hash map - feature "equivalent"
Requires:       crate(%{pkgname})
Requires:       crate(equivalent-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/equivalent)

%description -n %{name}+equivalent
This metapackage enables feature "equivalent" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        Rust port of Google's SwissTable hash map - feature "nightly"
Requires:       crate(%{pkgname})
Requires:       crate(allocator-api2-0.2/alloc) >= 0.2.9
Requires:       crate(allocator-api2-0.2/nightly) >= 0.2.9
Provides:       crate(%{pkgname}/nightly)

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Rust port of Google's SwissTable hash map - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv
Summary:        Rust port of Google's SwissTable hash map - feature "rkyv"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7/alloc) >= 0.7.42
Provides:       crate(%{pkgname}/rkyv)

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Rust port of Google's SwissTable hash map - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/compiler-builtins)
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
