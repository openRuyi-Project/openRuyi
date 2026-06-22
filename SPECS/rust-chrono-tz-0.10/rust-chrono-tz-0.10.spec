# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name chrono-tz
%global full_version 0.10.4
%global pkgname chrono-tz-0.10

Name:           rust-chrono-tz-0.10
Version:        0.10.4
Release:        %autorelease
Summary:        Rust crate "chrono-tz"
License:        MIT OR Apache-2.0
URL:            https://github.com/chronotope/chrono-tz
#!RemoteAsset:  sha256:a6139a8597ed92cf816dfb33f5dd6cf0bb93a6adc938f11039f371bc5bcd26c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(chrono-0.4) >= 0.4.25
Requires:       crate(phf-0.12) >= 0.12.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "chrono-tz"

%package     -n %{name}+arbitrary
Summary:        TimeZone implementations for chrono from the IANA database - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.2.0
Requires:       crate(arbitrary-1/derive) >= 1.2.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust chrono-tz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+case-insensitive
Summary:        TimeZone implementations for chrono from the IANA database - feature "case-insensitive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/chrono-tz-build) = %{version}
Requires:       crate(chrono-tz-build-0.5/case-insensitive) >= 0.5.0
Requires:       crate(phf-0.12/uncased) >= 0.12.0
Requires:       crate(uncased-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/case-insensitive) = %{version}

%description -n %{name}+case-insensitive
This metapackage enables feature "case-insensitive" for the Rust chrono-tz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono-tz-build
Summary:        TimeZone implementations for chrono from the IANA database - feature "chrono-tz-build"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-tz-build-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/chrono-tz-build) = %{version}

%description -n %{name}+chrono-tz-build
This metapackage enables feature "chrono-tz-build" for the Rust chrono-tz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+filter-by-regex
Summary:        TimeZone implementations for chrono from the IANA database - feature "filter-by-regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/chrono-tz-build) = %{version}
Requires:       crate(chrono-tz-build-0.5/filter-by-regex) >= 0.5.0
Provides:       crate(%{pkgname}/filter-by-regex) = %{version}

%description -n %{name}+filter-by-regex
This metapackage enables feature "filter-by-regex" for the Rust chrono-tz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        TimeZone implementations for chrono from the IANA database - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.99
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust chrono-tz crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
