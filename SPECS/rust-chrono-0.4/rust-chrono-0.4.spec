# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/core-error) = %{version}
Provides:       crate(%{pkgname}/internal-bench) = %{version}
Provides:       crate(%{pkgname}/libc) = %{version}
Provides:       crate(%{pkgname}/now) = %{version}
Provides:       crate(%{pkgname}/oldtime) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "chrono"

%package     -n %{name}+arbitrary
Summary:        Date and time library for Rust - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.0.0
Requires:       crate(arbitrary-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clock
Summary:        Date and time library for Rust - feature "clock"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/iana-time-zone) = %{version}
Requires:       crate(%{pkgname}/now) = %{version}
Requires:       crate(%{pkgname}/winapi) = %{version}
Provides:       crate(%{pkgname}/clock) = %{version}

%description -n %{name}+clock
This metapackage enables feature "clock" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Date and time library for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clock) = %{version}
Requires:       crate(%{pkgname}/oldtime) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/wasmbind) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+defmt
Summary:        Date and time library for Rust - feature "defmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-1/default) >= 1.0.1
Requires:       crate(pure-rust-locales-0.8/defmt) >= 0.8.2
Provides:       crate(%{pkgname}/defmt) = %{version}

%description -n %{name}+defmt
This metapackage enables feature "defmt" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+iana-time-zone
Summary:        Date and time library for Rust - feature "iana-time-zone"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(iana-time-zone-0.1/default) >= 0.1.45
Requires:       crate(iana-time-zone-0.1/fallback) >= 0.1.45
Provides:       crate(%{pkgname}/iana-time-zone) = %{version}

%description -n %{name}+iana-time-zone
This metapackage enables feature "iana-time-zone" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+js-sys
Summary:        Date and time library for Rust - feature "js-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(js-sys-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/js-sys) = %{version}

%description -n %{name}+js-sys
This metapackage enables feature "js-sys" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pure-rust-locales
Summary:        Date and time library for Rust - feature "pure-rust-locales" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pure-rust-locales-0.8/default) >= 0.8.2
Provides:       crate(%{pkgname}/pure-rust-locales) = %{version}
Provides:       crate(%{pkgname}/unstable-locales) = %{version}

%description -n %{name}+pure-rust-locales
This metapackage enables feature "pure-rust-locales" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-locales" feature.

%package     -n %{name}+rkyv
Summary:        Date and time library for Rust - feature "rkyv" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.7) >= 0.7.43
Requires:       crate(rkyv-0.7/size-32) >= 0.7.43
Provides:       crate(%{pkgname}/rkyv) = %{version}
Provides:       crate(%{pkgname}/rkyv-32) = %{version}

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rkyv-32" feature.

%package     -n %{name}+rkyv-16
Summary:        Date and time library for Rust - feature "rkyv-16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.7) >= 0.7.43
Requires:       crate(rkyv-0.7/size-16) >= 0.7.43
Provides:       crate(%{pkgname}/rkyv-16) = %{version}

%description -n %{name}+rkyv-16
This metapackage enables feature "rkyv-16" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-64
Summary:        Date and time library for Rust - feature "rkyv-64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.7) >= 0.7.43
Requires:       crate(rkyv-0.7/size-64) >= 0.7.43
Provides:       crate(%{pkgname}/rkyv-64) = %{version}

%description -n %{name}+rkyv-64
This metapackage enables feature "rkyv-64" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-validation
Summary:        Date and time library for Rust - feature "rkyv-validation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.7/validation) >= 0.7.43
Provides:       crate(%{pkgname}/rkyv-validation) = %{version}

%description -n %{name}+rkyv-validation
This metapackage enables feature "rkyv-validation" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Date and time library for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.99
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Date and time library for Rust - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasmbind
Summary:        Date and time library for Rust - feature "wasmbind"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/js-sys) = %{version}
Requires:       crate(%{pkgname}/wasm-bindgen) = %{version}
Provides:       crate(%{pkgname}/wasmbind) = %{version}

%description -n %{name}+wasmbind
This metapackage enables feature "wasmbind" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows-link
Summary:        Date and time library for Rust - feature "windows-link" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-link-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/winapi) = %{version}
Provides:       crate(%{pkgname}/windows-link) = %{version}

%description -n %{name}+windows-link
This metapackage enables feature "windows-link" for the Rust chrono crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "winapi" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
