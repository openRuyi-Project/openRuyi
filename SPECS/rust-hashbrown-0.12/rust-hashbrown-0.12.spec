# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hashbrown
%global full_version 0.12.3
%global pkgname hashbrown-0.12

Name:           rust-hashbrown-0.12
Version:        0.12.3
Release:        %autorelease
Summary:        Rust crate "hashbrown"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/hashbrown
#!RemoteAsset:  sha256:8a9ee70c43aaf417c914396645a0fa852624801b24ebb7ae78fe8272889ac888
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/inline-more) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/raw) = %{version}
Provides:       crate(%{pkgname}/rustc-internal-api) = %{version}

%description
Source code for takopackized Rust crate "hashbrown"

%package     -n %{name}+ahash
Summary:        Rust port of Google's SwissTable hash map - feature "ahash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ahash-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/ahash) = %{version}

%description -n %{name}+ahash
This metapackage enables feature "ahash" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ahash-compile-time-rng
Summary:        Rust port of Google's SwissTable hash map - feature "ahash-compile-time-rng"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ahash-0.7/compile-time-rng) >= 0.7.0
Provides:       crate(%{pkgname}/ahash-compile-time-rng) = %{version}

%description -n %{name}+ahash-compile-time-rng
This metapackage enables feature "ahash-compile-time-rng" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bumpalo
Summary:        Rust port of Google's SwissTable hash map - feature "bumpalo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bumpalo-3/default) >= 3.5.0
Provides:       crate(%{pkgname}/bumpalo) = %{version}

%description -n %{name}+bumpalo
This metapackage enables feature "bumpalo" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compiler-builtins
Summary:        Rust port of Google's SwissTable hash map - feature "compiler_builtins"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.2
Provides:       crate(%{pkgname}/compiler-builtins) = %{version}

%description -n %{name}+compiler-builtins
This metapackage enables feature "compiler_builtins" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rust port of Google's SwissTable hash map - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ahash) = %{version}
Requires:       crate(%{pkgname}/inline-more) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Rust port of Google's SwissTable hash map - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Rust port of Google's SwissTable hash map - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/compiler-builtins) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(%{pkgname}/nightly) = %{version}
Requires:       crate(%{pkgname}/rustc-internal-api) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Rust port of Google's SwissTable hash map - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.25
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust hashbrown crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
