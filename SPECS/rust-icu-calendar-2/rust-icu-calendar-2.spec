# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name icu_calendar
%global full_version 2.2.1
%global pkgname icu-calendar-2

Name:           rust-icu-calendar-2
Version:        2.2.1
Release:        %autorelease
Summary:        Rust crate "icu_calendar"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:a2b2acc6263f494f1df50685b53ff8e57869e47d5c6fe39c23d518ae9a4f3e45
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(calendrical-calculations-0.2) >= 0.2.4
Requires:       crate(displaydoc-0.2) >= 0.2.3
Requires:       crate(icu-locale-core-2) >= 2.2.0
Requires:       crate(icu-provider-2) >= 2.2.0
Requires:       crate(tinystr-0.8/zerovec) >= 0.8.3
Requires:       crate(zerovec-0.11/derive) >= 0.11.6

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "icu_calendar"

%package     -n %{name}+alloc
Summary:        Date APIs for Gregorian and non-Gregorian calendars - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(icu-locale-core-2/alloc) >= 2.2.0
Requires:       crate(serde-1/alloc) >= 1.0.220
Requires:       crate(serde-1/derive) >= 1.0.220
Requires:       crate(tinystr-0.8/alloc) >= 0.8.3
Requires:       crate(tinystr-0.8/zerovec) >= 0.8.3
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust icu_calendar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compiled-data
Summary:        Date APIs for Gregorian and non-Gregorian calendars - feature "compiled_data"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(icu-calendar-data-2) >= 2.2.0
Requires:       crate(icu-locale-2) >= 2.2.0
Requires:       crate(icu-locale-2/compiled-data) >= 2.2.0
Requires:       crate(icu-provider-2/baked) >= 2.2.0
Provides:       crate(%{pkgname}/compiled-data) = %{version}

%description -n %{name}+compiled-data
This metapackage enables feature "compiled_data" for the Rust icu_calendar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+datagen
Summary:        Date APIs for Gregorian and non-Gregorian calendars - feature "datagen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(databake-0.2/derive) >= 0.2.0
Requires:       crate(icu-provider-2/export) >= 2.2.0
Requires:       crate(tinystr-0.8/databake) >= 0.8.3
Requires:       crate(tinystr-0.8/zerovec) >= 0.8.3
Requires:       crate(zerovec-0.11/databake) >= 0.11.6
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Provides:       crate(%{pkgname}/datagen) = %{version}

%description -n %{name}+datagen
This metapackage enables feature "datagen" for the Rust icu_calendar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Date APIs for Gregorian and non-Gregorian calendars - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compiled-data) = %{version}
Requires:       crate(%{pkgname}/ixdtf) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust icu_calendar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ixdtf
Summary:        Date APIs for Gregorian and non-Gregorian calendars - feature "ixdtf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ixdtf-0.6) >= 0.6.5
Provides:       crate(%{pkgname}/ixdtf) = %{version}

%description -n %{name}+ixdtf
This metapackage enables feature "ixdtf" for the Rust icu_calendar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Date APIs for Gregorian and non-Gregorian calendars - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(calendrical-calculations-0.2/logging) >= 0.2.4
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust icu_calendar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Date APIs for Gregorian and non-Gregorian calendars - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(icu-provider-2/serde) >= 2.2.0
Requires:       crate(serde-1/derive) >= 1.0.220
Requires:       crate(tinystr-0.8/serde) >= 0.8.3
Requires:       crate(tinystr-0.8/zerovec) >= 0.8.3
Requires:       crate(zerovec-0.11/derive) >= 0.11.6
Requires:       crate(zerovec-0.11/serde) >= 0.11.6
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust icu_calendar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-chrono-0-4
Summary:        Date APIs for Gregorian and non-Gregorian calendars - feature "unstable_chrono_0_4"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/unstable-chrono-0-4) = %{version}

%description -n %{name}+unstable-chrono-0-4
This metapackage enables feature "unstable_chrono_0_4" for the Rust icu_calendar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-jiff-0-2
Summary:        Date APIs for Gregorian and non-Gregorian calendars - feature "unstable_jiff_0_2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jiff-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/unstable-jiff-0-2) = %{version}

%description -n %{name}+unstable-jiff-0-2
This metapackage enables feature "unstable_jiff_0_2" for the Rust icu_calendar crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-time-0-3
Summary:        Date APIs for Gregorian and non-Gregorian calendars - feature "unstable_time_0_3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/unstable-time-0-3) = %{version}

%description -n %{name}+unstable-time-0-3
This metapackage enables feature "unstable_time_0_3" for the Rust icu_calendar crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
