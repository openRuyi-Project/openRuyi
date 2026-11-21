# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name temporal_rs
%global full_version 0.2.6
%global pkgname temporal-rs-0.2

Name:           rust-temporal-rs-0.2
Version:        0.2.6
Release:        %autorelease
Summary:        Rust crate "temporal_rs"
License:        MIT OR Apache-2.0
URL:            https://github.com/boa-dev/temporal
#!RemoteAsset:  sha256:1a978fef907a27736827d336c0bfaab14fb8a7509dd6dc2b43c44e51d59aca5b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(calendrical-calculations-0.2/default) >= 0.2.4
Requires:       crate(core-maths-0.1/default) >= 0.1.1
Requires:       crate(icu-calendar-2/compiled-data) >= 2.2.1
Requires:       crate(icu-locale-core-2/default) >= 2.1.0
Requires:       crate(ixdtf-0.6/default) >= 0.6.4
Requires:       crate(ixdtf-0.6/duration) >= 0.6.4
Requires:       crate(num-traits-0.2) >= 0.2.19
Requires:       crate(timezone-provider-0.2) >= 0.2.6
Requires:       crate(tinystr-0.8/default) >= 0.8.0
Requires:       crate(writeable-0.6/default) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/float64-representable-durations) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "temporal_rs"

%package     -n %{name}+log
Summary:        Temporal in Rust is an implementation of the TC39 Temporal Builtin Proposal in Rust - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.28
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust temporal_rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sys
Summary:        Temporal in Rust is an implementation of the TC39 Temporal Builtin Proposal in Rust - feature "sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compiled-data) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(web-time-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/sys) = %{version}

%description -n %{name}+sys
This metapackage enables feature "sys" for the Rust temporal_rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sys-local
Summary:        Temporal in Rust is an implementation of the TC39 Temporal Builtin Proposal in Rust - feature "sys-local" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sys) = %{version}
Requires:       crate(iana-time-zone-0.1/default) >= 0.1.64
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/sys-local) = %{version}

%description -n %{name}+sys-local
This metapackage enables feature "sys-local" for the Rust temporal_rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tzdb
Summary:        Temporal in Rust is an implementation of the TC39 Temporal Builtin Proposal in Rust - feature "tzdb" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(timezone-provider-0.2/tzif) >= 0.2.6
Provides:       crate(%{pkgname}/compiled-data) = %{version}
Provides:       crate(%{pkgname}/tzdb) = %{version}

%description -n %{name}+tzdb
This metapackage enables feature "tzdb" for the Rust temporal_rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compiled_data" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
