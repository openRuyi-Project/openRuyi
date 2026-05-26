# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name chrono
%global full_version 0.4.44
%global pkgname chrono-0.4

Name:           rust-chrono-0.4
Version:        0.4.44
Release:        %autorelease
Summary:        Rust crate "chrono"
License:        MIT OR Apache-2.0
URL:            https://github.com/chronotope/chrono
#!RemoteAsset:  sha256:c673075a2e0e5f4a1dde27ce9dee1ea4558c7ffe648f576438a20ca1d2acc4b0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2) >= 0.2.19
Provides:       crate(chrono) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/internal-bench)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/core-error)
Provides:       crate(%{pkgname}/libc)
Provides:       crate(%{pkgname}/now)
Provides:       crate(%{pkgname}/oldtime)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "chrono"

%package     -n %{name}+arbitrary
Summary:        Date and time library for Rust - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.0.0
Requires:       crate(arbitrary-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clock
Summary:        Date and time library for Rust - feature "clock"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/iana-time-zone)
Requires:       crate(%{pkgname}/now)
Requires:       crate(%{pkgname}/winapi)
Provides:       crate(%{pkgname}/clock)

%description -n %{name}+clock
This metapackage enables feature "clock" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Date and time library for Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/clock)
Requires:       crate(%{pkgname}/oldtime)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/wasmbind)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+defmt
Summary:        Date and time library for Rust - feature "defmt"
Requires:       crate(%{pkgname})
Requires:       crate(defmt-1.0/default) >= 1.0.1
Requires:       crate(pure-rust-locales-0.8/defmt) >= 0.8.2
Provides:       crate(%{pkgname}/defmt)

%description -n %{name}+defmt
This metapackage enables feature "defmt" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+iana-time-zone
Summary:        Date and time library for Rust - feature "iana-time-zone"
Requires:       crate(%{pkgname})
Requires:       crate(iana-time-zone-0.1/default) >= 0.1.65
Requires:       crate(iana-time-zone-0.1/fallback) >= 0.1.65
Provides:       crate(%{pkgname}/iana-time-zone)

%description -n %{name}+iana-time-zone
This metapackage enables feature "iana-time-zone" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+js-sys
Summary:        Date and time library for Rust - feature "js-sys"
Requires:       crate(%{pkgname})
Requires:       crate(js-sys-0.3/default) >= 0.3.98
Provides:       crate(%{pkgname}/js-sys)

%description -n %{name}+js-sys
This metapackage enables feature "js-sys" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pure-rust-locales
Summary:        Date and time library for Rust - feature "pure-rust-locales" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(pure-rust-locales-0.8/default) >= 0.8.2
Provides:       crate(%{pkgname}/pure-rust-locales)
Provides:       crate(%{pkgname}/unstable-locales)

%description -n %{name}+pure-rust-locales
This metapackage enables feature "pure-rust-locales" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-locales" feature.

%package     -n %{name}+rkyv
Summary:        Date and time library for Rust - feature "rkyv" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7) >= 0.7.43
Requires:       crate(rkyv-0.7/size-32) >= 0.7.43
Provides:       crate(%{pkgname}/rkyv)
Provides:       crate(%{pkgname}/rkyv-32)

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rkyv-32" feature.

%package     -n %{name}+rkyv-16
Summary:        Date and time library for Rust - feature "rkyv-16"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7) >= 0.7.43
Requires:       crate(rkyv-0.7/size-16) >= 0.7.43
Provides:       crate(%{pkgname}/rkyv-16)

%description -n %{name}+rkyv-16
This metapackage enables feature "rkyv-16" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-64
Summary:        Date and time library for Rust - feature "rkyv-64"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7) >= 0.7.43
Requires:       crate(rkyv-0.7/size-64) >= 0.7.43
Provides:       crate(%{pkgname}/rkyv-64)

%description -n %{name}+rkyv-64
This metapackage enables feature "rkyv-64" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-validation
Summary:        Date and time library for Rust - feature "rkyv-validation"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7/validation) >= 0.7.43
Provides:       crate(%{pkgname}/rkyv-validation)

%description -n %{name}+rkyv-validation
This metapackage enables feature "rkyv-validation" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Date and time library for Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Date and time library for Rust - feature "wasm-bindgen"
Requires:       crate(%{pkgname})
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.121
Provides:       crate(%{pkgname}/wasm-bindgen)

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasmbind
Summary:        Date and time library for Rust - feature "wasmbind"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/js-sys)
Requires:       crate(%{pkgname}/wasm-bindgen)
Provides:       crate(%{pkgname}/wasmbind)

%description -n %{name}+wasmbind
This metapackage enables feature "wasmbind" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows-link
Summary:        Date and time library for Rust - feature "windows-link" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(windows-link-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/winapi)
Provides:       crate(%{pkgname}/windows-link)

%description -n %{name}+windows-link
This metapackage enables feature "windows-link" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "winapi" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
