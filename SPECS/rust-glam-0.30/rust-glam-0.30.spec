# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name glam
%global full_version 0.30.10
%global pkgname glam-0.30

Name:           rust-glam-0.30
Version:        0.30.10
Release:        %autorelease
Summary:        Rust crate "glam"
License:        MIT OR Apache-2.0
URL:            https://github.com/bitshifter/glam-rs
#!RemoteAsset:  sha256:19fc433e8437a212d1b6f1e68c7824af3aed907da60afa994e7f542d18d12aa9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cuda) = %{version}
Provides:       crate(%{pkgname}/debug-glam-assert) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fast-math) = %{version}
Provides:       crate(%{pkgname}/glam-assert) = %{version}
Provides:       crate(%{pkgname}/scalar-math) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "glam"

%package     -n %{name}+approx
Summary:        Simple and fast 3D math library for games and graphics - feature "approx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(approx-0.5) >= 0.5.0
Provides:       crate(%{pkgname}/approx) = %{version}

%description -n %{name}+approx
This metapackage enables feature "approx" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arbitrary
Summary:        Simple and fast 3D math library for games and graphics - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1) >= 1.4.2
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytecheck
Summary:        Simple and fast 3D math library for games and graphics - feature "bytecheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.8/bytecheck) >= 0.8.0
Provides:       crate(%{pkgname}/bytecheck) = %{version}

%description -n %{name}+bytecheck
This metapackage enables feature "bytecheck" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Simple and fast 3D math library for games and graphics - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/aarch64-simd) >= 1.9.0
Requires:       crate(bytemuck-1/derive) >= 1.9.0
Requires:       crate(bytemuck-1/wasm-simd) >= 1.9.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core-simd
Summary:        Simple and fast 3D math library for games and graphics - feature "core-simd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/aarch64-simd) >= 1.9.0
Requires:       crate(bytemuck-1/derive) >= 1.9.0
Requires:       crate(bytemuck-1/nightly-portable-simd) >= 1.9.0
Requires:       crate(bytemuck-1/wasm-simd) >= 1.9.0
Provides:       crate(%{pkgname}/core-simd) = %{version}

%description -n %{name}+core-simd
This metapackage enables feature "core-simd" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encase
Summary:        Simple and fast 3D math library for games and graphics - feature "encase"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(encase-0.12) >= 0.12.0
Provides:       crate(%{pkgname}/encase) = %{version}

%description -n %{name}+encase
This metapackage enables feature "encase" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        Simple and fast 3D math library for games and graphics - feature "libm" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libm-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/libm) = %{version}
Provides:       crate(%{pkgname}/nostd-libm) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nostd-libm" feature.

%package     -n %{name}+mint
Summary:        Simple and fast 3D math library for games and graphics - feature "mint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mint-0.5) >= 0.5.8
Provides:       crate(%{pkgname}/mint) = %{version}

%description -n %{name}+mint
This metapackage enables feature "mint" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Simple and fast 3D math library for games and graphics - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv
Summary:        Simple and fast 3D math library for games and graphics - feature "rkyv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rkyv) = %{version}

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Simple and fast 3D math library for games and graphics - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+speedy
Summary:        Simple and fast 3D math library for games and graphics - feature "speedy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(speedy-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/speedy) = %{version}

%description -n %{name}+speedy
This metapackage enables feature "speedy" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerocopy
Summary:        Simple and fast 3D math library for games and graphics - feature "zerocopy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zerocopy-0.8/simd) >= 0.8.0
Requires:       crate(zerocopy-derive-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/zerocopy) = %{version}

%description -n %{name}+zerocopy
This metapackage enables feature "zerocopy" for the Rust glam crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
